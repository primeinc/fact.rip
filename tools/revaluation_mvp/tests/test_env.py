import numpy as np
import torch
from envs.blob_revaluation_env import BlobRevaluationEnv


# ---------- Observation shape ----------

def test_obs_shape():
    env = BlobRevaluationEnv()
    obs, _ = env.reset(seed=0)
    assert obs.shape == (8,)


def test_obs_shape_no_cue():
    env = BlobRevaluationEnv(include_cue=False)
    obs, _ = env.reset(seed=0)
    assert obs.shape == (7,)


def test_obs_shape_homeostatic():
    env = BlobRevaluationEnv(mode="homeostatic")
    obs, _ = env.reset(seed=0)
    # 7 base + 1 cue + 1 energy = 9
    assert obs.shape == (9,)


def test_obs_shape_homeostatic_no_cue():
    env = BlobRevaluationEnv(mode="homeostatic", include_cue=False)
    obs, _ = env.reset(seed=0)
    # 7 base + 1 energy = 8
    assert obs.shape == (8,)


def test_obs_contains_visited_aversive_flag():
    env = BlobRevaluationEnv()
    obs, _ = env.reset(seed=0)
    # Index 6 is visited_aversive, should be 0.0 after reset
    assert obs[6] == 0.0


# ---------- Step / reward basics ----------

def test_step_penalty():
    env = BlobRevaluationEnv(step_penalty=-0.05)
    env.reset(seed=0)
    # Move agent to a neutral position (not aversive, not goal)
    env.agent_pos = (3, 3)
    env.goal_pos = (7, 7)
    env.aversive_pos = (0, 0)
    _, reward, _, _, _ = env.step(0)  # step up
    assert reward == -0.05


def test_goal_reward():
    env = BlobRevaluationEnv(goal_reward=2.0, step_penalty=0.0)
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.goal_pos = (0, 0)
    env.aversive_pos = (7, 7)
    _, reward, terminated, _, _ = env.step(0)  # up → goal
    assert terminated
    assert reward == 2.0


def test_aversive_cost_on_first_visit():
    env = BlobRevaluationEnv(raw_local_cost=-0.3, step_penalty=0.0)
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)
    _, reward, _, _, info = env.step(0)  # up → aversive
    assert reward == -0.3
    assert info["visited_aversive"] is True
    assert info["on_aversive"] is True


def test_aversive_no_cost_on_second_visit():
    """Critical fix: only first visit triggers cost/bonus."""
    env = BlobRevaluationEnv(raw_local_cost=-0.3, step_penalty=0.0)
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)

    # First visit
    env.step(0)  # up → aversive at (0,0)
    # Move away
    env.step(1)  # down → (1,0)
    # Second visit
    _, reward, _, _, info = env.step(0)  # up → aversive again
    assert reward == 0.0  # no cost on second visit (step_penalty=0)
    assert info["on_aversive"] is True
    assert info["visited_aversive"] is True


def test_delayed_context_reward():
    env = BlobRevaluationEnv(
        goal_reward=1.0, delayed_context_reward=1.5, step_penalty=0.0, raw_local_cost=-0.1,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (0, 1)
    env.true_benefit = True

    # Visit aversive first
    env.step(0)  # up → (0,0) aversive
    # Then go to goal
    _, reward, terminated, _, _ = env.step(3)  # right → (0,1) goal
    assert terminated
    # goal_reward + delayed_context_reward + step_penalty(0)
    assert reward == 1.0 + 1.5


def test_no_delayed_reward_without_aversive_visit():
    env = BlobRevaluationEnv(
        goal_reward=1.0, delayed_context_reward=1.5, step_penalty=0.0,
    )
    env.reset(seed=0)
    env.agent_pos = (0, 1)
    env.goal_pos = (0, 0)
    env.aversive_pos = (7, 7)
    env.true_benefit = True

    _, reward, terminated, _, _ = env.step(2)  # left → goal
    assert terminated
    assert reward == 1.0  # no delayed reward


# ---------- Boundary handling ----------

def test_wall_clipping():
    env = BlobRevaluationEnv(grid_size=4)
    env.reset(seed=0)
    env.agent_pos = (0, 0)
    env.goal_pos = (3, 3)
    env.aversive_pos = (3, 0)
    env.step(0)  # up from (0,0) → should stay at (0,0)
    assert env.agent_pos == (0, 0)
    env.step(2)  # left from (0,0) → should stay at (0,0)
    assert env.agent_pos == (0, 0)


# ---------- Truncation ----------

def test_truncation_at_max_steps():
    env = BlobRevaluationEnv(max_steps=3)
    env.reset(seed=0)
    env.goal_pos = (7, 7)
    env.aversive_pos = (7, 6)
    env.agent_pos = (0, 0)

    for i in range(2):
        _, _, _, truncated, _ = env.step(1)
        assert not truncated
    _, _, _, truncated, _ = env.step(1)
    assert truncated


# ---------- Mode logic ----------

def test_baseline_mode():
    env = BlobRevaluationEnv(mode="baseline")
    env.reset(seed=0)
    assert env.true_benefit is False
    assert env.context_cue == 0


def test_honest_revaluation_mode_reliability_1():
    env = BlobRevaluationEnv(mode="honest_revaluation", context_reliability=1.0)
    for seed in range(20):
        env.reset(seed=seed)
        assert env.context_cue == int(env.true_benefit)


def test_fake_revaluation_mode():
    env = BlobRevaluationEnv(mode="fake_revaluation", context_reliability=1.0)
    for seed in range(20):
        env.reset(seed=seed)
        assert env.true_benefit is False
        assert env.context_cue == 1


def test_invalid_mode_raises():
    env = BlobRevaluationEnv(mode="invalid")
    try:
        env.reset(seed=0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


# ---------- Visited aversive in observation ----------

def test_visited_aversive_obs_updates():
    env = BlobRevaluationEnv(step_penalty=0.0)
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)

    obs, _, _, _, _ = env.step(0)  # up → aversive
    assert obs[6] == 1.0  # visited_aversive flag now set


# ---------- Appraisal bonus ----------

def test_appraisal_bonus_applied_on_first_visit_only():
    class FixedModel:
        def __call__(self, x):
            return torch.tensor([[0.5]])

    env = BlobRevaluationEnv(
        appraisal_model=FixedModel(), raw_local_cost=-0.2, step_penalty=0.0,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)
    env.context_cue = 1

    # First visit: cost + bonus
    _, reward1, _, _, info1 = env.step(0)
    assert abs(reward1 - (-0.2 + 0.5)) < 1e-6
    assert abs(info1["appraisal_bonus"] - 0.5) < 1e-6

    # Move away and revisit
    env.step(1)
    _, reward2, _, _, info2 = env.step(0)
    assert reward2 == 0.0  # no cost or bonus on second visit
    assert info2["appraisal_bonus"] == 0.0


# ---------- Info dict completeness ----------

def test_info_dict_keys():
    env = BlobRevaluationEnv()
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)
    _, _, _, _, info = env.step(0)
    expected = {"true_benefit", "context_cue", "visited_aversive", "on_aversive",
                "raw_reward", "appraisal_bonus", "energy_level", "hazard_dwell_time",
                "died_of_starvation"}
    assert expected <= set(info.keys())


# ==========================================================================
# HOMEOSTATIC MODE
# ==========================================================================

def test_homeostatic_reward_always_zero():
    """Physics engine emits no moral truth."""
    env = BlobRevaluationEnv(mode="homeostatic")
    env.reset(seed=0)
    env.agent_pos = (3, 3)
    env.goal_pos = (7, 7)
    env.aversive_pos = (0, 0)
    _, reward, _, _, _ = env.step(1)  # neutral step
    assert reward == 0.0


def test_homeostatic_energy_drains_per_step():
    env = BlobRevaluationEnv(mode="homeostatic", step_drain=0.1, max_energy=1.0)
    env.reset(seed=0)
    env.agent_pos = (3, 3)
    env.goal_pos = (7, 7)
    env.aversive_pos = (0, 0)
    _, _, _, _, info = env.step(1)
    assert abs(info["energy_level"] - 0.9) < 1e-6


def test_homeostatic_hazard_drains_energy():
    env = BlobRevaluationEnv(
        mode="homeostatic", step_drain=0.0, hazard_drain=0.3, max_energy=1.0,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)
    _, _, _, _, info = env.step(0)  # up → hazard
    assert abs(info["energy_level"] - 0.7) < 1e-6
    assert info["hazard_dwell_time"] == 1


def test_homeostatic_hazard_drains_every_step():
    """Unlike reward-surface mode, hazard drains energy on EVERY visit."""
    env = BlobRevaluationEnv(
        mode="homeostatic", step_drain=0.0, hazard_drain=0.2, max_energy=1.0,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)
    env.step(0)  # first visit → energy 0.8
    env.step(1)  # move away
    _, _, _, _, info = env.step(0)  # second visit → energy 0.6
    assert abs(info["energy_level"] - 0.6) < 1e-6
    assert info["hazard_dwell_time"] == 2


def test_homeostatic_goal_charges_energy():
    env = BlobRevaluationEnv(
        mode="homeostatic", step_drain=0.5, charge_amount=0.8, max_energy=1.0,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.goal_pos = (0, 0)
    env.aversive_pos = (7, 7)
    _, _, terminated, _, info = env.step(0)  # up → goal
    assert terminated
    # Energy: 1.0 - 0.5 (drain) + 0.8 (charge) = 1.0 (capped at max)
    assert abs(info["energy_level"] - 1.0) < 1e-6


def test_homeostatic_energy_capped_at_max():
    env = BlobRevaluationEnv(
        mode="homeostatic", step_drain=0.0, charge_amount=5.0, max_energy=1.0,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.goal_pos = (0, 0)
    env.aversive_pos = (7, 7)
    _, _, _, _, info = env.step(0)
    assert info["energy_level"] <= 1.0


def test_homeostatic_death_on_zero_energy():
    env = BlobRevaluationEnv(
        mode="homeostatic", step_drain=0.0, hazard_drain=1.0, max_energy=1.0,
    )
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.aversive_pos = (0, 0)
    env.goal_pos = (7, 7)
    _, _, terminated, _, info = env.step(0)  # drain all energy
    assert terminated
    assert info["died_of_starvation"] is True
    assert info["energy_level"] == 0.0


def test_homeostatic_obs_includes_energy():
    env = BlobRevaluationEnv(mode="homeostatic", max_energy=1.0, step_drain=0.1)
    env.reset(seed=0)
    env.agent_pos = (3, 3)
    env.goal_pos = (7, 7)
    env.aversive_pos = (0, 0)
    obs, _, _, _, _ = env.step(1)
    # Last element should be energy_level
    assert abs(obs[-1] - 0.9) < 1e-6


def test_homeostatic_context_cue_generated():
    """Homeostatic mode uses honest_revaluation-style context logic."""
    env = BlobRevaluationEnv(mode="homeostatic", context_reliability=1.0)
    for seed in range(20):
        env.reset(seed=seed)
        assert env.context_cue == int(env.true_benefit)


def test_homeostatic_reward_zero_even_at_goal():
    env = BlobRevaluationEnv(mode="homeostatic", goal_reward=99.0)
    env.reset(seed=0)
    env.agent_pos = (1, 0)
    env.goal_pos = (0, 0)
    env.aversive_pos = (7, 7)
    _, reward, _, _, _ = env.step(0)
    assert reward == 0.0  # goal_reward ignored in homeostatic mode
