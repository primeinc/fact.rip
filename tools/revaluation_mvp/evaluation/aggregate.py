import glob
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import bootstrap

from utils.io import read_json, write_csv
from utils.paths import RUNS, TABLES, ensure_dirs


def _ci95(series: pd.Series):
    if len(series) < 2:
        return float(series.mean()), np.nan, np.nan
    res = bootstrap((series.to_numpy(),), np.mean, confidence_level=0.95)
    return float(series.mean()), float(res.confidence_interval.low), float(res.confidence_interval.high)


def aggregate_results():
    ensure_dirs()
    summary_files = sorted(glob.glob(str(RUNS / "*__summary.json")))
    if not summary_files:
        print("No run summaries found.")
        return None

    summaries = [read_json(Path(p)) for p in summary_files]
    seed_df = pd.DataFrame(summaries)
    write_csv(TABLES / "seed_level_summary.csv", seed_df)

    final_rows = []
    for g, sub in seed_df.groupby(["train_type", "eval_type", "mode", "reliability"]):
        m_a, l_a, u_a = _ci95(sub["mean_approach_rate"])
        m_d, l_d, u_d = _ci95(sub["mean_dwell"])
        m_r, l_r, u_r = _ci95(sub["mean_return"])
        final_rows.append({
            "train_type": g[0],
            "eval_type": g[1],
            "mode": g[2],
            "reliability": g[3],
            "mean_approach_rate": m_a,
            "ci95_approach_low": l_a,
            "ci95_approach_high": u_a,
            "mean_dwell": m_d,
            "ci95_dwell_low": l_d,
            "ci95_dwell_high": u_d,
            "mean_return": m_r,
            "ci95_return_low": l_r,
            "ci95_return_high": u_r,
            "n_seeds": int(len(sub)),
        })

    final_df = pd.DataFrame(final_rows)
    write_csv(TABLES / "aggregated_summary.csv", final_df)
    print(f"\u2713 Wrote {TABLES / 'aggregated_summary.csv'}")
    return seed_df, final_df


if __name__ == "__main__":
    aggregate_results()
