import gymnasium as gym
import numpy as np
import pandas as pd
import torch
import sys
from stable_baselines3 import PPO
from envs.blob_revaluation_env import BlobRevaluationEnv
from models.appraisal_network import AppraisalNetwork

def run_eval(model_path: str, use_appraisal_eval: bool, label: str, train_type: str, mode: str, reliability: float, seed: int, num_episodes: int = 500):
    appraisal_net = AppraisalNetwork().eval() if use_appraisal_eval else None
    if use_appraisal_eval:
        appraisal_net.load_state_dict(torch.load("artifacts/models/appraisal_model.pth", weights_only=True))

    env = BlobRevaluationEnv(mode=mode, context_reliability=reliability, appraisal_model=appraisal_net)
    model = PPO.load(model_path, device="cpu")

    records = []
    for ep in range(num_episodes):
        obs, _ = env.reset(seed=seed + ep)
        done = False
        episode_return = 0.0
        dwell = 0
        entered = False
        total_appraisal = 0.0
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            episode_return += reward
            done = terminated or truncated
            if np.allclose(obs[:2], obs[4:6], atol=1e-5):
                dwell += 1
                entered = True
                total_appraisal += info.get("appraisal_bonus", 0.0)
        records.append({
            "episode": ep,
            "return": episode_return,
            "approached": int(entered),
            "dwell_steps": dwell,
            "appraisal_sum": total_appraisal,
            "train_type": train_type,
            "eval_type": "appraisal" if use_appraisal_eval else "raw",
            "mode": mode,
            "reliability": reliability,
            "seed": seed,
        })

    df = pd.DataFrame(records)
    csv_name = f"artifacts/tables/eval_{train_type}_trained_to_{'appraisal' if use_appraisal_eval else 'raw'}_eval_mode{mode}_reliability{reliability}_seed{seed}.csv"
    df.to_csv(csv_name, index=False)
    approach = df["approached"].mean()
    dwell = df["dwell_steps"].mean()
    appraisal = df["appraisal_sum"].mean()
    print(f"{label:30} | Approach: {approach:.3f} | Dwell: {dwell:.2f} | Mean appraisal: {appraisal:.3f} | Saved {csv_name}")
    return df

if __name__ == "__main__":
    model_path = sys.argv[1]
    use_appraisal_eval = sys.argv[2].lower() == "true"
    label = sys.argv[3]
    train_type = sys.argv[4]
    mode = sys.argv[5]
    reliability = float(sys.argv[6])
    seed = int(sys.argv[7])
    run_eval(model_path, use_appraisal_eval, label, train_type, mode, reliability, seed)
