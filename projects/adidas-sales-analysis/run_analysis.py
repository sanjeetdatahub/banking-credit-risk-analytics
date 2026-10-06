"""
Master Pipeline Script: Adidas US Sales Data Analytics
Executes end-to-end data cleaning, feature engineering, exploratory data analysis,
executive dashboard reporting, and visualization generation.

Usage:
    python run_analysis.py
"""

import os
import sys
import time

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.generate_dataset import generate_adidas_sales_data
from src.data_cleaner import load_and_clean_data
from src.eda_insights import print_executive_dashboard, compute_executive_kpis
from src.visualizer import generate_all_visualizations

def run_pipeline():
    start_time = time.time()
    print("=" * 75)
    print("        🚀 ADIDAS US SALES ANALYTICS - END-TO-END PIPELINE")
    print("=" * 75)

    raw_path = os.path.join(PROJECT_ROOT, "data", "raw", "adidas_sales.csv")
    clean_path = os.path.join(PROJECT_ROOT, "data", "processed", "adidas_sales_clean.csv")
    figures_dir = os.path.join(PROJECT_ROOT, "reports", "figures")

    # Step 1: Check or Generate Raw Dataset
    if not os.path.exists(raw_path):
        print("\n[Step 1/4] Generating raw dataset...")
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        df_raw = generate_adidas_sales_data(num_records=9648)
        df_raw.to_csv(raw_path, index=False)
        print(f"  [✓] Created raw dataset: {raw_path}")
    else:
        print(f"\n[Step 1/4] Verified raw dataset at: {raw_path}")

    # Step 2: Data Cleaning & Feature Engineering
    print("\n[Step 2/4] Executing Data Cleaning & Feature Engineering...")
    df_clean = load_and_clean_data(raw_filepath=raw_path, processed_filepath=clean_path)

    # Step 3: Exploratory Data Analysis & Executive Dashboard
    print("\n[Step 3/4] Computing Business Analytics & Key Performance Indicators...")
    print_executive_dashboard(df_clean)

    # Step 4: Data Visualization Generation
    print("\n[Step 4/4] Generating Publication-Quality Figures with Matplotlib & Seaborn...")
    generate_all_visualizations(df_clean, output_dir=figures_dir)

    elapsed = time.time() - start_time
    print("=" * 75)
    print(f"🎉 Pipeline completed successfully in {elapsed:.2f} seconds!")
    print(f"📁 Cleaned data ready at:   {clean_path}")
    print(f"📊 Figures exported to:     {figures_dir}")
    print("=" * 75)

if __name__ == "__main__":
    run_pipeline()
