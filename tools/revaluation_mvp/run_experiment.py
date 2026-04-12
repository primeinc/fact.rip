"""
Full experiment runner -- one command entrypoint.

Three-way comparison: RAW-ONLY vs APPRAISAL vs HOMEOSTATIC (EMG).

Logs to both console and artifacts/experiment.log with timestamps.
Progress is tracked in artifacts/progress.json for observability.

Usage:
    uv run python run_experiment.py                        # uses configs/base.yaml
    uv run python run_experiment.py --config configs/debug.yaml
    uv run python run_experiment.py --clean                # wipe artifacts and re-run
"""
import argparse
import hashlib
import json
import logging
import shutil
import sys
import time

import yaml

from evaluation.aggregate import aggregate_results
from evaluation.evaluate import evaluate_run
from models.appraisal_network import appraisal_model_path, train_appraisal_layer
from plotting.figures_2x2 import make_2x2_figure
from plotting.figures_main import make_main_figure
from training.train_homeostatic import model_path as emg_model_path
from training.train_homeostatic import train as train_emg
from training.train_raw_only import model_path as raw_model_path
from training.train_raw_only import train as train_raw
from training.train_with_appraisal import model_path as app_model_path
from training.train_with_appraisal import train as train_app
from utils.paths import ARTIFACTS, CONFIGS, ensure_dirs

LOG_FILE = ARTIFACTS / "experiment.log"
PROGRESS_FILE = ARTIFACTS / "progress.json"
CONFIG_HASH_FILE = ARTIFACTS / "config_hash.json"

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

def setup_logging():
    """Configure logging to both console (INFO) and file (DEBUG)."""
    logger = logging.getLogger("experiment")
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(message)s", datefmt="%H:%M:%S"
    )

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    fh = logging.FileHandler(LOG_FILE, mode="w")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger


# ---------------------------------------------------------------------------
# Config hash validation
# ---------------------------------------------------------------------------

def _config_hash(cfg: dict) -> str:
    raw = json.dumps(cfg, sort_keys=True, default=str)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _check_config_hash(cfg: dict, log, clean: bool) -> None:
    current = _config_hash(cfg)
    if CONFIG_HASH_FILE.exists():
        saved = json.loads(CONFIG_HASH_FILE.read_text())
        if saved.get("hash") != current:
            if clean:
                log.warning("Config changed -- wiping stale artifacts (--clean).")
                for d in [ARTIFACTS / "runs", ARTIFACTS / "tables",
                          ARTIFACTS / "figures", ARTIFACTS / "models"]:
                    if d.exists():
                        shutil.rmtree(d)
                ensure_dirs()
            else:
                log.error(
                    "Config hash mismatch! Cached artifacts were produced with a "
                    "different config. Re-run with --clean to wipe stale results, "
                    "or delete artifacts/ manually."
                )
                sys.exit(1)
    CONFIG_HASH_FILE.write_text(json.dumps({"hash": current}))


# ---------------------------------------------------------------------------
# Progress tracking
# ---------------------------------------------------------------------------

def _fmt_duration(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}h{m:02d}m{s:02d}s"
    return f"{m}m{s:02d}s"


class ProgressTracker:
    """Write a JSON file after every step so progress is observable."""

    def __init__(self, total_train, total_eval):
        self.total_train = total_train
        self.total_eval = total_eval
        self.train_done = 0
        self.eval_done = 0
        self.phase = "init"
        self.current = ""
        self.start_time = time.time()
        self._write()

    def _write(self):
        elapsed = time.time() - self.start_time
        data = {
            "phase": self.phase,
            "current": self.current,
            "training": f"{self.train_done}/{self.total_train}",
            "evaluation": f"{self.eval_done}/{self.total_eval}",
            "elapsed_s": round(elapsed, 1),
            "elapsed_human": _fmt_duration(elapsed),
        }
        PROGRESS_FILE.write_text(json.dumps(data, indent=2))

    def start_train(self, label):
        self.phase = "training"
        self.current = label
        self._write()

    def finish_train(self):
        self.train_done += 1
        self._write()

    def start_eval(self, label):
        self.phase = "evaluation"
        self.current = label
        self._write()

    def finish_eval(self):
        self.eval_done += 1
        self._write()

    def done(self):
        self.phase = "complete"
        self.current = ""
        self._write()


def load_config(path=None):
    cfg_path = path if path else CONFIGS / "base.yaml"
    with open(cfg_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="Run the full revaluation MVP experiment.")
    parser.add_argument(
        "--config",
        default=None,
        help="Path to a YAML config file (default: configs/base.yaml)",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Wipe stale artifacts if config has changed",
    )
    args = parser.parse_args()

    ensure_dirs()
    log = setup_logging()
    cfg = load_config(args.config)

    _check_config_hash(cfg, log, clean=args.clean)

    env_cfg = cfg.get("environment", {})
    device = cfg["training"].get("device", "cpu")

    seeds = cfg["seeds"]
    rels = cfg["reliabilities"]
    modes = cfg["eval_modes"]
    # 3 training perspectives: RAW, APP, EMG
    total_train = len(rels) * len(seeds) * 3
    # Eval: modes × (raw + appraisal eval_types) × (raw_only + app + emg train_types)
    # Plus: homeostatic mode × (standard eval_type) × (emg train_type)
    total_eval_classic = len(rels) * len(seeds) * len(modes) * 2 * 2  # RAW/APP
    total_eval_emg = len(rels) * len(seeds) * len(modes)  # EMG on classic modes
    total_eval_homeostatic = len(rels) * len(seeds) * 3  # all 3 agents on homeostatic
    total_eval = total_eval_classic + total_eval_emg + total_eval_homeostatic
    progress = ProgressTracker(total_train, total_eval)

    log.info("Experiment started -- %d train runs, %d eval runs", total_train, total_eval)
    log.info("Config: seeds=%s  reliabilities=%s  timesteps=%s",
             seeds, rels, cfg["training"]["total_timesteps"])

    # --- Appraisal models (one per reliability level) ---
    for rel in rels:
        if not appraisal_model_path(rel).exists():
            log.info("Training appraisal network (reliability=%.2f) ...", rel)
            train_appraisal_layer(
                reliability=rel,
                positive_bonus_target=cfg["appraisal"]["positive_bonus_target"],
            )
        else:
            log.info("Appraisal network (reliability=%.2f) already exists -- skipping.", rel)

    # --- Training + evaluation loop ---
    for ri, rel in enumerate(rels):
        for si, seed in enumerate(seeds):
            pair_label = f"rel={rel} seed={seed}"
            pair_idx = ri * len(seeds) + si + 1
            pair_total = len(rels) * len(seeds)

            # Train RAW
            label = f"[{pair_idx}/{pair_total}] RAW-ONLY  {pair_label}"
            log.info("TRAIN  %s", label)
            progress.start_train(label)
            t0 = time.time()
            train_raw(
                seed, rel,
                total_timesteps=cfg["training"]["total_timesteps"],
                device=device,
                env_cfg=env_cfg,
            )
            log.info("TRAIN  %s  done in %s", label, _fmt_duration(time.time() - t0))
            progress.finish_train()

            # Train APPRAISAL
            label = f"[{pair_idx}/{pair_total}] APPRAISAL {pair_label}"
            log.info("TRAIN  %s", label)
            progress.start_train(label)
            t0 = time.time()
            train_app(
                seed, rel,
                total_timesteps=cfg["training"]["total_timesteps"],
                device=device,
                env_cfg=env_cfg,
            )
            log.info("TRAIN  %s  done in %s", label, _fmt_duration(time.time() - t0))
            progress.finish_train()

            # Train HOMEOSTATIC (EMG)
            label = f"[{pair_idx}/{pair_total}] EMG       {pair_label}"
            log.info("TRAIN  %s", label)
            progress.start_train(label)
            t0 = time.time()
            train_emg(
                seed, rel,
                total_timesteps=cfg["training"]["total_timesteps"],
                device=device,
                env_cfg=env_cfg,
            )
            log.info("TRAIN  %s  done in %s", label, _fmt_duration(time.time() - t0))
            progress.finish_train()

            # Evaluate RAW & APP on classic modes (honest/fake revaluation)
            for mode in modes:
                for eval_type in ["raw", "appraisal"]:
                    for train_type, model_path_fn, train_label in [
                        ("raw_only", raw_model_path, "RAW"),
                        ("with_appraisal", app_model_path, "APP"),
                    ]:
                        elabel = f"{train_label}/{eval_type}/{mode} {pair_label}"
                        log.debug("EVAL   %s", elabel)
                        progress.start_eval(elabel)
                        evaluate_run(
                            model_path=model_path_fn(seed, rel),
                            train_type=train_type,
                            eval_type=eval_type,
                            mode=mode,
                            reliability=rel,
                            seed=seed,
                            num_episodes=cfg["evaluation"]["num_episodes"],
                            device=device,
                            env_cfg=env_cfg,
                        )
                        progress.finish_eval()

                # Evaluate EMG on classic modes (standard eval, no appraisal swap)
                elabel = f"EMG/standard/{mode} {pair_label}"
                log.debug("EVAL   %s", elabel)
                progress.start_eval(elabel)
                evaluate_run(
                    model_path=emg_model_path(seed, rel),
                    train_type="homeostatic",
                    eval_type="standard",
                    mode=mode,
                    reliability=rel,
                    seed=seed,
                    num_episodes=cfg["evaluation"]["num_episodes"],
                    device=device,
                    env_cfg=env_cfg,
                )
                progress.finish_eval()

            # Evaluate all 3 agents on homeostatic mode (survival metrics)
            for train_type, model_path_fn, train_label in [
                ("raw_only", raw_model_path, "RAW"),
                ("with_appraisal", app_model_path, "APP"),
                ("homeostatic", emg_model_path, "EMG"),
            ]:
                elabel = f"{train_label}/standard/homeostatic {pair_label}"
                log.debug("EVAL   %s", elabel)
                progress.start_eval(elabel)
                evaluate_run(
                    model_path=model_path_fn(seed, rel),
                    train_type=train_type,
                    eval_type="standard",
                    mode="homeostatic",
                    reliability=rel,
                    seed=seed,
                    num_episodes=cfg["evaluation"]["num_episodes"],
                    device=device,
                    env_cfg=env_cfg,
                )
                progress.finish_eval()

            log.info("Completed %s -- evals done: %d/%d",
                     pair_label, progress.eval_done, total_eval)

    # --- Aggregate & plot ---
    log.info("Aggregating results ...")
    aggregate_results()
    log.info("Generating figures ...")
    make_main_figure()
    make_2x2_figure()

    progress.done()
    log.info("Experiment complete. Total time: %s",
             _fmt_duration(time.time() - progress.start_time))


if __name__ == "__main__":
    main()
