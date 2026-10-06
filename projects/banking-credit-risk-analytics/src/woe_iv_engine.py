"""
Weight of Evidence (WoE) & Information Value (IV) Engine
Industry-standard Credit Scorecard feature engineering & selection mechanism.
Transforms continuous and categorical predictors into risk-monotonic WoE bins.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple

class WoEIVEngine:
    """
    Computes Weight of Evidence (WoE) and Information Value (IV)
    adhering to Basel II Credit Risk Scorecard methodology.
    """
    def __init__(self, target_col: str = "default_flag", n_bins: int = 5):
        self.target_col = target_col
        self.n_bins = n_bins
        self.woe_tables: Dict[str, pd.DataFrame] = {}
        self.bin_edges: Dict[str, np.ndarray] = {}
        self.is_categorical_map: Dict[str, bool] = {}
        self.iv_summary: pd.DataFrame = pd.DataFrame()
        
    def fit_feature(self, df: pd.DataFrame, feature: str, is_categorical: bool = False) -> pd.DataFrame:
        """
        Calculates bin boundaries, Good/Bad counts, WoE, and IV for a single feature.
        """
        self.is_categorical_map[feature] = is_categorical
        target = self.target_col
        total_bads = (df[target] == 1).sum()
        total_goods = (df[target] == 0).sum()
        
        # 1. Binning
        if is_categorical:
            df_binned = df[[feature, target]].copy()
            df_binned["bin"] = df_binned[feature].astype(str)
        else:
            unique_vals = df[feature].nunique()
            if unique_vals <= self.n_bins:
                df_binned = df[[feature, target]].copy()
                df_binned["bin"] = df_binned[feature].astype(str)
                self.is_categorical_map[feature] = True
            else:
                # Compute quantiles with -inf and +inf bounds
                quantiles = np.linspace(0, 1, self.n_bins + 1)
                edges = np.unique(np.quantile(df[feature].dropna(), quantiles))
                edges[0] = -np.inf
                edges[-1] = np.inf
                self.bin_edges[feature] = edges
                
                binned_series = pd.cut(df[feature], bins=edges)
                df_binned = df[[feature, target]].copy()
                df_binned["bin"] = binned_series.astype(str)
                
        # 2. Aggregation
        grouped = df_binned.groupby("bin", observed=True)[target].agg(
            total_count="count",
            bad_count="sum"
        ).reset_index()
        
        grouped["good_count"] = grouped["total_count"] - grouped["bad_count"]
        
        # 3. Handle zero counts with Laplace smoothing (banking standard delta = 0.5)
        grouped["good_count"] = np.where(grouped["good_count"] == 0, 0.5, grouped["good_count"])
        grouped["bad_count"] = np.where(grouped["bad_count"] == 0, 0.5, grouped["bad_count"])
        
        grouped["pct_goods"] = grouped["good_count"] / total_goods
        grouped["pct_bads"] = grouped["bad_count"] / total_bads
        grouped["bad_rate"] = (grouped["bad_count"] / grouped["total_count"]).round(4)
        
        # 4. Weight of Evidence (WoE)
        # Positive WoE implies higher concentration of Goods (lower risk)
        # Negative WoE implies higher concentration of Bads (higher risk)
        grouped["woe"] = np.log(grouped["pct_goods"] / grouped["pct_bads"]).round(4)
        
        # 5. Information Value (IV)
        grouped["iv_component"] = ((grouped["pct_goods"] - grouped["pct_bads"]) * grouped["woe"]).round(5)
        grouped["feature"] = feature
        
        self.woe_tables[feature] = grouped
        return grouped

    def fit_all(self, df: pd.DataFrame, continuous_features: List[str], categorical_features: List[str]) -> pd.DataFrame:
        """
        Fits WoE/IV across all prospective scorecard predictors and produces ranking report.
        """
        iv_records = []
        
        for feat in continuous_features:
            table = self.fit_feature(df, feat, is_categorical=False)
            total_iv = table["iv_component"].sum()
            iv_records.append({"feature": feat, "iv": total_iv, "type": "Continuous"})
            
        for feat in categorical_features:
            table = self.fit_feature(df, feat, is_categorical=True)
            total_iv = table["iv_component"].sum()
            iv_records.append({"feature": feat, "iv": total_iv, "type": "Categorical"})
            
        summary = pd.DataFrame(iv_records).sort_values("iv", ascending=False).reset_index(drop=True)
        
        # Industry Predictive Power Classification
        def classify_iv(val):
            if val < 0.02:
                return "Not Predictive (<0.02) - Exclude"
            elif val < 0.10:
                return "Weak Predictor (0.02-0.10)"
            elif val < 0.30:
                return "Medium Predictor (0.10-0.30) - Retain"
            elif val < 0.50:
                return "Strong Predictor (0.30-0.50) - Prime"
            else:
                return "Suspicious / Potential Leakage (>0.50)"
                
        summary["power_classification"] = summary["iv"].apply(classify_iv)
        self.iv_summary = summary
        return summary

    def transform_to_woe(self, df: pd.DataFrame, selected_features: List[str]) -> pd.DataFrame:
        """
        Replaces raw feature values with their corresponding WoE values.
        """
        transformed = pd.DataFrame(index=df.index)
        
        for feat in selected_features:
            table = self.woe_tables.get(feat)
            if table is None:
                continue
                
            is_cat = self.is_categorical_map.get(feat, False)
            mapping = dict(zip(table["bin"], table["woe"]))
            
            if is_cat:
                transformed[f"{feat}_woe"] = df[feat].astype(str).map(mapping).fillna(0.0)
            else:
                edges = self.bin_edges.get(feat)
                if edges is not None:
                    binned = pd.cut(df[feat], bins=edges)
                    mapped_woe = binned.astype(str).map(mapping)
                    transformed[f"{feat}_woe"] = mapped_woe.fillna(table["woe"].median()).astype(float)
                else:
                    transformed[f"{feat}_woe"] = df[feat].astype(str).map(mapping).fillna(0.0)
                
        return transformed

if __name__ == "__main__":
    train_data = pd.read_csv("data/processed/portfolio_train.csv")
    engine = WoEIVEngine(target_col="default_flag", n_bins=5)
    
    num_cols = ["bureau_credit_score", "debt_to_income_ratio", "revolving_utilization_pct", 
                "inquiries_last_6m", "delinquencies_last_24m", "annual_income", "employment_years"]
    cat_cols = ["product_type", "home_ownership"]
    
    iv_report = engine.fit_all(train_data, num_cols, cat_cols)
    print("\n--- Weight of Evidence (WoE) & Information Value (IV) Report ---")
    print(iv_report.to_string(index=False))
    
    iv_report.to_csv("data/reference/iv_summary_report.csv", index=False)
