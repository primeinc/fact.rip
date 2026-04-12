import json

from evaluation.aggregate import aggregate_results


def _write_summary(path, *, train_type, eval_type, mode, reliability, seed, approach, ret):
    summary = {
        "run_id": f"{train_type}_{eval_type}_{mode}_{reliability}_{seed}",
        "train_type": train_type,
        "eval_type": eval_type,
        "mode": mode,
        "reliability": reliability,
        "seed": seed,
        "mean_approach_rate": approach,
        "mean_approach_rate_cue1": approach + 0.05,
        "mean_approach_rate_cue0": approach - 0.05,
        "mean_dwell": 2.0,
        "mean_return": ret,
        "mean_appraisal_sum": 0.1,
        "episode_csv": "",
    }
    (path / f"{summary['run_id']}__summary.json").write_text(json.dumps(summary))


def test_aggregate_results_produces_expected_schema(tmp_path, monkeypatch):
    import evaluation.aggregate as agg
    import utils.paths as p

    runs_tmp = tmp_path / "runs"
    tables_tmp = tmp_path / "tables"
    runs_tmp.mkdir(exist_ok=True)
    tables_tmp.mkdir(exist_ok=True)
    monkeypatch.setattr(p, "RUNS", runs_tmp)
    monkeypatch.setattr(p, "TABLES", tables_tmp)
    monkeypatch.setattr(agg, "RUNS", runs_tmp)
    monkeypatch.setattr(agg, "TABLES", tables_tmp)

    # Write two seeds for one group so CIs can be computed
    for seed in [0, 1]:
        _write_summary(
            runs_tmp,
            train_type="raw_only",
            eval_type="raw",
            mode="honest_revaluation",
            reliability=1.0,
            seed=seed,
            approach=0.8 - seed * 0.1,
            ret=0.5 + seed * 0.05,
        )

    result = aggregate_results()
    assert result is not None, "aggregate_results returned None with valid inputs"
    _, final_df = result

    expected_cols = {
        "train_type", "eval_type", "mode", "reliability",
        "mean_approach_rate", "ci95_approach_low", "ci95_approach_high",
        "mean_dwell", "ci95_dwell_low", "ci95_dwell_high",
        "mean_return", "ci95_return_low", "ci95_return_high",
        "n_seeds",
        "mean_approach_rate_cue1", "ci95_approach_cue1_low", "ci95_approach_cue1_high",
        "mean_approach_rate_cue0", "ci95_approach_cue0_low", "ci95_approach_cue0_high",
    }
    assert expected_cols <= set(final_df.columns), (
        f"Missing columns: {expected_cols - set(final_df.columns)}"
    )

    # One group → one row
    assert len(final_df) == 1, f"Expected 1 aggregated row, got {len(final_df)}"
    row = final_df.iloc[0]
    assert row["n_seeds"] == 2
    assert row["train_type"] == "raw_only"
    assert row["eval_type"] == "raw"
    assert row["mode"] == "honest_revaluation"
    assert row["reliability"] == 1.0
    assert row["ci95_return_low"] < row["mean_return"] < row["ci95_return_high"]
    assert row["ci95_approach_low"] < row["mean_approach_rate"] < row["ci95_approach_high"]
