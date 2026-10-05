"""
High-Resolution Banking Risk Visualization Suite
Generates publication-quality charts using Matplotlib & Seaborn:
1. Credit Scorecard Distribution & Cut-off Threshold
2. Kolmogorov-Smirnov (K-S) Cumulative Divergence Plot
3. ROC-AUC & Lorenz Curve (Gini Discrimination)
4. Vintage Delinquency Curves by Origination Cohort (Months on Book)
5. Delinquency Roll-Rate / Transition Probability Heatmap
6. IFRS 9 Staged ECL & Risk-Weighted Asset Allocation
7. Macroeconomic Stress Testing Capital Impact
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set professional aesthetics
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#CBD5E1"
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["grid.color"] = "#E2E8F0"
plt.rcParams["grid.linestyle"] = "--"

FIGURES_DIR = "reports/figures"
os.makedirs(FIGURES_DIR, exist_ok=True)

NAVY = "#0F172A"
BLUE = "#1E40AF"
CYAN = "#0EA5E9"
RED = "#DC2626"
GREEN = "#16A34A"
ORANGE = "#EA580C"
PURPLE = "#7C3AED"

def plot_score_distribution_and_cutoff(
    scores: np.ndarray, 
    defaults: np.ndarray, 
    cutoff: int = 611, 
    save_path: str = f"{FIGURES_DIR}/01_score_distribution_and_cutoff.png"
):
    """Plots credit score histogram split by Good/Bad borrowers with policy cut-off."""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    sns.histplot(
        x=scores[defaults == 0], 
        bins=35, 
        color=BLUE, 
        alpha=0.65, 
        label="Non-Default (Good Borrowers)", 
        stat="density",
        ax=ax
    )
    sns.histplot(
        x=scores[defaults == 1], 
        bins=35, 
        color=RED, 
        alpha=0.75, 
        label="Defaulted (Bad Borrowers)", 
        stat="density",
        ax=ax
    )
    
    ax.axvline(cutoff, color=NAVY, linestyle="--", linewidth=2.2, label=f"Optimal Risk Cut-off (Score = {cutoff})")
    
    # Calculate bad rate below vs above cutoff
    below_bad = defaults[scores < cutoff].mean() * 100
    above_bad = defaults[scores >= cutoff].mean() * 100
    
    ax.text(cutoff - 15, ax.get_ylim()[1]*0.80, f"Decline Zone\n(Bad Rate: {below_bad:.1f}%)", 
            horizontalalignment="right", color=RED, weight="bold", fontsize=10,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#FEE2E2", edgecolor=RED, alpha=0.9))
    
    ax.text(cutoff + 15, ax.get_ylim()[1]*0.80, f"Approval Zone\n(Bad Rate: {above_bad:.1f}%)", 
            horizontalalignment="left", color=GREEN, weight="bold", fontsize=10,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#DCFCE7", edgecolor=GREEN, alpha=0.9))

    ax.set_title("Credit Score Distribution & Underwriting Cut-off Policy", fontsize=14, weight="bold", color=NAVY, pad=15)
    ax.set_xlabel("Calibrated Credit Score (300 - 850 Range)", fontsize=11, weight="bold")
    ax.set_ylabel("Borrower Density", fontsize=11, weight="bold")
    ax.legend(frameon=True, facecolor="white", loc="upper right")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[Chart Generated] {save_path}")

def plot_ks_statistic(
    y_true: np.ndarray, 
    y_pred_pd: np.ndarray, 
    scores: np.ndarray, 
    save_path: str = f"{FIGURES_DIR}/02_ks_statistic_divergence.png"
):
    """Plots the Kolmogorov-Smirnov cumulative separation curve."""
    df_eval = pd.DataFrame({"y": y_true, "pd": y_pred_pd, "score": scores}).sort_values("pd", ascending=True).reset_index(drop=True)
    
    n_bad = (df_eval["y"] == 1).sum()
    n_good = (df_eval["y"] == 0).sum()
    
    df_eval["cum_bad"] = (df_eval["y"] == 1).cumsum() / n_bad
    df_eval["cum_good"] = (df_eval["y"] == 0).cumsum() / n_good
    df_eval["ks_diff"] = np.abs(df_eval["cum_good"] - df_eval["cum_bad"])
    
    ks_max = df_eval["ks_diff"].max()
    ks_idx = df_eval["ks_diff"].idxmax()
    ks_pct = ks_idx / len(df_eval) * 100
    
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    population_pct = np.linspace(0, 100, len(df_eval))
    ax.plot(population_pct, df_eval["cum_good"] * 100, color=GREEN, linewidth=2.5, label="Cumulative Non-Defaults (Goods)")
    ax.plot(population_pct, df_eval["cum_bad"] * 100, color=RED, linewidth=2.5, label="Cumulative Defaults (Bads)")
    
    # Draw K-S distance line
    ax.vlines(
        x=ks_pct, 
        ymin=df_eval.loc[ks_idx, "cum_bad"] * 100, 
        ymax=df_eval.loc[ks_idx, "cum_good"] * 100, 
        color=NAVY, linestyle="-.", linewidth=2.5,
        label=f"K-S Statistic: {ks_max*100:.1f}% (Optimal Split)"
    )
    
    ax.annotate(
        f"K-S = {ks_max*100:.1f}%\nScore = {df_eval.loc[ks_idx, 'score']}",
        xy=(ks_pct, (df_eval.loc[ks_idx, 'cum_good'] + df_eval.loc[ks_idx, 'cum_bad']) / 2 * 100),
        xytext=(ks_pct + 8, 50),
        arrowprops=dict(facecolor=NAVY, shrink=0.05, width=1.5, headwidth=7),
        fontsize=10, weight="bold", color=NAVY,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#F1F5F9", edgecolor=NAVY)
    )

    ax.set_title("Kolmogorov-Smirnov (K-S) Cumulative Separation Chart", fontsize=14, weight="bold", color=NAVY, pad=15)
    ax.set_xlabel("Population Percentile Ranked by Risk (Low to High)", fontsize=11, weight="bold")
    ax.set_ylabel("Cumulative Percentage (%)", fontsize=11, weight="bold")
    ax.legend(frameon=True, facecolor="white", loc="lower right")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[Chart Generated] {save_path}")

def plot_roc_curve(
    y_true: np.ndarray, 
    y_pred_pd: np.ndarray, 
    save_path: str = f"{FIGURES_DIR}/03_roc_auc_curve.png"
):
    """Plots Receiver Operating Characteristic (ROC) and calculates Gini."""
    df_roc = pd.DataFrame({"y": y_true, "pd": y_pred_pd}).sort_values("pd", ascending=False).reset_index(drop=True)
    n_bad = (df_roc["y"] == 1).sum()
    n_good = (df_roc["y"] == 0).sum()
    
    df_roc["tpr"] = (df_roc["y"] == 1).cumsum() / n_bad
    df_roc["fpr"] = (df_roc["y"] == 0).cumsum() / n_good
    
    trapz_func = getattr(np, "trapezoid", np.trapz)
    auc = trapz_func(df_roc["tpr"], df_roc["fpr"])
    gini = (2.0 * auc) - 1.0
    
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    ax.plot(df_roc["fpr"], df_roc["tpr"], color=BLUE, linewidth=2.8, label=f"Scorecard ROC (AUC = {auc:.3f} | Gini = {gini:.3f})")
    ax.plot([0, 1], [0, 1], color="#94A3B8", linestyle="--", linewidth=1.5, label="Random Guess (AUC = 0.50)")
    
    ax.fill_between(df_roc["fpr"], df_roc["tpr"], alpha=0.15, color=BLUE)
    
    ax.set_title("ROC Curve & Gini Discrimination Index", fontsize=14, weight="bold", color=NAVY, pad=15)
    ax.set_xlabel("False Positive Rate (1 - Specificity)", fontsize=11, weight="bold")
    ax.set_ylabel("True Positive Rate (Sensitivity)", fontsize=11, weight="bold")
    ax.legend(frameon=True, facecolor="white", loc="lower right")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[Chart Generated] {save_path}")

def plot_vintage_analysis(
    df: pd.DataFrame, 
    save_path: str = f"{FIGURES_DIR}/04_vintage_delinquency_curves.png"
):
    """Plots vintage delinquency aging curves across origination cohorts."""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    # Bucket months on book into cohorts
    cohorts = [2020, 2021, 2022, 2023]
    palette = [NAVY, BLUE, CYAN, ORANGE]
    
    for yr, col in zip(cohorts, palette):
        sub = df[df["origination_year"] == yr].copy()
        if len(sub) == 0:
            continue
        # Calculate cumulative default rate over months on book
        max_mob = int(sub["months_on_book"].max())
        mobs = np.arange(3, min(max_mob, 48), 3)
        cum_defaults = []
        for m in mobs:
            # Fraction defaulted within m months
            sub_m = sub[sub["months_on_book"] >= m]
            if len(sub_m) > 0:
                cum_defaults.append(sub_m["default_flag"].mean() * 100)
            else:
                cum_defaults.append(np.nan)
                
        ax.plot(mobs, cum_defaults, marker="o", markersize=5, linewidth=2.2, color=col, label=f"Vintage {yr} Cohort")
        
    ax.set_title("Vintage Analysis: Cumulative Default Rate by Origination Cohort", fontsize=14, weight="bold", color=NAVY, pad=15)
    ax.set_xlabel("Months on Book (MOB)", fontsize=11, weight="bold")
    ax.set_ylabel("Cumulative Default Rate (%)", fontsize=11, weight="bold")
    ax.legend(frameon=True, facecolor="white", loc="upper left")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[Chart Generated] {save_path}")

def plot_delinquency_roll_rates(save_path: str = f"{FIGURES_DIR}/05_delinquency_transition_heatmap.png"):
    """Generates an empirical roll-rate transition matrix heatmap across DPD buckets."""
    states = ["Current (0 DPD)", "30 DPD (1-29)", "60 DPD (30-59)", "90 DPD (60-89)", "Default (90+)"]
    
    # Industry benchmark 30-day transition matrix
    matrix = np.array([
        [0.912, 0.071, 0.012, 0.003, 0.002],
        [0.485, 0.310, 0.162, 0.031, 0.012],
        [0.180, 0.145, 0.420, 0.210, 0.045],
        [0.065, 0.040, 0.125, 0.450, 0.320],
        [0.010, 0.005, 0.015, 0.030, 0.940]
    ]) * 100.0
    
    fig, ax = plt.subplots(figsize=(9, 7), dpi=300)
    sns.heatmap(
        matrix, 
        annot=True, 
        fmt=".1f", 
        cmap="Blues", 
        xticklabels=states, 
        yticklabels=states, 
        cbar_kws={"label": "Transition Probability (%)"},
        ax=ax,
        annot_kws={"weight": "bold", "size": 10}
    )
    
    ax.set_title("30-Day Delinquency Roll-Rate Transition Matrix (%)", fontsize=14, weight="bold", color=NAVY, pad=15)
    ax.set_xlabel("Destination Bucket (Month t+1)", fontsize=11, weight="bold")
    ax.set_ylabel("Origination Bucket (Month t)", fontsize=11, weight="bold")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[Chart Generated] {save_path}")

def plot_stress_test_comparison(
    summary_df: pd.DataFrame, 
    save_path: str = f"{FIGURES_DIR}/06_macro_stress_testing_impact.png"
):
    """Visualizes portfolio Expected Loss and Capital Adequacy under stress scenarios."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
    
    scenarios = summary_df["Scenario"]
    colors = [GREEN, ORANGE, RED]
    
    # 1. Expected Loss
    bars1 = ax1.bar(scenarios, summary_df["Expected Loss ($M)"], color=colors, width=0.55, edgecolor=NAVY)
    ax1.set_title("Expected Loss (ECL) by Macro Scenario ($ Millions)", fontsize=12, weight="bold", color=NAVY)
    ax1.set_ylabel("Expected Loss ($M)", fontsize=11, weight="bold")
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 3.0, f"${yval:.1f}M", ha="center", va="bottom", weight="bold")
        
    # 2. Regulatory Capital Requirement
    bars2 = ax2.bar(scenarios, summary_df["Required Regulatory Capital ($M)"], color=[BLUE, PURPLE, NAVY], width=0.55, edgecolor=NAVY)
    ax2.set_title("Required Basel III Regulatory Capital ($ Millions)", fontsize=12, weight="bold", color=NAVY)
    ax2.set_ylabel("Capital Required ($M)", fontsize=11, weight="bold")
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 2.0, f"${yval:.1f}M", ha="center", va="bottom", weight="bold")
        
    ax1.set_xticks(range(len(scenarios)))
    ax1.set_xticklabels(scenarios, rotation=15, ha="right", weight="bold")
    ax2.set_xticks(range(len(scenarios)))
    ax2.set_xticklabels(scenarios, rotation=15, ha="right", weight="bold")
    
    plt.suptitle("Federal Reserve CCAR / EBA Macroeconomic Stress Test Portfolio Impact", fontsize=14, weight="bold", color=NAVY, y=0.98)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[Chart Generated] {save_path}")

def plot_ecl_by_product(
    exec_summary: pd.DataFrame,
    save_path: str = f"{FIGURES_DIR}/07_ifrs9_ecl_by_product.png"
):
    """Bar chart comparing Outstanding Balance vs IFRS 9 ECL Provision by Asset Class."""
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    
    prods = exec_summary["product_type"]
    balance_m = exec_summary["total_outstanding_balance"] / 1e6
    ecl_m = exec_summary["total_ifrs9_ecl"] / 1e6
    
    x = np.arange(len(prods))
    width = 0.38
    
    ax.bar(x - width/2, balance_m, width, label="Total Outstanding Balance ($M)", color=BLUE, alpha=0.85)
    ax.bar(x + width/2, ecl_m, width, label="IFRS 9 ECL Provision ($M)", color=RED, alpha=0.85)
    
    # Annotate coverage ratio
    for i in range(len(prods)):
        cov = exec_summary.loc[i, "ecl_coverage_ratio_pct"]
        ax.text(x[i] + width/2, ecl_m[i] + 15.0, f"Cov: {cov:.1f}%", ha="center", fontsize=9, weight="bold", color=RED)
        
    ax.set_title("Credit Exposure vs IFRS 9 ECL Impairment Reserve by Product", fontsize=14, weight="bold", color=NAVY, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(prods, fontsize=10, weight="bold")
    ax.set_ylabel("Portfolio Amount ($ Millions)", fontsize=11, weight="bold")
    ax.legend(frameon=True, facecolor="white", loc="upper right")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
    print(f"[Chart Generated] {save_path}")

if __name__ == "__main__":
    print("Testing Visualization Suite...")
    clean_df = pd.read_csv("data/processed/portfolio_with_expected_loss.csv")
    stress_sum = pd.read_csv("data/reference/macro_stress_test_summary.csv")
    
    from expected_loss_model import ExpectedLossEngine
    el_engine = ExpectedLossEngine()
    exec_sum = el_engine.generate_executive_summary(clean_df)
    
    # 1. Score distribution
    plot_score_distribution_and_cutoff(clean_df["credit_score"].values, clean_df["default_flag"].values, cutoff=611)
    # 2. K-S statistic
    plot_ks_statistic(clean_df["default_flag"].values, clean_df["predicted_pd"].values, clean_df["credit_score"].values)
    # 3. ROC Curve
    plot_roc_curve(clean_df["default_flag"].values, clean_df["predicted_pd"].values)
    # 4. Vintage
    plot_vintage_analysis(clean_df)
    # 5. Roll rates
    plot_delinquency_roll_rates()
    # 6. Stress test
    plot_stress_test_comparison(stress_sum)
    # 7. ECL by Product
    plot_ecl_by_product(exec_sum)
    print("All 7 banking charts generated successfully!")
