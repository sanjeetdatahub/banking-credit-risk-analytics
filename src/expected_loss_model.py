"""
Basel II/III & IFRS-9 Expected Loss (ECL) Calculation Engine
Computes Exposure at Default (EAD), Loss Given Default (LGD),
12-Month / Lifetime Expected Loss (EL = PD * LGD * EAD),
and regulatory Risk-Weighted Assets (RWA).
"""

import numpy as np
import pandas as pd
from typing import Dict

class ExpectedLossEngine:
    """
    Implements Basel II/III Foundation Internal Ratings-Based (F-IRB)
    and IFRS 9 staging impairment calculations.
    """
    def __init__(self, ccf_mapping: Dict[str, float] = None, lgd_mapping: Dict[str, float] = None):
        self.ccf_mapping = ccf_mapping or {
            "MORTGAGE": 0.0,
            "AUTO_LOAN": 0.0,
            "PERSONAL_LOAN": 0.10,
            "CREDIT_CARD": 0.75,
            "SME_WORKING_CAP": 0.50
        }
        self.lgd_mapping = lgd_mapping or {
            "MORTGAGE": 0.18,
            "AUTO_LOAN": 0.35,
            "PERSONAL_LOAN": 0.70,
            "CREDIT_CARD": 0.85,
            "SME_WORKING_CAP": 0.45
        }

    def compute_ead(self, df: pd.DataFrame) -> pd.Series:
        """
        EAD = Current Balance + (Credit Conversion Factor * Undrawn Amount)
        """
        ccf_series = df["product_type"].map(self.ccf_mapping).fillna(0.20)
        undrawn = np.maximum(0.0, df["credit_limit"] - df["current_balance"])
        ead = df["current_balance"] + (ccf_series * undrawn)
        return ead.round(2)

    def compute_lgd(self, df: pd.DataFrame) -> pd.Series:
        """
        Assigns Basel regulatory LGD based on product collateral hierarchy.
        """
        return df["product_type"].map(self.lgd_mapping).fillna(0.50)

    def calculate_portfolio_losses(self, df: pd.DataFrame, pd_series: pd.Series) -> pd.DataFrame:
        """
        Calculates loan-level EAD, LGD, Expected Loss (EL),
        and applies IFRS-9 Stage 1 / Stage 2 / Stage 3 impairment adjustments.
        """
        results = df.copy()
        results["predicted_pd"] = pd_series
        results["calibrated_ead"] = self.compute_ead(results)
        results["assigned_lgd"] = self.compute_lgd(results)
        
        # 1. Base 12-Month Expected Loss
        results["base_expected_loss"] = (
            results["predicted_pd"] * results["assigned_lgd"] * results["calibrated_ead"]
        ).round(2)
        
        # 2. IFRS 9 Multi-Stage ECL Provisioning
        # Stage 1: 12-Month ECL
        # Stage 2: Significant Increase in Credit Risk (SICR) -> Lifetime ECL (~2.5x multiplier)
        # Stage 3: Credit Impaired / Default -> Specific Allowance (LGD * EAD)
        ecl_stage_adjusted = np.zeros(len(results))
        
        for i, row in results.iterrows():
            stage = row.get("ifrs9_stage", "Stage 1 (Current)")
            el_base = row["base_expected_loss"]
            lgd = row["assigned_lgd"]
            ead = row["calibrated_ead"]
            
            if "Stage 3" in stage or row["default_flag"] == 1:
                # Stage 3: Incurred / Specific provision
                ecl_stage_adjusted[i] = round(lgd * ead, 2)
            elif "Stage 2" in stage:
                # Stage 2: Lifetime expected loss
                ecl_stage_adjusted[i] = round(el_base * 2.5, 2)
            else:
                # Stage 1: 12-month expected loss
                ecl_stage_adjusted[i] = el_base
                
        results["ifrs9_ecl_provision"] = ecl_stage_adjusted
        
        # 3. Basel Risk-Weighted Assets (RWA) estimation:
        # Standardized supervisory risk weight approx: Mortgage (35%), Auto (75%), Unsecured (100-150%)
        rwa_weights = {"MORTGAGE": 0.35, "AUTO_LOAN": 0.75, "PERSONAL_LOAN": 1.00, "CREDIT_CARD": 1.00, "SME_WORKING_CAP": 0.85}
        results["risk_weight"] = results["product_type"].map(rwa_weights).fillna(1.0)
        results["rwa_amount"] = (results["calibrated_ead"] * results["risk_weight"]).round(2)
        
        # Minimum Regulatory Capital Required (8.0% Basel Pillar 1 CAR)
        results["regulatory_capital_required"] = (results["rwa_amount"] * 0.08).round(2)
        
        return results

    def generate_executive_summary(self, enriched_df: pd.DataFrame) -> pd.DataFrame:
        """
        Aggregates balance, EAD, ECL, and regulatory capital by product portfolio.
        """
        summary = enriched_df.groupby("product_type").agg(
            total_accounts=("loan_id", "count"),
            total_outstanding_balance=("current_balance", "sum"),
            total_ead=("calibrated_ead", "sum"),
            avg_pd=("predicted_pd", "mean"),
            avg_lgd=("assigned_lgd", "mean"),
            total_12m_el=("base_expected_loss", "sum"),
            total_ifrs9_ecl=("ifrs9_ecl_provision", "sum"),
            regulatory_capital=("regulatory_capital_required", "sum")
        ).reset_index()
        
        summary["avg_pd"] = (summary["avg_pd"] * 100.0).round(2)
        summary["avg_lgd"] = (summary["avg_lgd"] * 100.0).round(2)
        summary["ecl_coverage_ratio_pct"] = (
            (summary["total_ifrs9_ecl"] / summary["total_outstanding_balance"]) * 100.0
        ).round(2)
        
        return summary

if __name__ == "__main__":
    from woe_iv_engine import WoEIVEngine
    from risk_scorecard import CreditScorecard
    
    clean_df = pd.read_csv("data/processed/portfolio_clean.csv")
    engine = WoEIVEngine()
    features = ["bureau_credit_score", "debt_to_income_ratio", "revolving_utilization_pct", "inquiries_last_6m"]
    engine.fit_all(clean_df, features, [])
    
    X_woe = engine.transform_to_woe(clean_df, features)
    scorecard = CreditScorecard()
    scorecard.fit(X_woe, clean_df["default_flag"])
    clean_df["predicted_pd"] = scorecard.predict_pd(X_woe)
    clean_df["credit_score"] = scorecard.calculate_credit_score(clean_df["predicted_pd"])
    
    el_engine = ExpectedLossEngine()
    enriched = el_engine.calculate_portfolio_losses(clean_df, clean_df["predicted_pd"])
    exec_summary = el_engine.generate_executive_summary(enriched)
    
    print("\n--- Basel II / IFRS-9 Portfolio Loss & Capital Provisioning Summary ---")
    print(exec_summary.to_string(index=False))
    
    enriched.to_csv("data/processed/portfolio_with_expected_loss.csv", index=False)
