import json
import numpy as np
import pytest
from pathlib import Path

from utils.metadata import run_id


class _FakePPO:
    """Minimal stub that mimics the PPO.predict interface."""

    def predict(self, obs, deterministic=True):
        return np.int64(0), None  # always move "up"


@pytest.fixture()
def isolated_runs(tmp_path, monkeypatch):
    import utils.paths as p
    import evaluation.evaluate as ev

    runs_tmp = tmp_path / "runs"
    runs_tmp.mkdir()
    monkeypatch.setattr(p, "RUNS", runs_tmp)
    monkeypatch.setattr(ev, "RUNS", runs_tmp)

    # Patch PPO.load so we don't need a real saved model
    monkeypatch.setattr(ev, "PPO", type("PPO", (), {"load": staticmethod(lambda *a, **kw: _FakePPO())}))

    return runs_tmp


def test_evaluate_run_writes_csv_and_json(isolated_runs, tmp_path):
    from evaluation.evaluate import evaluate_run

    fake_model_path = tmp_path / "fake_model.zip"
    fake_model_path.touch()

    _, summary = evaluate_run(
        model_path=fake_model_path,
        train_type="raw_only",
        eval_type="raw",
        mode="honest_revaluation",
        reliability=1.0,
        seed=0,
        num_episodes=5,
        device="cpu",
    )

    rid = run_id("raw_only", "raw", "honest_revaluation", 1.0, 0)
    episode_csv = isolated_runs / f"{rid}__episodes.csv"
    summary_json = isolated_runs / f"{rid}__summary.json"

    assert episode_csv.exists(), "Episode CSV was not written"
    assert summary_json.exists(), "Summary JSON was not written"

    # Verify CSV schema
    import pandas as pd
    df = pd.read_csv(episode_csv)
    expected_cols = {"episode", "return", "approached", "dwell_steps", "appraisal_sum",
                     "train_type", "eval_type", "mode", "reliability", "seed"}
    assert expected_cols <= set(df.columns), f"Missing CSV columns: {expected_cols - set(df.columns)}"
    assert len(df) == 5

    # Verify JSON schema
    with open(summary_json) as f:
        data = json.load(f)
    expected_keys = {"run_id", "train_type", "eval_type", "mode", "reliability", "seed",
                     "mean_approach_rate", "mean_dwell", "mean_return", "mean_appraisal_sum",
                     "episode_csv"}
    assert expected_keys <= set(data.keys()), f"Missing JSON keys: {expected_keys - set(data.keys())}"
    assert data["train_type"] == "raw_only"
    assert data["eval_type"] == "raw"
    assert data["mode"] == "honest_revaluation"
    assert data["reliability"] == 1.0
    assert data["seed"] == 0
    assert isinstance(data["mean_approach_rate"], float)
    assert isinstance(data["mean_return"], float)
