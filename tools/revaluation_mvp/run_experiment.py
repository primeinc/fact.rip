"""
Full experiment runner — one command entrypoint.
"""
import yaml

from utils.paths import CONFIGS, ensure_dirs
from models.appraisal_network import appraisal_model_path, train_appraisal_layer
from training.train_raw_only import train as train_raw
from training.train_with_appraisal import train as train_app
from evaluation.evaluate import evaluate_run
from evaluation.aggregate import aggregate_results
from plotting.figures_main import make_main_figure
from plotting.figures_2x2 import make_2x2_figure
from training.train_raw_only import model_path as raw_model_path
from training.train_with_appraisal import model_path as app_model_path


def load_config():
    with open(CONFIGS / "base.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    ensure_dirs()
    cfg = load_config()

    if not appraisal_model_path().exists():
        print("=== Generating appraisal model ===")
        train_appraisal_layer(
            num_samples=cfg["appraisal"]["num_samples"],
            epochs=cfg["appraisal"]["epochs"],
            lr=cfg["appraisal"]["lr"],
            positive_bonus_target=cfg["appraisal"]["positive_bonus_target"],
        )

    for rel in cfg["reliabilities"]:
        for seed in cfg["seeds"]:
            print(f"\n=== Reliability={rel} | Seed={seed} ===")
            train_raw(seed, rel, total_timesteps=cfg["training"]["total_timesteps"])
            train_app(seed, rel, total_timesteps=cfg["training"]["total_timesteps"])

            for mode in cfg["eval_modes"]:
                for eval_type in ["raw", "appraisal"]:
                    evaluate_run(
                        model_path=raw_model_path(seed, rel),
                        train_type="raw_only",
                        eval_type=eval_type,
                        mode=mode,
                        reliability=rel,
                        seed=seed,
                        num_episodes=cfg["evaluation"]["num_episodes"],
                    )
                    evaluate_run(
                        model_path=app_model_path(seed, rel),
                        train_type="with_appraisal",
                        eval_type=eval_type,
                        mode=mode,
                        reliability=rel,
                        seed=seed,
                        num_episodes=cfg["evaluation"]["num_episodes"],
                    )

    aggregate_results()
    make_main_figure()
    make_2x2_figure()
    print("\u2705 Full experiment complete.")


if __name__ == "__main__":
    main()
