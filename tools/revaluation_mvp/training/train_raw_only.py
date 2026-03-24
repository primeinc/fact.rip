import sys
from pathlib import Path
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from envs.blob_revaluation_env import BlobRevaluationEnv
from utils.paths import MODELS, ensure_dirs


def model_path(seed: int, reliability: float) -> Path:
    ensure_dirs()
    return MODELS / f"ppo_raw_only_rel_{reliability}_seed{seed}.zip"


def train(
    seed: int,
    reliability: float,
    total_timesteps: int = 200000,
    device: str = "cpu",
    env_cfg: dict | None = None,
):
    out = model_path(seed, reliability)
    if out.exists():
        print(f"Skipping existing RAW-ONLY (reliability={reliability}, seed={seed})")
        return out

    env_kwargs = env_cfg or {}
    env = BlobRevaluationEnv(
        mode="honest_revaluation",
        context_reliability=reliability,
        appraisal_model=None,
        include_cue=True,
        **env_kwargs,
    )
    print(f"=== Training RAW-ONLY (cue-visible, no bonus) | rel={reliability} seed={seed} ===")
    check_env(env, warn=True)
    model = PPO("MlpPolicy", env, verbose=1, seed=seed, device=device)
    model.learn(total_timesteps=total_timesteps, progress_bar=True)
    model.save(out.with_suffix(""))
    print(f"\u2713 Saved {out}")
    return out


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    reliability = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    train(seed, reliability)
