"""
Full grid runner — called by reproduce.py
"""
import subprocess
import os
import yaml

with open("configs/base.yaml") as f:
    config = yaml.safe_load(f)

SEEDS = config["seeds"]
RELIABILITIES = config["reliabilities"]
EVAL_MODES = config["modes"]

if __name__ == "__main__":
    os.makedirs("artifacts/tables", exist_ok=True)
    os.makedirs("artifacts/models", exist_ok=True)

    print("=== Running full publishable grid ===")
    for rel in RELIABILITIES:
        for seed in SEEDS:
            print(f"\n=== Reliability={rel} | Seed={seed} ===")
            subprocess.run(["python", "-m", "training.train_raw_only", str(seed), str(rel)], check=True)
            subprocess.run(["python", "-m", "training.train_with_appraisal", str(seed), str(rel)], check=True)

            for train_type in ["raw_only", "with_appraisal"]:
                model_path = f"artifacts/models/ppo_{train_type}_reliability{rel}_seed{seed}"
                for eval_appraisal in [False, True]:
                    for eval_mode in EVAL_MODES:
                        label = f"{train_type}_trained_to_{'appraisal' if eval_appraisal else 'raw'}_eval"
                        subprocess.run([
                            "python", "-m", "evaluation.evaluate",
                            model_path, str(eval_appraisal), label, train_type,
                            eval_mode, str(rel), str(seed)
                        ], check=True)

    print("\n\u2705 Full grid complete.")
