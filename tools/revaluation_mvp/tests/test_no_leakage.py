import torch

from envs.blob_revaluation_env import BlobRevaluationEnv


def test_appraisal_uses_only_cue():
    """In fake_revaluation mode the appraisal model receives context_cue (=1),
    not true_benefit (=0), as its input — a behavioral no-leakage check."""
    call_args = []

    class SpyModel:
        def __call__(self, x: torch.Tensor):
            call_args.append(x.detach().clone())
            return torch.tensor([[0.0]])

    spy = SpyModel()
    env = BlobRevaluationEnv(
        appraisal_model=spy,
        mode="fake_revaluation",  # true_benefit=False (0), context_cue=1 at rel=1.0
        context_reliability=1.0,
    )
    env.reset(seed=0)

    # Place agent one step above aversive_pos so action 0 (up: -1,0) lands on it.
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)  # keep goal away so we don't terminate early

    env.step(0)  # move up → lands on aversive_pos, triggering appraisal

    assert len(call_args) == 1, "Appraisal model should have been called exactly once"
    input_val = call_args[0].item()

    # In fake_revaluation with reliability=1.0: context_cue=1, true_benefit=False(=0.0)
    assert input_val == float(env.context_cue), "Model must be called with context_cue"
    assert input_val != float(env.true_benefit), "Model must NOT be called with true_benefit"


def test_appraisal_not_called_on_second_visit():
    """Appraisal model should only be invoked on first visit to aversive tile."""
    call_count = 0

    class CountingModel:
        def __call__(self, x: torch.Tensor):
            nonlocal call_count
            call_count += 1
            return torch.tensor([[0.1]])

    env = BlobRevaluationEnv(
        appraisal_model=CountingModel(),
        mode="honest_revaluation",
        context_reliability=1.0,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)

    env.step(0)  # first visit → model called
    assert call_count == 1

    env.step(1)  # move away
    env.step(0)  # second visit → model NOT called
    assert call_count == 1, "Appraisal model must not be called on revisits"
