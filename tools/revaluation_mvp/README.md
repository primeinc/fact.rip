# SSOT MVP — Cue-Conditioned Reward-Shaping for Contextual Revaluation

## Reproduction (one command)
```bash
cd tools/revaluation_mvp
uv sync
uv run python reproduce.py
```

## Short Conclusion (from aggregated seed-level results)

A learned appraisal bonus based only on an observable context cue produces higher approach rates and dwell times on the aversive tile compared to raw-cost-only (cue-visible, no-bonus) training in honest_revaluation mode. The effect is cue-dependent: it is substantially reduced in fake_revaluation mode and scales with cue reliability. The 2×2 matrix shows the difference lives primarily in the trained policy. This demonstrates cue-conditioned reward revaluation alters behavior beyond raw cost alone, but does not spontaneously reconstruct valence from first principles.

This is the smallest real publishable object that satisfies the full checklist. All claims map to explicit artifacts, configs, and seed-level statistics.
