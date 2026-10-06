"""
Exploratory Data Analysis and Business Insights Engine for Adidas Sales.
Calculates executive KPIs, product performance, channel profitability,
regional distribution, and generates strategic executive summaries.
"""

import os
import pandas as pd
import numpy as np

def compute_executive_kpis(df):
    """Calculates top-line executive KPIs."""
    total_revenue = df["Total Sales"].sum()
    total_profit = df["Operating Profit"].sum()
    total_units = df["Units Sold"].sum()
    avg_margin = (total_profit / total_revenue) * 100
    avg_price = df["Price per Unit"].mean()
    transaction_count = len(df)

    return {
        "Total Revenue": total_revenue,
        "Total Operating Profit": total_profit,
        "Overall Profit Margin (%)": round(avg_margin, 2),
        "Total Units Sold": total_units,
        "Average Price per Unit ($)": round(avg_price, 2),
        "Total Invoices Processed": transaction_count
    }

def analyze_products(df):
    """Analyzes product performance by revenue, volume, and profitability."""
    prod_summary = df.groupby("Product").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum"),
        Avg_Price=("Price per Unit", "mean"),
        Avg_Margin=("Operating Margin", "mean")
    ).reset_index()

    prod_summary["Margin_Pct"] = (prod_summary["Operating_Profit"] / prod_summary["Total_Revenue"] * 100).round(2)
    prod_summary = prod_summary.sort_values(by="Total_Revenue", ascending=False).reset_index(drop=True)
    return prod_summary

def analyze_categories(df):
    """Compares Footwear vs Apparel and Men's vs Women's."""
    cat_summary = df.groupby("Product_Category").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum"),
        Avg_Margin=("Operating Margin", "mean")
    ).reset_index()
    cat_summary["Revenue_Share_Pct"] = (cat_summary["Total_Revenue"] / cat_summary["Total_Revenue"].sum() * 100).round(2)

    gender_summary = df.groupby("Gender_Target").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum"),
        Avg_Margin=("Operating Margin", "mean")
    ).reset_index()
    gender_summary["Revenue_Share_Pct"] = (gender_summary["Total_Revenue"] / gender_summary["Total_Revenue"].sum() * 100).round(2)

    return cat_summary, gender_summary

def analyze_channels(df):
    """Compares In-store, Outlet, and Online sales channels."""
    channel_summary = df.groupby("Sales Method").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum"),
        Avg_Price=("Price per Unit", "mean")
    ).reset_index()

    channel_summary["Profit_Margin_Pct"] = (channel_summary["Operating_Profit"] / channel_summary["Total_Revenue"] * 100).round(2)
    channel_summary["Revenue_Share_Pct"] = (channel_summary["Total_Revenue"] / channel_summary["Total_Revenue"].sum() * 100).round(2)
    return channel_summary.sort_values(by="Total_Revenue", ascending=False).reset_index(drop=True)

def analyze_retailers(df):
    """Ranks retail partners by revenue, profit, and volume."""
    retailer_summary = df.groupby("Retailer").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum"),
        Avg_Margin=("Operating Margin", "mean")
    ).reset_index()

    retailer_summary["Profit_Margin_Pct"] = (retailer_summary["Operating_Profit"] / retailer_summary["Total_Revenue"] * 100).round(2)
    retailer_summary["Revenue_Share_Pct"] = (retailer_summary["Total_Revenue"] / retailer_summary["Total_Revenue"].sum() * 100).round(2)
    return retailer_summary.sort_values(by="Total_Revenue", ascending=False).reset_index(drop=True)

def analyze_geography(df):
    """Analyzes sales across regions and states."""
    region_summary = df.groupby("Region").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum"),
        Avg_Margin=("Operating Margin", "mean")
    ).reset_index()
    region_summary["Revenue_Share_Pct"] = (region_summary["Total_Revenue"] / region_summary["Total_Revenue"].sum() * 100).round(2)
    region_summary = region_summary.sort_values(by="Total_Revenue", ascending=False).reset_index(drop=True)

    state_summary = df.groupby(["State", "Region"]).agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum")
    ).reset_index().sort_values(by="Total_Revenue", ascending=False).reset_index(drop=True)

    return region_summary, state_summary

def analyze_trends(df):
    """Calculates monthly and yearly growth trends."""
    monthly_trend = df.groupby("Year_Month").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum")
    ).reset_index()

    yoy_summary = df.groupby("Year").agg(
        Total_Revenue=("Total Sales", "sum"),
        Operating_Profit=("Operating Profit", "sum"),
        Units_Sold=("Units Sold", "sum")
    ).reset_index()

    if len(yoy_summary) > 1:
        rev_growth = ((yoy_summary.loc[1, "Total_Revenue"] - yoy_summary.loc[0, "Total_Revenue"]) / yoy_summary.loc[0, "Total_Revenue"]) * 100
        profit_growth = ((yoy_summary.loc[1, "Operating_Profit"] - yoy_summary.loc[0, "Operating_Profit"]) / yoy_summary.loc[0, "Operating_Profit"]) * 100
        yoy_summary["Revenue_Growth_YoY_Pct"] = [0.0, round(rev_growth, 2)]
        yoy_summary["Profit_Growth_YoY_Pct"] = [0.0, round(profit_growth, 2)]

    return monthly_trend, yoy_summary

def print_executive_dashboard(df):
    """Prints a styled, readable console dashboard of key analytics."""
    kpis = compute_executive_kpis(df)
    prod = analyze_products(df)
    channel = analyze_channels(df)
    retailer = analyze_retailers(df)
    region, _ = analyze_geography(df)

    print("\n" + "="*70)
    print("           ADIDAS US SALES ANALYTICS - EXECUTIVE DASHBOARD")
    print("="*70)
    print(f" Total Revenue:            ${kpis['Total Revenue']:,.2f}")
    print(f" Total Operating Profit:   ${kpis['Total Operating Profit']:,.2f}")
    print(f" Overall Profit Margin:    {kpis['Overall Profit Margin (%)']}%")
    print(f" Total Units Sold:         {kpis['Total Units Sold']:,} pairs/units")
    print(f" Average Price per Unit:   ${kpis['Average Price per Unit ($)']:.2f}")
    print(f" Total Transactions:       {kpis['Total Invoices Processed']:,}")
    print("-"*70)

    print("\n[★] Top Products by Revenue:")
    for _, row in prod.iterrows():
        print(f"  • {row['Product']:<28} | Rev: ${row['Total_Revenue']:>11,.2f} | Margin: {row['Margin_Pct']:>5.1f}% | Units: {row['Units_Sold']:>7,}")

    print("\n[★] Sales Channels Breakdown:")
    for _, row in channel.iterrows():
        print(f"  • {row['Sales Method']:<12} | Share: {row['Revenue_Share_Pct']:>5.1f}% | Rev: ${row['Total_Revenue']:>11,.2f} | Margin: {row['Profit_Margin_Pct']:>5.1f}%")

    print("\n[★] Top Retail Partners:")
    for _, row in retailer.iterrows():
        print(f"  • {row['Retailer']:<15} | Share: {row['Revenue_Share_Pct']:>5.1f}% | Rev: ${row['Total_Revenue']:>11,.2f} | Profit: ${row['Operating_Profit']:>10,.2f}")

    print("\n[★] Regional Sales Distribution:")
    for _, row in region.iterrows():
        print(f"  • {row['Region']:<12} | Share: {row['Revenue_Share_Pct']:>5.1f}% | Rev: ${row['Total_Revenue']:>11,.2f}")
    print("="*70 + "\n")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, "data", "processed", "adidas_sales_clean.csv")
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        print_executive_dashboard(df)
    else:
        print("Processed data not found. Run data_cleaner.py first.")
