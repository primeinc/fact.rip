from envs.blob_revaluation_env import BlobRevaluationEnv
from training.homeostatic_wrapper import HomeostaticIntrinsicDriveWrapper


def test_wrapper_generates_intrinsic_reward():
    raw_env = BlobRevaluationEnv(mode="homeostatic", step_drain=0.1, max_energy=1.0)
    env = HomeostaticIntrinsicDriveWrapper(raw_env, optimal_energy=1.0)
    env.reset(seed=0)
    env.unwrapped.agent_pos = (3, 3)
    env.unwrapped.goal_pos = (7, 7)
    env.unwrapped.aversive_pos = (0, 0)

    obs, reward, _, _, _ = env.step(1)
    # Energy after step: 1.0 - 0.1 = 0.9
    # Intrinsic: -(1.0 - 0.9)^2 = -0.01
    assert abs(reward - (-0.01)) < 1e-6


def test_wrapper_death_penalty():
    raw_env = BlobRevaluationEnv(
        mode="homeostatic", step_drain=0.0, hazard_drain=1.0, max_energy=1.0,
    )
    env = HomeostaticIntrinsicDriveWrapper(raw_env, optimal_energy=1.0, death_penalty=5.0)
    env.reset(seed=0)
    env.unwrapped.agent_pos = (1, 0)
    env.unwrapped.aversive_pos = (0, 0)
    env.unwrapped.goal_pos = (7, 7)

    _, reward, terminated, _, info = env.step(0)
    assert terminated
    assert info["died_of_starvation"] is True
    # Energy = 0 → deviation = 1.0 → intrinsic = -(1)^2 - 5.0 = -6.0
    assert abs(reward - (-6.0)) < 1e-6


def test_wrapper_passes_through_info():
    raw_env = BlobRevaluationEnv(mode="homeostatic")
    env = HomeostaticIntrinsicDriveWrapper(raw_env)
    env.reset(seed=0)
    env.unwrapped.agent_pos = (3, 3)
    env.unwrapped.goal_pos = (7, 7)
    env.unwrapped.aversive_pos = (0, 0)
    _, _, _, _, info = env.step(1)
    assert "energy_level" in info
    assert "died_of_starvation" in info
    assert "visited_aversive" in info


def test_wrapper_optimal_energy_gives_zero_intrinsic():
    raw_env = BlobRevaluationEnv(mode="homeostatic", step_drain=0.0, max_energy=1.0)
    env = HomeostaticIntrinsicDriveWrapper(raw_env, optimal_energy=1.0)
    env.reset(seed=0)
    env.unwrapped.agent_pos = (3, 3)
    env.unwrapped.goal_pos = (7, 7)
    env.unwrapped.aversive_pos = (0, 0)
    _, reward, _, _, _ = env.step(1)
    # No drain → energy stays at 1.0 → deviation = 0 → reward = 0
    assert abs(reward) < 1e-6
