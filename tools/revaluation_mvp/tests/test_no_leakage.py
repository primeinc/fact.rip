import inspect
from models.appraisal_network import AppraisalNetwork
from envs.blob_revaluation_env import BlobRevaluationEnv


def test_appraisal_uses_only_cue():
    src = inspect.getsource(BlobRevaluationEnv.step)
    assert "self.context_cue" in src
    assert "self.true_benefit" not in src.split("appraisal_bonus")[0]
