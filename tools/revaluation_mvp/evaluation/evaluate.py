import logging
import pandas as pd
import numpy as np
from pathlib import Path
from stable_baselines3 import PPO

from envs.blob_revaluation_env import BlobRevaluationEnv
from models.appraisal_network import load_appraisal_model
from utils.io import write_csv, write_json
from utils.metadata import run_id
from utils.paths import RUNS, ensure_dirs

log = logging.getLogger(__name__)

_ENV_EXPLICIT_KEYS = frozenset({"mode", "context_reliability", "appraisal_model", "include_cue"})


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
    rid = run_id(train_type, eval_type, mode, reliability, seed)
    summary_path = RUNS / f"{rid}__summary.json"
    if summary_path.exists():
        log.debug("Skipping existing eval %s", rid)
        return None, None

    appraisal_net = load_appraisal_model(reliability) if eval_type == "appraisal" else None
    env_kwargs = {k: v for k, v in (env_cfg or {}).items() if k not in _ENV_EXPLICIT_KEYS}
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
        obs, _ = env.reset(seed=seed + 10_000 + ep)
        done = False
        episode_return = 0.0
        dwell = 0
        entered = False
        total_appraisal = 0.0
        context_cue = env.context_cue

        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            episode_return += reward
            done = terminated or truncated
            if info["on_aversive"]:
                dwell += 1
            if info["visited_aversive"] and not entered:
                entered = True
                total_appraisal += info.get("appraisal_bonus", 0.0)

        rows.append({
            "episode": ep,
            "return": episode_return,
            "approached": int(entered),
            "dwell_steps": dwell,
            "appraisal_sum": total_appraisal,
            "context_cue": int(context_cue),
            "train_type": train_type,
            "eval_type": eval_type,
            "mode": mode,
            "reliability": reliability,
            "seed": seed,
        })

    df = pd.DataFrame(rows)
    episode_path = RUNS / f"{rid}__episodes.csv"

    write_csv(episode_path, df)

    # Cue-conditional approach rates
    cue1 = df[df["context_cue"] == 1]
    cue0 = df[df["context_cue"] == 0]

    summary = {
        "run_id": rid,
        "train_type": train_type,
        "eval_type": eval_type,
        "mode": mode,
        "reliability": reliability,
        "seed": seed,
        "mean_approach_rate": float(df["approached"].mean()),
        "mean_approach_rate_cue1": float(cue1["approached"].mean()) if len(cue1) > 0 else float("nan"),
        "mean_approach_rate_cue0": float(cue0["approached"].mean()) if len(cue0) > 0 else float("nan"),
        "mean_dwell": float(df["dwell_steps"].mean()),
        "mean_return": float(df["return"].mean()),
        "mean_appraisal_sum": float(df["appraisal_sum"].mean()),
        "episode_csv": str(episode_path),
    }
    write_json(summary_path, summary)
    log.debug("Evaluated %s", rid)
    return df, summary
