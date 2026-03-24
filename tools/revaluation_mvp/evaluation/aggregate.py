import glob
import logging
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import bootstrap

from utils.io import read_json, write_csv
from utils.paths import RUNS, TABLES, ensure_dirs

log = logging.getLogger(__name__)

_RNG = np.random.default_rng(42)


def _ci95(series: pd.Series):
    if len(series) < 2:
        return float(series.mean()), np.nan, np.nan
    res = bootstrap(
        (series.to_numpy(),),
        np.mean,
        confidence_level=0.95,
        random_state=_RNG,
    )
    return float(series.mean()), float(res.confidence_interval.low), float(res.confidence_interval.high)


def aggregate_results():
    ensure_dirs()
    summary_files = sorted(glob.glob(str(RUNS / "*__summary.json")))
    if not summary_files:
        log.warning("No run summaries found.")
        return None

    summaries = [read_json(Path(p)) for p in summary_files]
    seed_df = pd.DataFrame(summaries)
    write_csv(TABLES / "seed_level_summary.csv", seed_df)

    final_rows = []
    for g, sub in seed_df.groupby(["train_type", "eval_type", "mode", "reliability"]):
        m_a, l_a, u_a = _ci95(sub["mean_approach_rate"])
        m_d, l_d, u_d = _ci95(sub["mean_dwell"])
        m_r, l_r, u_r = _ci95(sub["mean_return"])

        row = {
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
        }

        # Cue-conditional approach rates (may be NaN if column missing in older runs)
        if "mean_approach_rate_cue1" in sub.columns:
            cue1 = sub["mean_approach_rate_cue1"].dropna()
            cue0 = sub["mean_approach_rate_cue0"].dropna()
            m1, l1, u1 = _ci95(cue1) if len(cue1) >= 1 else (np.nan, np.nan, np.nan)
            m0, l0, u0 = _ci95(cue0) if len(cue0) >= 1 else (np.nan, np.nan, np.nan)
            row.update({
                "mean_approach_rate_cue1": m1,
                "ci95_approach_cue1_low": l1,
                "ci95_approach_cue1_high": u1,
                "mean_approach_rate_cue0": m0,
                "ci95_approach_cue0_low": l0,
                "ci95_approach_cue0_high": u0,
            })

        final_rows.append(row)

    final_df = pd.DataFrame(final_rows)
    out = TABLES / "aggregated_summary.csv"
    write_csv(out, final_df)
    log.info("Wrote %s (%d rows)", out, len(final_df))
    return seed_df, final_df


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    aggregate_results()
