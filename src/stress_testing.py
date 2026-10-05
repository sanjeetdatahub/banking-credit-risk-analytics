"""
Macroeconomic Stress Testing Engine (CCAR / DFAST / EBA Methodology)
Simulates portfolio losses, impairment spikes, and capital depletion under
Baseline, Adverse, and Severely Adverse macroeconomic shock scenarios.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple

class MacroStressTester:
    """
    Applies macroeconomic stress factors to loan-level PD, LGD, and EAD
    to project portfolio performance under economic downturns.
    """
    def __init__(self, scenarios: Dict[str, Dict] = None):
        self.scenarios = scenarios or {
            "Baseline": {
                "desc": "Current macroeconomic trajectory",
                "pd_mult": 1.00,
                "lgd_mult": 1.00,
                "ead_draw_spike": 0.00
            },
            "Adverse (Stagflation)": {
                "desc": "+2.2% Unemployment, +150bps Rates, -1.5% GDP",
                "pd_mult": 1.45,
                "lgd_mult": 1.15,
                "ead_draw_spike": 0.15 # Consumers draw 15% more on credit cards
            },
            "Severely Adverse (Global Recession)": {
                "desc": "+4.8% Unemployment, +300bps Rates, -4.2% GDP",
                "pd_mult": 2.25,
                "lgd_mult": 1.30,
                "ead_draw_spike": 0.35 # Credit line utilization surges under liquidity stress
            }
        }

    def run_stress_test(self, portfolio_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Runs stress tests across all scenarios and outputs:
        1. Portfolio-level aggregated impact table
        2. Product-by-product loss comparison
        """
        scenario_summaries = []
        product_breakdowns = []
        
        base_ead = portfolio_df["calibrated_ead"]
        base_pd = portfolio_df["predicted_pd"]
        base_lgd = portfolio_df["assigned_lgd"]
        base_balance = portfolio_df["current_balance"].sum()
        
        for sc_name, params in self.scenarios.items():
            pd_mult = params["pd_mult"]
            lgd_mult = params["lgd_mult"]
            ead_spike = params["ead_draw_spike"]
            
            # Stressed parameters
            stressed_pd = np.clip(base_pd * pd_mult, 0.001, 0.98)
            stressed_lgd = np.clip(base_lgd * lgd_mult, 0.05, 1.00)
            
            # If credit lines are stressed, additional undrawn balance gets utilized
            undrawn = np.maximum(0.0, portfolio_df["credit_limit"] - portfolio_df["current_balance"])
            stressed_ead = base_ead + (undrawn * ead_spike)
            
            # Stressed Expected Loss
            stressed_el = stressed_pd * stressed_lgd * stressed_ead
            total_stressed_el = stressed_el.sum()
            
            # Stressed Capital Requirement (assuming 8% CAR on RWA)
            rwa = stressed_ead * portfolio_df["risk_weight"]
            stressed_cap = (rwa * 0.08).sum()
            
            scenario_summaries.append({
                "Scenario": sc_name,
                "Description": params["desc"],
                "Portfolio Stressed PD (%)": round(stressed_pd.mean() * 100.0, 2),
                "Portfolio Stressed LGD (%)": round(stressed_lgd.mean() * 100.0, 2),
                "Total Stressed EAD ($M)": round(stressed_ead.sum() / 1e6, 2),
                "Expected Loss ($M)": round(total_stressed_el / 1e6, 2),
                "EL Increase vs Baseline ($M)": round((total_stressed_el - (base_pd * base_lgd * base_ead).sum()) / 1e6, 2),
                "EL Increase (%)": round(((total_stressed_el / (base_pd * base_lgd * base_ead).sum()) - 1.0) * 100.0, 1),
                "Required Regulatory Capital ($M)": round(stressed_cap / 1e6, 2)
            })
            
            # Product level breakdown
            df_temp = portfolio_df[["product_type"]].copy()
            df_temp["stressed_el"] = stressed_el
            prod_grp = df_temp.groupby("product_type")["stressed_el"].sum().reset_index()
            prod_grp["Scenario"] = sc_name
            prod_grp["stressed_el_m"] = (prod_grp["stressed_el"] / 1e6).round(2)
            product_breakdowns.append(prod_grp[["Scenario", "product_type", "stressed_el_m"]])
            
        summary_df = pd.DataFrame(scenario_summaries)
        prod_df = pd.concat(product_breakdowns, ignore_index=True)
        return summary_df, prod_df

if __name__ == "__main__":
    from typing import Tuple
    df_with_el = pd.read_csv("data/processed/portfolio_with_expected_loss.csv")
    stress_tester = MacroStressTester()
    summary, prod_stress = stress_tester.run_stress_test(df_with_el)
    
    print("\n--- CCAR / EBA Macroeconomic Stress Testing Results ---")
    print(summary.to_string(index=False))
    
    summary.to_csv("data/reference/macro_stress_test_summary.csv", index=False)
    prod_stress.to_csv("data/reference/product_stress_breakdown.csv", index=False)
