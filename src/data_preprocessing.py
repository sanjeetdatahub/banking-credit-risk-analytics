"""
Data Preprocessing & Feature Engineering Module
Handles data quality audits, missing value strategies, banking outlier winsorization,
IFRS 9 impairment staging, and train/test stratified partitioning.
"""

import numpy as np
import pandas as pd
from typing import Tuple, Dict

def preprocess_credit_portfolio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw banking portfolio, derives banking credit metrics,
    and assigns IFRS-9 / CECL impairment stages.
    """
    data = df.copy()
    
    # 1. Feature Engineering
    # Undrawn credit line exposure
    data["undrawn_amount"] = np.maximum(0.0, data["credit_limit"] - data["current_balance"])
    
    # Overall balance-to-limit ratio
    data["balance_to_limit_ratio"] = (data["current_balance"] / np.maximum(data["credit_limit"], 1.0)).round(4)
    
    # Estimated monthly debt burden relative to monthly income
    monthly_income = np.maximum(data["annual_income"] / 12.0, 500.0)
    data["estimated_monthly_burden"] = ((data["debt_to_income_ratio"] / 100.0) * monthly_income).round(2)
    
    # 2. Outlier Treatment (Banking Winsorization at 99.5th percentile)
    for col in ["debt_to_income_ratio", "revolving_utilization_pct", "inquiries_last_6m"]:
        upper_limit = np.percentile(data[col], 99.5)
        data[f"{col}_capped"] = np.minimum(data[col], upper_limit)
        
    # 3. IFRS 9 Accounting Classification (Stage 1, Stage 2, Stage 3)
    # Stage 1: Performing (0-30 DPD) -> 12-Month Expected Loss
    # Stage 2: Underperforming / Significant Increase in Credit Risk (31-89 DPD) -> Lifetime Expected Loss
    # Stage 3: Credit Impaired / Defaulted (90+ DPD) -> Lifetime Expected Loss
    conditions = [
        data["days_past_due"] == 0,
        (data["days_past_due"] > 0) & (data["days_past_due"] < 30),
        (data["days_past_due"] >= 30) & (data["days_past_due"] < 90),
        data["days_past_due"] >= 90
    ]
    stage_labels = ["Stage 1 (Current)", "Stage 1 (1-29 DPD)", "Stage 2 (SICR 30-89 DPD)", "Stage 3 (Default 90+ DPD)"]
    data["ifrs9_stage"] = np.select(conditions, stage_labels, default="Stage 1 (Current)")
    
    return data

def train_test_split_stratified(
    df: pd.DataFrame, 
    target_col: str = "default_flag", 
    test_size: float = 0.30, 
    random_seed: int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Performs stratified train/test split on credit portfolio ensuring 
    identical default proportions in train and holdout validation sets.
    """
    np.random.seed(random_seed)
    
    defaults = df[df[target_col] == 1]
    non_defaults = df[df[target_col] == 0]
    
    n_def_test = int(len(defaults) * test_size)
    n_non_def_test = int(len(non_defaults) * test_size)
    
    def_test_idx = np.random.choice(defaults.index, size=n_def_test, replace=False)
    non_def_test_idx = np.random.choice(non_defaults.index, size=n_non_def_test, replace=False)
    
    test_indices = np.concatenate([def_test_idx, non_def_test_idx])
    train_indices = df.index.difference(test_indices)
    
    train_df = df.loc[train_indices].copy().reset_index(drop=True)
    test_df = df.loc[test_indices].copy().reset_index(drop=True)
    
    return train_df, test_df

if __name__ == "__main__":
    print("Testing Preprocessing Pipeline...")
    raw_df = pd.read_csv("data/raw/loan_portfolio_raw.csv")
    clean_df = preprocess_credit_portfolio(raw_df)
    train_df, test_df = train_test_split_stratified(clean_df)
    
    clean_df.to_csv("data/processed/portfolio_clean.csv", index=False)
    train_df.to_csv("data/processed/portfolio_train.csv", index=False)
    test_df.to_csv("data/processed/portfolio_test.csv", index=False)
    
    print(f"Processed: {len(clean_df):,} records")
    print(f"Train set: {len(train_df):,} records (Default: {train_df['default_flag'].mean()*100:.2f}%)")
    print(f"Test set:  {len(test_df):,} records (Default: {test_df['default_flag'].mean()*100:.2f}%)")
