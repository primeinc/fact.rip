import torch
import torch.nn as nn
import torch.optim as optim

class AppraisalNetwork(nn.Module):
    """Learned appraisal proxy — cue ONLY"""
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(1, 32), nn.ReLU(), nn.Linear(32, 1))

    def forward(self, cue: torch.Tensor):
        return self.net(cue)


def train_appraisal_layer(num_samples: int = 10000, epochs: int = 50, lr: float = 0.01):
    model = AppraisalNetwork()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()

    from envs.blob_revaluation_env import BlobRevaluationEnv
    env = BlobRevaluationEnv(mode="honest_revaluation", context_reliability=1.0)
    X, y = [], []
    for _ in range(num_samples):
        obs, _ = env.reset()
        cue = obs[-1]
        target = 0.4 if cue == 1.0 else 0.0
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
            print(f"Appraisal epoch {epoch:3d} | loss = {loss.item():.5f}")

    torch.save(model.state_dict(), "artifacts/models/appraisal_model.pth")
    print("\u2713 AppraisalNetwork trained (cue-only)")
    return model


if __name__ == "__main__":
    train_appraisal_layer()
