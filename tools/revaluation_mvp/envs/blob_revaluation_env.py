import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
from gymnasium import spaces


class BlobRevaluationEnv(gym.Env):
    """
    Gridworld with two regimes:

    **Reward-surface** (baseline / honest_revaluation / fake_revaluation):
        Traditional MDP.  Aversive tile cost + appraisal bonus on *first visit
        only* (oracle fix), goal reward, delayed context reward.

    **Physics-only** (homeostatic):
        Returns reward ≡ 0.  Only updates internal energy: step drain, hazard
        drain every step on the aversive tile, charge at goal.  The wrapper
        (HomeostaticIntrinsicDriveWrapper) is responsible for generating
        intrinsic valence from the physiological state.
    """

    metadata = {"render_modes": []}

    def __init__(
        self,
        grid_size: int = 8,
        raw_local_cost: float = -0.2,
        goal_reward: float = 1.0,
        delayed_context_reward: float = 1.0,
        context_reliability: float = 1.0,
        mode: str = "honest_revaluation",
        max_steps: int = 50,
        step_penalty: float = -0.01,
        appraisal_model: nn.Module | None = None,
        include_cue: bool = True,
        render_mode: str | None = None,
        # Homeostatic physics parameters
        max_energy: float = 1.0,
        step_drain: float = 0.02,
        hazard_drain: float = 0.25,
        charge_amount: float = 1.0,
    ):
        super().__init__()
        self.render_mode = render_mode
        self.grid_size = grid_size
        self.raw_local_cost = raw_local_cost
        self.goal_reward = goal_reward
        self.delayed_context_reward = delayed_context_reward
        self.context_reliability = context_reliability
        self.mode = mode
        self.max_steps = max_steps
        self.step_penalty = step_penalty
        self.appraisal_model = appraisal_model
        self.include_cue = include_cue

        # Homeostatic internal state params
        self.max_energy = max_energy
        self.step_drain = step_drain
        self.hazard_drain = hazard_drain
        self.charge_amount = charge_amount

        self.action_space = spaces.Discrete(4)

        # Obs layout: [agent_xy, goal_xy, aversive_xy, visited_aversive, (cue), (energy)]
        # Base = 7 (6 positions + visited_aversive flag)
        obs_dim = 7
        if include_cue:
            obs_dim += 1
        if mode == "homeostatic":
            obs_dim += 1  # energy_level
        low = np.zeros(obs_dim, dtype=np.float32)
        high = np.ones(obs_dim, dtype=np.float32)
        if mode == "homeostatic":
            high[-1] = float(self.max_energy)
        self.observation_space = spaces.Box(
            low=low, high=high, dtype=np.float32,
        )

    def _get_obs(self) -> np.ndarray:
        norm = float(self.grid_size - 1) if self.grid_size > 1 else 1.0
        base = [
            self.agent_pos[0] / norm,
            self.agent_pos[1] / norm,
            self.goal_pos[0] / norm,
            self.goal_pos[1] / norm,
            self.aversive_pos[0] / norm,
            self.aversive_pos[1] / norm,
            float(self.visited_aversive),
        ]
        if self.include_cue:
            base.append(float(self.context_cue))
        if self.mode == "homeostatic":
            base.append(float(self.energy_level))
        return np.array(base, dtype=np.float32)

    # ------------------------------------------------------------------
    # Reset
    # ------------------------------------------------------------------

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        n_cells = self.grid_size ** 2
        pos_indices = self.np_random.choice(n_cells, 3, replace=False)

        def idx_to_pos(idx):
            return (idx // self.grid_size, idx % self.grid_size)

        self.agent_pos = idx_to_pos(pos_indices[0])
        self.goal_pos = idx_to_pos(pos_indices[1])
        self.aversive_pos = idx_to_pos(pos_indices[2])
        self.visited_aversive = False
        self.current_step = 0
        self.energy_level = self.max_energy
        self.hazard_dwell_time = 0

        if self.mode == "baseline":
            self.true_benefit = False
            self.context_cue = 0
        elif self.mode in ("honest_revaluation", "homeostatic"):
            self.true_benefit = self.np_random.random() < 0.5
            self.context_cue = (
                int(self.true_benefit)
                if self.np_random.random() < self.context_reliability
                else int(not self.true_benefit)
            )
        elif self.mode == "fake_revaluation":
            self.true_benefit = False
            self.context_cue = (
                1 if self.np_random.random() < self.context_reliability else 0
            )
        else:
            raise ValueError(f"Unknown mode: {self.mode}")

        return self._get_obs(), {}

    # ------------------------------------------------------------------
    # Step
    # ------------------------------------------------------------------

    def step(self, action):
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dx, dy = deltas[action]
        new_x = self.agent_pos[0] + dx
        new_y = self.agent_pos[1] + dy
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
            self.agent_pos = (new_x, new_y)

        reward = 0.0
        raw_reward = 0.0
        appraisal_bonus = 0.0
        on_aversive = self.agent_pos == self.aversive_pos
        terminated = False
        died_of_starvation = False

        if self.mode == "homeostatic":
            # ----------------------------------------------------------
            # PHYSICS-ONLY regime: reward ≡ 0, update energy
            # ----------------------------------------------------------
            self.energy_level -= self.step_drain

            if on_aversive:
                self.energy_level -= self.hazard_drain
                self.hazard_dwell_time += 1
                self.visited_aversive = True

            if self.agent_pos == self.goal_pos:
                self.energy_level = min(
                    self.max_energy, self.energy_level + self.charge_amount,
                )
                terminated = True

            if self.energy_level <= 0:
                self.energy_level = 0.0
                died_of_starvation = True
                terminated = True

            reward = 0.0  # physics engine emits no moral truth

        else:
            # ----------------------------------------------------------
            # REWARD-SURFACE regime (RAW / APP)
            # ----------------------------------------------------------
            reward = self.step_penalty

            # First-visit-only guard (oracle fix: prevents tile-camping)
            if on_aversive and not self.visited_aversive:
                raw_reward = self.raw_local_cost
                if self.appraisal_model is not None:
                    inp = torch.tensor(
                        [[float(self.context_cue)]], dtype=torch.float32,
                    )
                    with torch.no_grad():
                        appraisal_bonus = float(
                            self.appraisal_model(inp).item()
                        )
                reward += raw_reward + appraisal_bonus
                self.visited_aversive = True

            if self.agent_pos == self.goal_pos:
                reward += self.goal_reward
                if self.visited_aversive and self.true_benefit:
                    reward += self.delayed_context_reward
                terminated = True

        self.current_step += 1
        truncated = self.current_step >= self.max_steps

        obs = self._get_obs()
        info = {
            "true_benefit": self.true_benefit,
            "context_cue": self.context_cue,
            "visited_aversive": self.visited_aversive,
            "on_aversive": on_aversive,
            "raw_reward": raw_reward,
            "appraisal_bonus": appraisal_bonus,
            "energy_level": self.energy_level,
            "hazard_dwell_time": self.hazard_dwell_time,
            "died_of_starvation": died_of_starvation,
        }
        return obs, reward, terminated, truncated, info
