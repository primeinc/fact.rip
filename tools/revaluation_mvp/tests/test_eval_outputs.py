import unittest
import pandas as pd
import glob

class TestEvalOutputs(unittest.TestCase):
    def test_metadata_columns_present(self):
        csvs = glob.glob("artifacts/tables/eval_*.csv")
        self.assertGreater(len(csvs), 0)
        for f in csvs:
            df = pd.read_csv(f)
            self.assertIn("train_type", df.columns)
            self.assertIn("eval_type", df.columns)
            self.assertIn("mode", df.columns)
            self.assertIn("reliability", df.columns)
            self.assertIn("seed", df.columns)

if __name__ == "__main__":
    unittest.main()
