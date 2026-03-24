import unittest
import pandas as pd

class TestAggregation(unittest.TestCase):
    def test_aggregated_file_exists(self):
        df = pd.read_csv("artifacts/tables/aggregated_summary.csv")
        self.assertIn("mean_approach_rate", df.columns)
        self.assertIn("ci95_approach_low", df.columns)

if __name__ == "__main__":
    unittest.main()
