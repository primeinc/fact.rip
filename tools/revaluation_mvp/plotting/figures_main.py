import logging

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from utils.paths import FIGURES, TABLES, ensure_dirs

log = logging.getLogger(__name__)


def _safe_errbar(means, lows, highs):
    """Compute error bar arrays, replacing NaN with 0 so matplotlib doesn't choke."""
    lower = np.where(np.isnan(lows), 0.0, means - lows)
    upper = np.where(np.isnan(highs), 0.0, highs - means)
    return np.clip(lower, 0, None), np.clip(upper, 0, None)


def _plot_grouped_bars(ax, sub, metric, low, high, title):
    reliabilities = sorted(sub["reliability"].unique())
    train_types = list(sub["train_type"].unique())
    width = 0.35
    x = np.arange(len(reliabilities))

    for idx, tt in enumerate(train_types):
        tt_df = sub[sub["train_type"] == tt].sort_values("reliability")
        xpos = x + (idx - (len(train_types) - 1) / 2) * width
        means = tt_df[metric].to_numpy()
        lower, upper = _safe_errbar(means, tt_df[low].to_numpy(), tt_df[high].to_numpy())

        ax.bar(xpos, means, width=width, label=tt)
        ax.errorbar(xpos, means, yerr=[lower, upper], fmt="none", color="black", capsize=4)

    ax.set_xticks(x)
    ax.set_xticklabels([str(r) for r in reliabilities])
    ax.set_xlabel("Reliability")
    ax.set_title(title)


def make_main_figure():
    ensure_dirs()
    df = pd.read_csv(TABLES / "aggregated_summary.csv")
    df = df[df["eval_type"] == "raw"]

    has_cue_cols = "mean_approach_rate_cue1" in df.columns
    n_rows = 3 if has_cue_cols else 2

    fig, axes = plt.subplots(n_rows, 2, figsize=(14, 5 * n_rows), sharey="row")

    for i, mode in enumerate(["honest_revaluation", "fake_revaluation"]):
        sub = df[df["mode"] == mode]
        _plot_grouped_bars(
            axes[0, i], sub,
            "mean_approach_rate", "ci95_approach_low", "ci95_approach_high",
            f"Approach Rate -- {mode}"
        )
        _plot_grouped_bars(
            axes[1, i], sub,
            "mean_dwell", "ci95_dwell_low", "ci95_dwell_high",
            f"Mean Dwell -- {mode}"
        )

        if has_cue_cols:
            _plot_grouped_bars(
                axes[2, i], sub,
                "mean_approach_rate_cue1", "ci95_approach_cue1_low", "ci95_approach_cue1_high",
                f"Approach Rate (cue=1) -- {mode}"
            )

    axes[0, 0].legend()
    fig.suptitle("Cue-Conditioned Appraisal vs Raw-Only (raw eval, 95% bootstrap CI)")
    fig.tight_layout()
    fig.savefig(FIGURES / "figure_main_effects.png", dpi=300)
    fig.savefig(FIGURES / "figure_main_effects.svg", bbox_inches="tight")
    plt.close(fig)
    log.info("Saved %s", FIGURES / "figure_main_effects.png")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    make_main_figure()
