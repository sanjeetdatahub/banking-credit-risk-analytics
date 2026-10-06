"""
Data Cleaning and Preprocessing Module for Adidas US Sales Analysis.
Transforms raw sales strings, formats currencies and percentages,
engineers temporal and categorical features, and saves the cleaned dataset.
"""

import os
import pandas as pd
import numpy as np

def clean_currency(val):
    """Strip currency symbols, commas and convert to float."""
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)):
        return float(val)
    return float(str(val).replace("$", "").replace(",", "").strip())

def clean_percentage(val):
    """Strip percentage symbols and convert to float (0.0 to 1.0)."""
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)):
        return float(val) if val <= 1.0 else float(val) / 100.0
    cleaned = str(val).replace("%", "").strip()
    return float(cleaned) / 100.0 if float(cleaned) > 1.0 else float(cleaned)

def clean_integer(val):
    """Strip commas and convert to int."""
    if pd.isna(val):
        return 0
    if isinstance(val, (int, float)):
        return int(val)
    return int(str(val).replace(",", "").strip())

def load_and_clean_data(raw_filepath=None, processed_filepath=None):
    """
    Main data processing pipeline.
    Reads raw CSV, executes cleaning, feature engineering, validation, and saves cleaned CSV.
    """
    if raw_filepath is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        raw_filepath = os.path.join(project_root, "data", "raw", "adidas_sales.csv")
    
    if processed_filepath is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        processed_filepath = os.path.join(project_root, "data", "processed", "adidas_sales_clean.csv")

    print(f"[*] Loading raw dataset from: {raw_filepath}")
    df = pd.read_csv(raw_filepath)
    initial_shape = df.shape
    print(f"    Raw data records: {initial_shape[0]} rows, {initial_shape[1]} columns")

    # 1. Clean Column Names
    df.columns = df.columns.str.strip()

    # 2. Clean Numeric and Currency Columns
    df["Price per Unit"] = df["Price per Unit"].apply(clean_currency)
    df["Units Sold"] = df["Units Sold"].apply(clean_integer)
    df["Total Sales"] = df["Total Sales"].apply(clean_currency)
    df["Operating Profit"] = df["Operating Profit"].apply(clean_currency)
    df["Operating Margin"] = df["Operating Margin"].apply(clean_percentage)

    # 3. Clean and Parse Dates
    df["Invoice Date"] = pd.to_datetime(df["Invoice Date"])

    # 4. Feature Engineering: Temporal Dimensions
    df["Year"] = df["Invoice Date"].dt.year
    df["Month"] = df["Invoice Date"].dt.month
    df["Month_Name"] = df["Invoice Date"].dt.strftime("%b")
    df["Year_Month"] = df["Invoice Date"].dt.to_period("M").astype(str)
    df["Quarter"] = "Q" + df["Invoice Date"].dt.quarter.astype(str)
    df["Day_Name"] = df["Invoice Date"].dt.day_name()
    df["Is_Weekend"] = df["Invoice Date"].dt.dayofweek.isin([5, 6]).astype(int)

    # 5. Feature Engineering: Product Segmentation
    # Segment: Footwear vs Apparel
    df["Product_Category"] = df["Product"].apply(
        lambda x: "Apparel" if "Apparel" in x else "Footwear"
    )
    
    # Segment: Men's vs Women's
    df["Gender_Target"] = df["Product"].apply(
        lambda x: "Women's" if "Women" in x else ("Men's" if "Men" in x else "Unisex")
    )

    # Calculated Margin Percentage (for display convenience e.g. 42.5%)
    df["Margin_Pct"] = (df["Operating Margin"] * 100).round(2)

    # 6. Sanity Checks and Outlier Validation
    # Recompute total sales discrepancy if any
    calc_sales = (df["Price per Unit"] * df["Units Sold"]).round(2)
    diff = np.abs(df["Total Sales"] - calc_sales)
    if (diff > 1.0).sum() > 0:
        print(f"    Notice: Adjusted {(diff > 1.0).sum()} small rounding discrepancies in Total Sales.")
        df["Total Sales"] = calc_sales

    # Drop any null records if present
    df = df.dropna()

    # Sort deterministically by date
    df = df.sort_values(by="Invoice Date").reset_index(drop=True)

    # Save processed dataset
    os.makedirs(os.path.dirname(processed_filepath), exist_ok=True)
    df.to_csv(processed_filepath, index=False)
    print(f"[✓] Cleaned dataset saved to: {processed_filepath}")
    print(f"    Cleaned records: {df.shape[0]} rows, {df.shape[1]} columns")

    return df

if __name__ == "__main__":
    df_clean = load_and_clean_data()
    print("\nSample Cleaned Data (First 3 rows):")
    print(df_clean[["Invoice Date", "Retailer", "Product", "Product_Category", "Units Sold", "Total Sales", "Operating Margin"]].head(3))
