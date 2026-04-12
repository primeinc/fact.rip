import gymnasium as gym


class HomeostaticIntrinsicDriveWrapper(gym.Wrapper):
    """
    Agent-side valuation module.

    Intercepts the physics-only transitions from a ``mode="homeostatic"``
    environment and computes internal valence based on energy-state deviation
    from the homeostatic set-point.

    The wrapped env must expose ``energy_level`` as the *last* element of its
    observation vector (guaranteed by ``BlobRevaluationEnv`` in homeostatic mode).
    """

    def __init__(self, env, optimal_energy: float = 1.0, death_penalty: float = 5.0):
        super().__init__(env)
        self.optimal_energy = optimal_energy
        self.death_penalty = death_penalty

    def step(self, action):
        obs, _env_reward, terminated, truncated, info = self.env.step(action)

        # Internal physiological state (last element of obs in homeostatic mode)
        current_energy = obs[-1]

        # First principle: minimise deviation from homeostatic optimum
        intrinsic_reward = -((self.optimal_energy - current_energy) ** 2)

        # Acute negative valence upon catastrophic failure
        if info["died_of_starvation"]:
            intrinsic_reward -= self.death_penalty

        return obs, intrinsic_reward, terminated, truncated, info
