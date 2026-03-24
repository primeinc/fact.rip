"""
ONE COMMAND ENTRYPOINT — full reproducible experiment
"""
import subprocess
import os

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)
    os.makedirs("figures", exist_ok=True)
    os.makedirs("artifacts/models", exist_ok=True)
    os.makedirs("artifacts/tables", exist_ok=True)
    os.makedirs("artifacts/figures", exist_ok=True)

    print("=== Reproducing full SSOT MVP experiment ===")
    subprocess.run(["python", "-m", "training.train_appraisal"], check=True)
    subprocess.run(["python", "-m", "run_experiment"], check=True)
    print("\u2705 Experiment complete. All artifacts in ./artifacts/")
    print("   Tables  \u2192 artifacts/tables/")
    print("   Figures \u2192 artifacts/figures/")
    print("   Models  \u2192 artifacts/models/")
