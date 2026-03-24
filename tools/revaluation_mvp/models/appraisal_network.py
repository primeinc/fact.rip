import logging
import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path

from utils.paths import MODELS, ensure_dirs

log = logging.getLogger(__name__)


class AppraisalNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Linear(1, 1)

    def forward(self, cue: torch.Tensor):
        return self.net(cue)


def appraisal_model_path(reliability: float) -> Path:
    ensure_dirs()
    return MODELS / f"appraisal_model_rel_{reliability}.pth"


def train_appraisal_layer(
    reliability: float = 1.0,
    positive_bonus_target: float = 0.4,
    **_kwargs,
):
    ensure_dirs()
    model = AppraisalNetwork()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()

    # Mean-centered targets scaled by reliability informativeness.
    # At reliability=1.0: cue=1 → +target, cue=0 → −target  (E[bonus]=0)
    # At reliability=0.5: cue is random → bonus=0 for both   (no information)
    scaling = 2.0 * reliability - 1.0
    X = torch.tensor([[0.0], [1.0]], dtype=torch.float32)
    y = torch.tensor(
        [[-positive_bonus_target * scaling], [+positive_bonus_target * scaling]],
        dtype=torch.float32,
    )

    for epoch in range(200):
        optimizer.zero_grad()
        pred = model(X)
        loss = loss_fn(pred, y)
        loss.backward()
        optimizer.step()
        if loss.item() < 1e-8:
            break

    path = appraisal_model_path(reliability)
    torch.save(model.state_dict(), path)
    log.info(
        "AppraisalNetwork trained (rel=%.2f, scaling=%.2f) → cue0=%.4f cue1=%.4f, saved to %s",
        reliability, scaling, model(X[:1]).item(), model(X[1:]).item(), path,
    )
    return model


def load_appraisal_model(reliability: float) -> AppraisalNetwork:
    model = AppraisalNetwork()
    model.load_state_dict(torch.load(appraisal_model_path(reliability), weights_only=True))
    model.eval()
    return model


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    train_appraisal_layer(reliability=1.0)
