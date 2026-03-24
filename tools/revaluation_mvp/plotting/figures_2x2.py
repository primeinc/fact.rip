import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
sns.set_style("whitegrid")

def plot_2x2():
    os.makedirs("artifacts/figures", exist_ok=True)
    df = pd.read_csv("artifacts/tables/aggregated_summary.csv")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharey="row")

    for i, m in enumerate(["honest_revaluation", "fake_revaluation"]):
        for j, et in enumerate(["raw", "appraisal"]):
            sub = df[(df["mode"] == m) & (df["eval_type"] == et)]
            sns.barplot(data=sub, x="reliability", y="mean_approach_rate", hue="train_type", ax=axes[i, j])
            axes[i, j].set_title(f"{m} | eval={et}")
    plt.suptitle("2\u00d72 Matrix \u2014 Train Type \u00d7 Eval Type")
    plt.tight_layout()
    plt.savefig("artifacts/figures/2x2_matrix.png", dpi=300)
    plt.savefig("artifacts/figures/2x2_matrix.svg", bbox_inches="tight")
    print("\u2713 2\u00d72 mechanism figure saved")

if __name__ == "__main__":
    plot_2x2()
