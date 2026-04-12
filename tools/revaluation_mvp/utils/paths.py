from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
MODELS = ARTIFACTS / "models"
RUNS = ARTIFACTS / "runs"
TABLES = ARTIFACTS / "tables"
FIGURES = ARTIFACTS / "figures"
CONFIGS = ROOT / "configs"


def ensure_dirs() -> None:
    for p in [ARTIFACTS, MODELS, RUNS, TABLES, FIGURES]:
        p.mkdir(parents=True, exist_ok=True)
