import gymnasium as gym
import sys
import os
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from envs.blob_revaluation_env import BlobRevaluationEnv

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    reliability = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    model_path = f"artifacts/models/ppo_raw_only_reliability{reliability}_seed{seed}.zip"
    if os.path.exists(model_path):
        print(f"Skipping existing RAW-ONLY (reliability={reliability}, seed={seed})")
    else:
        env = BlobRevaluationEnv(mode="honest_revaluation", context_reliability=reliability, appraisal_model=None)
        print(f"=== Training RAW-ONLY (reliability={reliability}, seed={seed}) ===")
        check_env(env, warn=True)
        model = PPO("MlpPolicy", env, verbose=1, seed=seed, device="cpu")
        model.learn(total_timesteps=200_000, progress_bar=True)
        model.save(model_path.replace(".zip", ""))
        print(f"\u2713 RAW-ONLY saved")
