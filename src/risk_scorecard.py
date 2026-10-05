"""
Basel II Probability of Default (PD) Scorecard Engine
Implements Logistic Regression on WoE features, FICO-standard Scorecard Scaling (Offset/Factor),
and credit validation metrics: K-S Statistic, Gini Coefficient, ROC-AUC, and Cut-off matrices.
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, List

class LogisticRegressionNumPy:
    """
    High-performance Logistic Regression with L2 Regularization
    implemented natively in NumPy via Vectorized Gradient Descent.
    """
    def __init__(self, lr: float = 0.05, iterations: int = 1200, l2_reg: float = 0.01):
        self.lr = lr
        self.iterations = iterations
        self.l2_reg = l2_reg
        self.weights = None
        self.intercept = 0.0

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-np.clip(z, -25.0, 25.0)))

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.intercept = np.log((y.mean()) / (1.0 - y.mean())) # Smart log-odds intercept start
        
        for _ in range(self.iterations):
            linear_pred = np.dot(X, self.weights) + self.intercept
            y_pred = self._sigmoid(linear_pred)
            
            # Gradients with L2 regularization
            dw = (1.0 / n_samples) * np.dot(X.T, (y_pred - y)) + (self.l2_reg / n_samples) * self.weights
            db = (1.0 / n_samples) * np.sum(y_pred - y)
            
            self.weights -= self.lr * dw
            self.intercept -= self.lr * db
            
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        linear_pred = np.dot(X, self.weights) + self.intercept
        return self._sigmoid(linear_pred)


class CreditScorecard:
    """
    Calibrates PD probabilities into standard 3-digit Credit Scores (300-850)
    using Points to Double the Odds (PDO) formula.
    """
    def __init__(
        self, 
        target_score: float = 660.0, 
        target_odds: float = 25.0, 
        pdo: float = 40.0,
        min_score: int = 300,
        max_score: int = 850
    ):
        self.target_score = target_score
        self.target_odds = target_odds
        self.pdo = pdo
        self.min_score = min_score
        self.max_score = max_score
        
        # Scaling parameters: Score = Offset + Factor * ln(Odds)
        self.factor = pdo / np.log(2.0)
        self.offset = target_score - (self.factor * np.log(target_odds))
        
        self.model = LogisticRegressionNumPy(lr=0.08, iterations=1500, l2_reg=0.02)
        self.feature_names: List[str] = []

    def fit(self, X_woe: pd.DataFrame, y: pd.Series):
        self.feature_names = list(X_woe.columns)
        X_mat = X_woe.values
        y_vec = y.values
        self.model.fit(X_mat, y_vec)

    def predict_pd(self, X_woe: pd.DataFrame) -> np.ndarray:
        return self.model.predict_proba(X_woe[self.feature_names].values)

    def calculate_credit_score(self, pd_prob: np.ndarray) -> np.ndarray:
        """
        Translates PD to Good/Bad Odds and scales to FICO-like credit score.
        Odds = P(Good) / P(Bad) = (1 - PD) / PD
        Score = Offset + Factor * ln(Odds)
        """
        pd_safe = np.clip(pd_prob, 0.0001, 0.9999)
        odds = (1.0 - pd_safe) / pd_safe
        scores = self.offset + (self.factor * np.log(odds))
        return np.clip(scores, self.min_score, self.max_score).round().astype(int)

    def evaluate_model(self, y_true: np.ndarray, y_pred_pd: np.ndarray, scores: np.ndarray) -> Dict[str, float]:
        """
        Computes Basel Regulatory Metrics: ROC-AUC, Gini, and Kolmogorov-Smirnov (K-S) Statistic.
        """
        df_eval = pd.DataFrame({"y": y_true, "pd": y_pred_pd, "score": scores})
        df_eval = df_eval.sort_values("pd", ascending=True).reset_index(drop=True)
        
        n_bad = (df_eval["y"] == 1).sum()
        n_good = (df_eval["y"] == 0).sum()
        
        df_eval["cum_bads"] = (df_eval["y"] == 1).cumsum()
        df_eval["cum_goods"] = (df_eval["y"] == 0).cumsum()
        
        df_eval["cum_bad_rate"] = df_eval["cum_bads"] / n_bad
        df_eval["cum_good_rate"] = df_eval["cum_goods"] / n_good
        
        # 1. K-S Statistic: max separation between cumulative bads and cumulative goods
        df_eval["ks_diff"] = np.abs(df_eval["cum_good_rate"] - df_eval["cum_bad_rate"])
        ks_statistic = df_eval["ks_diff"].max()
        ks_cutoff_row = df_eval.loc[df_eval["ks_diff"].idxmax()]
        
        # 2. ROC-AUC via trapezoidal integration
        df_roc = df_eval.sort_values("pd", ascending=False).reset_index(drop=True)
        df_roc["tpr"] = (df_roc["y"] == 1).cumsum() / n_bad
        df_roc["fpr"] = (df_roc["y"] == 0).cumsum() / n_good
        
        trapz_func = getattr(np, "trapezoid", np.trapz)
        auc = trapz_func(df_roc["tpr"], df_roc["fpr"])
        
        # 3. Gini Coefficient
        gini = (2.0 * auc) - 1.0
        
        return {
            "roc_auc": round(auc, 4),
            "gini_coefficient": round(gini, 4),
            "ks_statistic_pct": round(ks_statistic * 100.0, 2),
            "ks_optimal_score_cutoff": int(ks_cutoff_row["score"]),
            "ks_optimal_pd_cutoff": round(ks_cutoff_row["pd"], 4)
        }

    def generate_cutoff_matrix(self, scores: np.ndarray, y_true: np.ndarray, cutoffs: List[int] = None) -> pd.DataFrame:
        """
        Creates an executive policy approval vs bad rate table across score cutoffs.
        """
        if cutoffs is None:
            cutoffs = [520, 560, 600, 620, 640, 660, 700, 740]
            
        records = []
        total = len(scores)
        
        for cut in cutoffs:
            approved = scores >= cut
            n_app = approved.sum()
            app_rate = (n_app / total) * 100.0
            
            if n_app > 0:
                bad_in_approved = y_true[approved].sum()
                bad_rate_approved = (bad_in_approved / n_app) * 100.0
            else:
                bad_rate_approved = 0.0
                
            rejected = ~approved
            n_rej = rejected.sum()
            if n_rej > 0:
                bad_rate_rejected = (y_true[rejected].sum() / n_rej) * 100.0
            else:
                bad_rate_rejected = 0.0
                
            records.append({
                "Credit Score Cut-off": cut,
                "Approval Rate (%)": round(app_rate, 2),
                "Approved Accounts": n_app,
                "Portfolio Bad Rate in Approvals (%)": round(bad_rate_approved, 2),
                "Rejected Bad Rate (%)": round(bad_rate_rejected, 2)
            })
            
        return pd.DataFrame(records)

if __name__ == "__main__":
    from woe_iv_engine import WoEIVEngine
    
    train_df = pd.read_csv("data/processed/portfolio_train.csv")
    test_df = pd.read_csv("data/processed/portfolio_test.csv")
    
    engine = WoEIVEngine()
    features = ["bureau_credit_score", "debt_to_income_ratio", "revolving_utilization_pct", "inquiries_last_6m"]
    engine.fit_all(train_df, features, [])
    
    X_train_woe = engine.transform_to_woe(train_df, features)
    X_test_woe = engine.transform_to_woe(test_df, features)
    
    scorecard = CreditScorecard()
    scorecard.fit(X_train_woe, train_df["default_flag"])
    
    test_pd = scorecard.predict_pd(X_test_woe)
    test_scores = scorecard.calculate_credit_score(test_pd)
    
    metrics = scorecard.evaluate_model(test_df["default_flag"].values, test_pd, test_scores)
    print("\n--- Model Performance & Discrimination Metrics ---")
    for k, v in metrics.items():
        print(f"{k}: {v}")
        
    cut_matrix = scorecard.generate_cutoff_matrix(test_scores, test_df["default_flag"].values)
    print("\n--- Credit Policy Approval vs Risk Matrix ---")
    print(cut_matrix.to_string(index=False))
