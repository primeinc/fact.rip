import logging
import sys
from pathlib import Path
from stable_baselines3 import PPO

from envs.blob_revaluation_env import BlobRevaluationEnv
from models.appraisal_network import load_appraisal_model
from utils.paths import MODELS, ensure_dirs
from utils.seed import set_global_seed

log = logging.getLogger(__name__)

_ENV_EXPLICIT_KEYS = frozenset({"mode", "context_reliability", "appraisal_model", "include_cue"})


def model_path(seed: int, reliability: float) -> Path:
    ensure_dirs()
    return MODELS / f"ppo_with_appraisal_rel_{reliability}_seed{seed}.zip"


def train(
    seed: int,
    reliability: float,
    total_timesteps: int = 200000,
    device: str = "cpu",
    env_cfg: dict | None = None,
):
    out = model_path(seed, reliability)
    if out.exists():
        log.info("Skipping existing WITH-APPRAISAL (rel=%s, seed=%d)", reliability, seed)
        return out

    set_global_seed(seed)
    try:
        appraisal_net = load_appraisal_model(reliability)
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"Appraisal model weights not found for reliability={reliability}. "
            "Run 'run_experiment.py' or 'train_appraisal_layer' first."
        ) from exc
    env_kwargs = {k: v for k, v in (env_cfg or {}).items() if k not in _ENV_EXPLICIT_KEYS}
    env = BlobRevaluationEnv(
        mode="honest_revaluation",
        context_reliability=reliability,
        appraisal_model=appraisal_net,
        include_cue=True,
        **env_kwargs,
    )
    log.info("Training WITH-APPRAISAL | rel=%s seed=%d", reliability, seed)
    model = PPO("MlpPolicy", env, verbose=0, seed=seed, device=device)
    model.learn(total_timesteps=total_timesteps)
    model.save(out.with_suffix(""))
    log.info("Saved %s", out)
    return out


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
    reliability = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    train(seed, reliability)
