"""
End-to-End Enterprise Credit Risk Pipeline Runner
Executes the full institutional workflow from data generation to Basel scoring,
Expected Loss calculation, Macro Stress Testing, and Visual Report compilation.
"""

import os
import sys
import time
import numpy as np
import pandas as pd

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from data_generator import generate_banking_portfolio
from data_preprocessing import preprocess_credit_portfolio, train_test_split_stratified
from woe_iv_engine import WoEIVEngine
from risk_scorecard import CreditScorecard
from expected_loss_model import ExpectedLossEngine
from stress_testing import MacroStressTester
from visualization import (
    plot_score_distribution_and_cutoff,
    plot_ks_statistic,
    plot_roc_curve,
    plot_vintage_analysis,
    plot_delinquency_roll_rates,
    plot_stress_test_comparison,
    plot_ecl_by_product
)

def main():
    print("=" * 80)
    print("  ENTERPRISE RETAIL BANKING CREDIT RISK & BASEL II/III ECL ENGINE  ")
    print("=" * 80)
    start_time = time.time()
    
    # 1. Data Ingestion / Generation
    raw_path = "data/raw/loan_portfolio_raw.csv"
    if not os.path.exists(raw_path):
        print("\n[Step 1/7] Generating synthetic retail banking portfolio (50,000 accounts)...")
        raw_df = generate_banking_portfolio(n_records=50000, random_seed=42)
        raw_df.to_csv(raw_path, index=False)
    else:
        print(f"\n[Step 1/7] Ingesting existing raw portfolio: {raw_path}")
        raw_df = pd.read_csv(raw_path)
    print(f"-> Total Portfolio Size: {len(raw_df):,} accounts")
    print(f"-> Unconditional Default Rate: {raw_df['default_flag'].mean()*100:.2f}%")
    
    # 2. Preprocessing & IFRS-9 Staging
    print("\n[Step 2/7] Preprocessing portfolio, winsorizing outliers, assigning IFRS-9 stages...")
    clean_df = preprocess_credit_portfolio(raw_df)
    train_df, test_df = train_test_split_stratified(clean_df, test_size=0.30, random_seed=42)
    clean_df.to_csv("data/processed/portfolio_clean.csv", index=False)
    train_df.to_csv("data/processed/portfolio_train.csv", index=False)
    test_df.to_csv("data/processed/portfolio_test.csv", index=False)
    print(f"-> Training Set: {len(train_df):,} | Holdout Validation Set: {len(test_df):,}")
    
    # 3. Weight of Evidence (WoE) & Information Value (IV) Analysis
    print("\n[Step 3/7] Running WoE binning and Information Value ranking...")
    engine = WoEIVEngine(target_col="default_flag", n_bins=5)
    candidate_num = ["bureau_credit_score", "debt_to_income_ratio", "revolving_utilization_pct", 
                     "inquiries_last_6m", "annual_income", "employment_years"]
    candidate_cat = ["product_type", "home_ownership"]
    
    iv_report = engine.fit_all(train_df, candidate_num, candidate_cat)
    iv_report.to_csv("data/reference/iv_summary_report.csv", index=False)
    print("-> Top Predictors by Information Value (IV):")
    for _, row in iv_report.head(5).iterrows():
        print(f"   * {row['feature']:<25}: IV = {row['iv']:.4f} ({row['power_classification']})")
        
    selected_features = ["bureau_credit_score", "debt_to_income_ratio", "revolving_utilization_pct", "inquiries_last_6m"]
    X_train_woe = engine.transform_to_woe(train_df, selected_features)
    X_test_woe = engine.transform_to_woe(test_df, selected_features)
    X_full_woe = engine.transform_to_woe(clean_df, selected_features)
    
    # 4. Scorecard Fitting & Calibration
    print("\n[Step 4/7] Fitting PD Scorecard and Calibrating 300-850 Credit Scores...")
    scorecard = CreditScorecard(target_score=660.0, target_odds=25.0, pdo=40.0)
    scorecard.fit(X_train_woe, train_df["default_flag"])
    
    # Predict on holdout test set
    test_pd = scorecard.predict_pd(X_test_woe)
    test_scores = scorecard.calculate_credit_score(test_pd)
    metrics = scorecard.evaluate_model(test_df["default_flag"].values, test_pd, test_scores)
    
    print("-> Validation Performance:")
    print(f"   * ROC-AUC Score:      {metrics['roc_auc']:.4f}")
    print(f"   * Gini Coefficient:   {metrics['gini_coefficient']:.4f}")
    print(f"   * K-S Statistic:      {metrics['ks_statistic_pct']:.2f}% (Separation at Score = {metrics['ks_optimal_score_cutoff']})")
    
    # Full portfolio scores
    clean_df["predicted_pd"] = scorecard.predict_pd(X_full_woe)
    clean_df["credit_score"] = scorecard.calculate_credit_score(clean_df["predicted_pd"])
    
    # Cutoff policy matrix
    cutoff_table = scorecard.generate_cutoff_matrix(test_scores, test_df["default_flag"].values)
    cutoff_table.to_csv("data/reference/credit_cutoff_policy_matrix.csv", index=False)
    
    # 5. Basel II/III Expected Loss & IFRS-9 Provisioning
    print("\n[Step 5/7] Computing EAD, LGD, Expected Loss (EL = PD * LGD * EAD) & Capital Requirements...")
    el_engine = ExpectedLossEngine()
    enriched_portfolio = el_engine.calculate_portfolio_losses(clean_df, clean_df["predicted_pd"])
    exec_summary = el_engine.generate_executive_summary(enriched_portfolio)
    
    enriched_portfolio.to_csv("data/processed/portfolio_with_expected_loss.csv", index=False)
    exec_summary.to_csv("data/reference/portfolio_loss_summary.csv", index=False)
    
    total_balance = enriched_portfolio["current_balance"].sum()
    total_ead = enriched_portfolio["calibrated_ead"].sum()
    total_el = enriched_portfolio["base_expected_loss"].sum()
    total_ecl = enriched_portfolio["ifrs9_ecl_provision"].sum()
    total_rwa = enriched_portfolio["rwa_amount"].sum()
    total_cap = enriched_portfolio["regulatory_capital_required"].sum()
    
    print(f"-> Total Portfolio Outstanding:   ${total_balance/1e6:,.2f} Million")
    print(f"-> Total Exposure at Default (EAD): ${total_ead/1e6:,.2f} Million")
    print(f"-> Baseline 12-Month Expected Loss: ${total_el/1e6:,.2f} Million ({(total_el/total_ead)*100:.2f}%)")
    print(f"-> IFRS 9 Staged ECL Impairment:    ${total_ecl/1e6:,.2f} Million ({(total_ecl/total_balance)*100:.2f}% Coverage)")
    print(f"-> Basel III Regulatory Capital:    ${total_cap/1e6:,.2f} Million (8% CAR on RWA)")
    
    # 6. CCAR Macroeconomic Stress Testing
    print("\n[Step 6/7] Running Federal Reserve CCAR / EBA Macro Stress Scenarios...")
    stress_tester = MacroStressTester()
    stress_summary, product_stress = stress_tester.run_stress_test(enriched_portfolio)
    stress_summary.to_csv("data/reference/macro_stress_test_summary.csv", index=False)
    product_stress.to_csv("data/reference/product_stress_breakdown.csv", index=False)
    
    for _, s_row in stress_summary.iterrows():
        print(f"   * {s_row['Scenario']:<35}: Stressed EL = ${s_row['Expected Loss ($M)']:.2f}M (+{s_row['EL Increase (%)']}%) | Req Capital = ${s_row['Required Regulatory Capital ($M)']:.2f}M")
        
    # 7. Visual Reporting & Figure Generation
    print("\n[Step 7/7] Rendering publication-grade executive charts in reports/figures/...")
    cutoff_point = metrics['ks_optimal_score_cutoff']
    plot_score_distribution_and_cutoff(clean_df["credit_score"].values, clean_df["default_flag"].values, cutoff=cutoff_point)
    plot_ks_statistic(clean_df["default_flag"].values, clean_df["predicted_pd"].values, clean_df["credit_score"].values)
    plot_roc_curve(clean_df["default_flag"].values, clean_df["predicted_pd"].values)
    plot_vintage_analysis(clean_df)
    plot_delinquency_roll_rates()
    plot_stress_test_comparison(stress_summary)
    plot_ecl_by_product(exec_summary)
    
    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"PIPELINE COMPLETED SUCCESSFULLY IN {elapsed:.2f} SECONDS!")
    print("All datasets, risk scorecards, stress test tables, and visualizations are ready.")
    print("=" * 80)

if __name__ == "__main__":
    main()
