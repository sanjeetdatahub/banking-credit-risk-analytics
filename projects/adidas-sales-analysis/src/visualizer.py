"""
Data Visualization Module for Adidas US Sales Analysis.
Generates publication-quality charts using Matplotlib and Seaborn.
Saves all figures to reports/figures/ for GitHub README embedding and portfolio presentations.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set global visual style
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.labelsize"] = 11
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10
plt.rcParams["figure.titlesize"] = 16

# Primary Color Palette (Adidas corporate inspired)
PALETTE = {
    "blue": "#0055A5",
    "dark_blue": "#002B49",
    "cyan": "#00A3E0",
    "black": "#1B1B1B",
    "gray": "#708090",
    "light_gray": "#F4F6F9",
    "coral": "#E63946",
    "teal": "#2A9D8F",
    "amber": "#E9C46A",
    "soft_orange": "#F4A261"
}

def ensure_output_dir(output_dir):
    os.makedirs(output_dir, exist_ok=True)

def plot_sales_and_profit_by_product(df, output_dir):
    """Figure 1: Product-wise Revenue and Operating Profit."""
    summary = df.groupby("Product").agg(
        Total_Sales=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum")
    ).sort_values(by="Total_Sales", ascending=True)

    summary["Sales_M"] = summary["Total_Sales"] / 1e6
    summary["Profit_M"] = summary["Operating_Profit"] / 1e6

    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    y = np.arange(len(summary))
    height = 0.38

    rects1 = ax.barh(y - height/2, summary["Sales_M"], height, label="Total Sales ($M)", color=PALETTE["blue"], alpha=0.9)
    rects2 = ax.barh(y + height/2, summary["Profit_M"], height, label="Operating Profit ($M)", color=PALETTE["teal"], alpha=0.9)

    ax.set_xlabel("Amount in Millions ($ USD)")
    ax.set_title("Total Sales vs. Operating Profit by Product Category", pad=15)
    ax.set_yticks(y)
    ax.set_yticklabels(summary.index, fontweight="medium")
    ax.legend(frameon=True, facecolor="white", edgecolor="none")
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    # Annotate bar values
    for rect in rects1:
        w = rect.get_width()
        ax.annotate(f"${w:.1f}M", xy=(w, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=9, fontweight="bold", color="#1B1B1B")

    for rect in rects2:
        w = rect.get_width()
        ax.annotate(f"${w:.1f}M", xy=(w, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=9, fontweight="bold", color="#2A9D8F")

    ax.set_xlim(0, summary["Sales_M"].max() * 1.18)
    plt.tight_layout()
    out_path = os.path.join(output_dir, "01_total_sales_and_profit_by_product.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  [✓] Saved: {out_path}")

def plot_monthly_sales_trend(df, output_dir):
    """Figure 2: Time-series monthly revenue trend."""
    monthly = df.groupby(["Year", "Month", "Year_Month"]).agg(
        Total_Sales=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum")
    ).reset_index().sort_values(by=["Year", "Month"])

    monthly["Sales_M"] = monthly["Total_Sales"] / 1e6
    monthly["Profit_M"] = monthly["Operating_Profit"] / 1e6

    fig, ax = plt.subplots(figsize=(14, 6), dpi=300)

    x = np.arange(len(monthly))
    ax.plot(x, monthly["Sales_M"], marker="o", linewidth=2.5, markersize=6, color=PALETTE["blue"], label="Monthly Revenue ($M)")
    ax.plot(x, monthly["Profit_M"], marker="s", linewidth=2.0, markersize=5, color=PALETTE["coral"], linestyle="--", label="Monthly Profit ($M)")
    ax.fill_between(x, monthly["Sales_M"], alpha=0.12, color=PALETTE["blue"])

    ax.set_xticks(x)
    ax.set_xticklabels(monthly["Year_Month"], rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("Revenue & Profit in Millions ($ USD)")
    ax.set_title("Monthly Sales & Operating Profit Trend (2020 - 2021)", pad=15)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(frameon=True, facecolor="white")

    # Annotate peak months
    peak_idx = monthly["Sales_M"].idxmax()
    peak_x = x[peak_idx]
    peak_y = monthly.loc[peak_idx, "Sales_M"]
    ax.annotate(f"Peak Month: {monthly.loc[peak_idx, 'Year_Month']}\n${peak_y:.2f}M",
                xy=(peak_x, peak_y), xytext=(peak_x - 3, peak_y + 0.8),
                arrowprops=dict(facecolor=PALETTE["dark_blue"], arrowstyle="->", lw=1.5),
                fontweight="bold", bbox=dict(boxstyle="round,pad=0.4", fc="#FFF3CD", ec="#FFEBAA"))

    ax.set_ylim(0, monthly["Sales_M"].max() * 1.25)
    plt.tight_layout()
    out_path = os.path.join(output_dir, "02_monthly_sales_trend.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  [✓] Saved: {out_path}")

def plot_sales_by_region_and_retailer(df, output_dir):
    """Figure 3: Clustered analysis of Region and Retail Partners."""
    pivot = df.pivot_table(index="Region", columns="Retailer", values="Total Sales", aggfunc="sum", fill_value=0) / 1e6

    colors = [PALETTE["blue"], PALETTE["teal"], PALETTE["cyan"], PALETTE["coral"], PALETTE["amber"], "#8338EC"]
    fig, ax = plt.subplots(figsize=(13, 6.5), dpi=300)
    pivot.plot(kind="bar", ax=ax, color=colors, width=0.8)

    ax.set_ylabel("Total Sales in Millions ($ USD)")
    ax.set_xlabel("Geographic Region")
    ax.set_title("Sales Distribution Across Geographic Regions by Retail Partner", pad=15)
    ax.set_xticklabels(pivot.index, rotation=0, fontweight="bold")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.legend(title="Retail Partner", frameon=True, bbox_to_anchor=(1.02, 1), loc="upper left")

    plt.tight_layout()
    out_path = os.path.join(output_dir, "03_sales_by_region_and_retailer.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  [✓] Saved: {out_path}")

def plot_sales_channel_efficiency(df, output_dir):
    """Figure 4: Sales Method share and profitability donut + bar."""
    channel = df.groupby("Sales Method").agg(
        Total_Sales=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum")
    ).reset_index()
    channel["Margin_Pct"] = (channel["Operating_Profit"] / channel["Total_Sales"]) * 100

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=300)

    # Donut Chart for Revenue Share
    colors = [PALETTE["blue"], PALETTE["teal"], PALETTE["coral"]]
    wedges, texts, autotexts = ax1.pie(
        channel["Total_Sales"],
        labels=channel["Sales Method"],
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2),
        pctdistance=0.75
    )
    for at in autotexts:
        at.set_color("white")
        at.set_fontweight("bold")
    ax1.set_title("Revenue Share by Sales Method", pad=10)

    # Bar chart for Operating Margin %
    bars = ax2.bar(channel["Sales Method"], channel["Margin_Pct"], color=colors, width=0.5)
    ax2.set_ylabel("Operating Margin (%)")
    ax2.set_title("Profit Margin Efficiency by Sales Method", pad=10)
    ax2.grid(axis="y", linestyle="--", alpha=0.5)
    ax2.set_ylim(0, channel["Margin_Pct"].max() * 1.25)

    for bar in bars:
        h = bar.get_height()
        ax2.annotate(f"{h:.1f}%", xy=(bar.get_x() + bar.get_width()/2, h),
                     xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                     fontweight="bold")

    plt.suptitle("Sales Channel Breakdown: Volume vs. Margin Comparison", fontsize=15, fontweight="bold", y=1.02)
    plt.tight_layout()
    out_path = os.path.join(output_dir, "04_sales_method_profitability.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  [✓] Saved: {out_path}")

def plot_top_10_states(df, output_dir):
    """Figure 5: Top 10 Revenue Generating States."""
    state_df = df.groupby("State").agg(
        Total_Sales=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum")
    ).reset_index().sort_values(by="Total_Sales", ascending=False).head(10)

    state_df["Sales_M"] = state_df["Total_Sales"] / 1e6
    state_df = state_df.sort_values(by="Sales_M", ascending=True)

    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    bars = ax.barh(state_df["State"], state_df["Sales_M"], color=PALETTE["blue"], alpha=0.85, height=0.6)

    ax.set_xlabel("Total Sales in Millions ($ USD)")
    ax.set_title("Top 10 US States by Total Sales Revenue", pad=15)
    ax.grid(axis="x", linestyle="--", alpha=0.5)

    for bar in bars:
        w = bar.get_width()
        ax.annotate(f"${w:.2f}M", xy=(w, bar.get_y() + bar.get_height()/2),
                    xytext=(5, 0), textcoords="offset points", ha="left", va="center",
                    fontweight="bold", color=PALETTE["black"])

    ax.set_xlim(0, state_df["Sales_M"].max() * 1.15)
    plt.tight_layout()
    out_path = os.path.join(output_dir, "05_top_10_states_revenue.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  [✓] Saved: {out_path}")

def plot_correlation_heatmap(df, output_dir):
    """Figure 6: Correlation Heatmap between key numeric drivers."""
    numeric_cols = ["Price per Unit", "Units Sold", "Total Sales", "Operating Profit", "Operating Margin"]
    corr = df[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(8, 6.5), dpi=300)
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="Blues",
        cbar_kws={"label": "Pearson Correlation Coefficient"},
        square=True,
        linewidths=1.2,
        linecolor="white",
        ax=ax
    )
    ax.set_title("Correlation Heatmap: Sales Drivers & Profitability", pad=15)
    plt.xticks(rotation=30, ha="right")
    plt.yticks(rotation=0)

    plt.tight_layout()
    out_path = os.path.join(output_dir, "06_correlation_heatmap.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  [✓] Saved: {out_path}")

def plot_gender_and_category_breakdown(df, output_dir):
    """Figure 7: Gender target and Apparel vs Footwear category share."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5), dpi=300)

    # 1. Product Category
    cat = df.groupby("Product_Category")["Total Sales"].sum()
    ax1.pie(cat, labels=cat.index, autopct="%1.1f%%", startangle=90,
            colors=[PALETTE["blue"], PALETTE["cyan"]],
            wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2),
            textprops={"fontsize": 11, "fontweight": "bold"})
    ax1.set_title("Product Category: Apparel vs Footwear", pad=10)

    # 2. Gender Target
    gender = df.groupby("Gender_Target")["Total Sales"].sum()
    ax2.pie(gender, labels=gender.index, autopct="%1.1f%%", startangle=90,
            colors=[PALETTE["teal"], PALETTE["soft_orange"]],
            wedgeprops=dict(width=0.45, edgecolor="white", linewidth=2),
            textprops={"fontsize": 11, "fontweight": "bold"})
    ax2.set_title("Target Demographic: Men's vs Women's", pad=10)

    plt.suptitle("Portfolio Segmentation by Category & Target Audience", fontsize=15, fontweight="bold", y=1.02)
    plt.tight_layout()
    out_path = os.path.join(output_dir, "07_gender_and_category_breakdown.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"  [✓] Saved: {out_path}")

def generate_all_visualizations(df, output_dir=None):
    """Generates all 7 publication-grade visualizations."""
    if output_dir is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        output_dir = os.path.join(project_root, "reports", "figures")

    ensure_output_dir(output_dir)
    print(f"\n[*] Generating high-resolution charts in: {output_dir}")

    plot_sales_and_profit_by_product(df, output_dir)
    plot_monthly_sales_trend(df, output_dir)
    plot_sales_by_region_and_retailer(df, output_dir)
    plot_sales_channel_efficiency(df, output_dir)
    plot_top_10_states(df, output_dir)
    plot_correlation_heatmap(df, output_dir)
    plot_gender_and_category_breakdown(df, output_dir)

    print("[✓] All 7 charts successfully rendered and saved!\n")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, "data", "processed", "adidas_sales_clean.csv")

    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        generate_all_visualizations(df)
    else:
        print("Processed data not found. Run data_cleaner.py first.")
