import pandas as pd
import numpy as np
from scipy.stats import bootstrap
import glob

def aggregate():
    csvs = glob.glob("artifacts/tables/eval_*.csv")
    if not csvs:
        print("No CSVs found")
        return

    all_dfs = [pd.read_csv(f) for f in csvs]
    big_df = pd.concat(all_dfs, ignore_index=True)

    seed_summary = big_df.groupby(["train_type", "eval_type", "mode", "reliability", "seed"]).agg({
        "approached": "mean",
        "dwell_steps": "mean",
        "return": "mean",
        "appraisal_sum": "mean"
    }).reset_index()

    def ci95(series):
        if len(series) < 2:
            return series.mean(), np.nan, np.nan
        res = bootstrap((series.to_numpy(),), np.mean, confidence_level=0.95)
        return series.mean(), res.confidence_interval.low, res.confidence_interval.high

    final_summary = []
    for g, sub in seed_summary.groupby(["train_type", "eval_type", "mode", "reliability"]):
        m_approach, l_approach, u_approach = ci95(sub["approached"])
        m_dwell, l_dwell, u_dwell = ci95(sub["dwell_steps"])
        final_summary.append({
            "train_type": g[0],
            "eval_type": g[1],
            "mode": g[2],
            "reliability": g[3],
            "mean_approach_rate": m_approach,
            "ci95_approach_low": l_approach,
            "ci95_approach_high": u_approach,
            "mean_dwell": m_dwell,
            "ci95_dwell_low": l_dwell,
            "ci95_dwell_high": u_dwell,
            "n_seeds": len(sub),
        })

    summary_df = pd.DataFrame(final_summary)
    summary_df.to_csv("artifacts/tables/aggregated_summary.csv", index=False)
    print("\u2713 Aggregated across-seed results saved")
    print(summary_df.round(3))
    return summary_df

if __name__ == "__main__":
    aggregate()
