import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
sns.set_style("whitegrid")

def plot_main():
    os.makedirs("artifacts/figures", exist_ok=True)
    df = pd.read_csv("artifacts/tables/aggregated_summary.csv")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharey="row")

    for i, m in enumerate(["honest_revaluation", "fake_revaluation"]):
        sub = df[df["mode"] == m].copy()
        sns.barplot(data=sub, x="reliability", y="mean_approach_rate", hue="train_type", ax=axes[i, 0])
        sns.barplot(data=sub, x="reliability", y="mean_dwell", hue="train_type", ax=axes[i, 1])
        axes[i, 0].set_title(f"Approach Rate \u2014 {m}")
        axes[i, 1].set_title(f"Mean Dwell \u2014 {m}")

    plt.suptitle("Cue-Conditioned Appraisal vs Raw-Only (5 seeds)")
    plt.tight_layout()
    plt.savefig("artifacts/figures/main_effect.png", dpi=300)
    plt.savefig("artifacts/figures/main_effect.svg", bbox_inches="tight")
    print("\u2713 Main effect figure saved")

if __name__ == "__main__":
    plot_main()
