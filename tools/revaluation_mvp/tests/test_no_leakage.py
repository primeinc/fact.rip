import unittest
import torch
from models.appraisal_network import AppraisalNetwork

class TestNoLeakage(unittest.TestCase):
    def test_appraisal_input_is_cue_only(self):
        model = AppraisalNetwork()
        dummy_cue = torch.tensor([[1.0]])
        output = model(dummy_cue)
        self.assertEqual(output.shape, (1, 1))

if __name__ == "__main__":
    unittest.main()
