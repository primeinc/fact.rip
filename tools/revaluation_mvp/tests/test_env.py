from envs.blob_revaluation_env import BlobRevaluationEnv


def test_obs_shape():
    env = BlobRevaluationEnv()
    obs, _ = env.reset(seed=0)
    assert obs.shape == (7,)


def test_obs_shape_no_cue():
    env = BlobRevaluationEnv(include_cue=False)
    obs, _ = env.reset(seed=0)
    assert obs.shape == (6,)
