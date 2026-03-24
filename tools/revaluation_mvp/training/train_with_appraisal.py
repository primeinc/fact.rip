import gymnasium as gym
import torch
import sys
import os
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from envs.blob_revaluation_env import BlobRevaluationEnv
from models.appraisal_network import AppraisalNetwork

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    reliability = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    model_path = f"artifacts/models/ppo_with_appraisal_reliability{reliability}_seed{seed}.zip"
    if os.path.exists(model_path):
        print(f"Skipping existing WITH-APPRAISAL (reliability={reliability}, seed={seed})")
    else:
        appraisal_net = AppraisalNetwork()
        appraisal_net.load_state_dict(torch.load("artifacts/models/appraisal_model.pth", weights_only=True))
        appraisal_net.eval()

        env = BlobRevaluationEnv(mode="honest_revaluation", context_reliability=reliability, appraisal_model=appraisal_net)
        print(f"=== Training WITH-APPRAISAL (reliability={reliability}, seed={seed}) ===")
        check_env(env, warn=True)
        model = PPO("MlpPolicy", env, verbose=1, seed=seed, device="cpu")
        model.learn(total_timesteps=200_000, progress_bar=True)
        model.save(model_path.replace(".zip", ""))
        print(f"\u2713 WITH-APPRAISAL saved")
