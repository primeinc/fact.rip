import logging
import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path

from envs.blob_revaluation_env import BlobRevaluationEnv
from utils.paths import MODELS, ensure_dirs

log = logging.getLogger(__name__)


class AppraisalNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
        )

    def forward(self, cue: torch.Tensor):
        return self.net(cue)


def appraisal_model_path() -> Path:
    ensure_dirs()
    return MODELS / "appraisal_model.pth"


def train_appraisal_layer(
    num_samples: int = 10000,
    epochs: int = 50,
    lr: float = 0.01,
    positive_bonus_target: float = 0.4,
):
    ensure_dirs()
    model = AppraisalNetwork()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()

    env = BlobRevaluationEnv(mode="honest_revaluation", context_reliability=1.0)
    X, y = [], []
    for _ in range(num_samples):
        obs, _ = env.reset()
        cue = obs[-1]
        target = positive_bonus_target if cue == 1.0 else 0.0
        X.append([cue])
        y.append(target)

    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32).unsqueeze(1)

    for epoch in range(epochs):
        optimizer.zero_grad()
        pred = model(X)
        loss = loss_fn(pred, y)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            log.info("Appraisal epoch %3d | loss = %.5f", epoch, loss.item())

    path = appraisal_model_path()
    torch.save(model.state_dict(), path)
    log.info("AppraisalNetwork trained and saved to %s", path)
    return model


def load_appraisal_model() -> AppraisalNetwork:
    model = AppraisalNetwork()
    model.load_state_dict(torch.load(appraisal_model_path(), weights_only=True))
    model.eval()
    return model


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    train_appraisal_layer()
