import gymnasium as gym
from gymnasium import spaces
import numpy as np
import torch
import torch.nn as nn

class BlobRevaluationEnv(gym.Env):
    """
    SSOT MVP — final publishable version
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
    ):
        super().__init__()
        self.grid_size = grid_size
        self.raw_local_cost = raw_local_cost
        self.goal_reward = goal_reward
        self.delayed_context_reward = delayed_context_reward
        self.context_reliability = context_reliability
        self.mode = mode
        self.max_steps = max_steps
        self.step_penalty = step_penalty
        self.appraisal_model = appraisal_model

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(7,), dtype=np.float32)

    def _get_obs(self) -> np.ndarray:
        norm = float(self.grid_size - 1) if self.grid_size > 1 else 1.0
        return np.array([
            self.agent_pos[0] / norm, self.agent_pos[1] / norm,
            self.goal_pos[0] / norm, self.goal_pos[1] / norm,
            self.aversive_pos[0] / norm, self.aversive_pos[1] / norm,
            float(self.context_cue)
        ], dtype=np.float32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        n_cells = self.grid_size**2
        pos_indices = self.np_random.choice(n_cells, 3, replace=False)
        def idx_to_pos(idx): return (idx // self.grid_size, idx % self.grid_size)
        self.agent_pos = idx_to_pos(pos_indices[0])
        self.goal_pos = idx_to_pos(pos_indices[1])
        self.aversive_pos = idx_to_pos(pos_indices[2])
        self.visited_aversive = False
        self.current_step = 0

        if self.mode == "baseline":
            self.true_benefit = False
            self.context_cue = 0
        elif self.mode == "honest_revaluation":
            self.true_benefit = self.np_random.random() < 0.5
            self.context_cue = int(self.true_benefit) if self.np_random.random() < self.context_reliability else int(not self.true_benefit)
        elif self.mode == "fake_revaluation":
            self.true_benefit = False
            self.context_cue = 1 if self.np_random.random() < self.context_reliability else 0
        else:
            raise ValueError(f"Unknown mode: {self.mode}")

        return self._get_obs(), {}

    def step(self, action):
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dx, dy = deltas[action]
        new_x = self.agent_pos[0] + dx
        new_y = self.agent_pos[1] + dy
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
            self.agent_pos = (new_x, new_y)

        reward = self.step_penalty
        raw_reward = 0.0
        appraisal_bonus = 0.0

        if self.agent_pos == self.aversive_pos:
            raw_reward = self.raw_local_cost
            if self.appraisal_model is not None:
                input_tensor = torch.tensor([[float(self.context_cue)]], dtype=torch.float32)
                with torch.no_grad():
                    appraisal_bonus = self.appraisal_model(input_tensor).item()
            reward += raw_reward + appraisal_bonus
            self.visited_aversive = True

        terminated = False
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
            "raw_reward": raw_reward,
            "appraisal_bonus": appraisal_bonus,
        }
        return obs, reward, terminated, truncated, info
