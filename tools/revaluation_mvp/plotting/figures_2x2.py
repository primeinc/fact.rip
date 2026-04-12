import logging

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from utils.paths import FIGURES, TABLES, ensure_dirs

log = logging.getLogger(__name__)


def make_2x2_figure():
    ensure_dirs()
    df = pd.read_csv(TABLES / "aggregated_summary.csv")
    df = df[df["reliability"] == 1.0]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    for i, mode in enumerate(["honest_revaluation", "fake_revaluation"]):
        sub = df[df["mode"] == mode].copy()
        sub["cell"] = sub["train_type"] + " -> " + sub["eval_type"]
        sub = sub.sort_values(["train_type", "eval_type"])
        x = np.arange(len(sub))
        means = sub["mean_return"].to_numpy()
        lower = means - sub["ci95_return_low"].to_numpy()
        upper = sub["ci95_return_high"].to_numpy() - means

        axes[i].bar(x, means)
        axes[i].errorbar(x, means, yerr=[lower, upper], fmt="none", color="black", capsize=4)
        axes[i].set_xticks(x)
        axes[i].set_xticklabels(sub["cell"], rotation=20, ha="right")
        axes[i].set_title(f"2x2 mechanism -- {mode}")
        axes[i].set_ylabel("Mean return")

    fig.tight_layout()
    fig.savefig(FIGURES / "figure_2x2_mechanism.png", dpi=300)
    fig.savefig(FIGURES / "figure_2x2_mechanism.svg", bbox_inches="tight")
    plt.close(fig)
    log.info("Saved %s", FIGURES / "figure_2x2_mechanism.png")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    make_2x2_figure()
