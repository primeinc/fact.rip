import pandas as pd
import numpy as np
from pathlib import Path
from stable_baselines3 import PPO

from envs.blob_revaluation_env import BlobRevaluationEnv
from models.appraisal_network import load_appraisal_model
from utils.io import write_csv, write_json
from utils.metadata import run_id
from utils.paths import RUNS, ensure_dirs


def evaluate_run(
    model_path: Path,
    train_type: str,
    eval_type: str,
    mode: str,
    reliability: float,
    seed: int,
    num_episodes: int = 500,
    device: str = "cpu",
    env_cfg: dict | None = None,
):
    ensure_dirs()
    appraisal_net = load_appraisal_model() if eval_type == "appraisal" else None
    env_kwargs = env_cfg or {}
    env = BlobRevaluationEnv(
        mode=mode,
        context_reliability=reliability,
        appraisal_model=appraisal_net,
        include_cue=True,
        **env_kwargs,
    )
    model = PPO.load(model_path, device=device)

    rows = []
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

        rows.append({
            "episode": ep,
            "return": episode_return,
            "approached": int(entered),
            "dwell_steps": dwell,
            "appraisal_sum": total_appraisal,
            "train_type": train_type,
            "eval_type": eval_type,
            "mode": mode,
            "reliability": reliability,
            "seed": seed,
        })

    df = pd.DataFrame(rows)
    rid = run_id(train_type, eval_type, mode, reliability, seed)
    episode_path = RUNS / f"{rid}__episodes.csv"
    summary_path = RUNS / f"{rid}__summary.json"

    write_csv(episode_path, df)

    summary = {
        "run_id": rid,
        "train_type": train_type,
        "eval_type": eval_type,
        "mode": mode,
        "reliability": reliability,
        "seed": seed,
        "mean_approach_rate": float(df["approached"].mean()),
        "mean_dwell": float(df["dwell_steps"].mean()),
        "mean_return": float(df["return"].mean()),
        "mean_appraisal_sum": float(df["appraisal_sum"].mean()),
        "episode_csv": str(episode_path),
    }
    write_json(summary_path, summary)
    print(f"\u2713 Evaluated {rid}")
    return df, summary
