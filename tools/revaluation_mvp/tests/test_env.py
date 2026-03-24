import unittest
from envs.blob_revaluation_env import BlobRevaluationEnv

class TestEnv(unittest.TestCase):
    def test_observation_shape(self):
        env = BlobRevaluationEnv()
        obs, _ = env.reset()
        self.assertEqual(obs.shape, (7,))

    def test_appraisal_no_leak(self):
        env = BlobRevaluationEnv(appraisal_model=None)
        obs, _ = env.reset()
        self.assertIn("appraisal_bonus", env.step(0)[4])  # info dict

if __name__ == "__main__":
    unittest.main()
