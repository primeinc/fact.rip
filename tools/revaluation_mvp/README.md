# Revaluation MVP

A reproducible gridworld experiment testing whether a learned cue-conditioned shaping module
changes behavior around a locally aversive state under honest vs deceptive cue conditions.

## Reproduction

```bash
cd tools/revaluation_mvp
uv sync
uv run python run_experiment.py
```

Artifacts are written under `artifacts/`:
- `artifacts/models/`
- `artifacts/runs/`
- `artifacts/tables/`
- `artifacts/figures/`

## Core claim

This repo tests whether an observable context cue, implemented through a learned shaping module,
changes approach behavior toward a locally aversive state under varying cue reliability and
deceptive cue conditions.

## Notes

- The appraisal module is not emergent valence learning from first principles.
- It is a learned implementation of a hand-specified cue-conditioned shaping rule.
- Metadata is stored explicitly in run artifacts, never inferred from filenames.
