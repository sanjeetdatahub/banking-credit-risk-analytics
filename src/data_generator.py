"""
Synthetic Banking Portfolio Generator
Produces a high-dimensional, realistic retail banking loan portfolio (50,000+ accounts)
adhering to banking statistical distributions, credit risk correlations, and Basel guidelines.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_banking_portfolio(n_records: int = 50000, random_seed: int = 42) -> pd.DataFrame:
    """
    Generates a realistic multi-product retail loan book with correlated risk attributes,
    revolving exposure dynamics, and historical repayment behaviour.
    """
    np.random.seed(random_seed)
    
    # 1. Product Distribution
    products = ["MORTGAGE", "AUTO_LOAN", "PERSONAL_LOAN", "CREDIT_CARD", "SME_WORKING_CAP"]
    product_probs = [0.25, 0.20, 0.25, 0.20, 0.10]
    assigned_products = np.random.choice(products, size=n_records, p=product_probs)
    
    # 2. Borrower Demographics
    age = np.clip(np.random.normal(loc=41, scale=11, size=n_records), 21, 72).astype(int)
    employment_years = np.clip(np.random.exponential(scale=6.5, size=n_records), 0.5, 38).round(1)
    
    home_ownership_choices = ["RENT", "MORTGAGE", "OWN", "OTHER"]
    home_ownership = np.random.choice(home_ownership_choices, size=n_records, p=[0.42, 0.45, 0.11, 0.02])
    
    # Log-normal distribution for Annual Income ($24,000 to $300,000+)
    annual_income = np.exp(np.random.normal(loc=11.1, scale=0.55, size=n_records)).round(-2)
    annual_income = np.clip(annual_income, 18000, 350000)
    
    # 3. Bureau Variables
    # Credit score (correlated with income and age)
    latent_credit = (
        0.30 * (np.log(annual_income) - 11.1) / 0.55 +
        0.20 * (age - 41) / 11 +
        0.15 * (employment_years - 6.5) / 6.5 +
        np.random.normal(0, 0.85, size=n_records)
    )
    bureau_score = np.clip(660 + latent_credit * 65, 350, 850).astype(int)
    
    # Debt-to-Income (DTI) ratio % (negatively correlated with bureau score)
    dti_base = 28 - (bureau_score - 660) * 0.06 + np.random.normal(0, 7.5, size=n_records)
    dti_ratio = np.clip(dti_base, 3.5, 65.0).round(2)
    
    # Revolving Utilization % (strongly inverse to credit score)
    util_base = 45 - (bureau_score - 660) * 0.15 + np.random.normal(0, 18, size=n_records)
    revolving_util = np.clip(util_base, 1.0, 120.0).round(2)
    
    # Recent Credit Inquiries in last 6 months (Poisson distributed)
    inquiries_lambda = np.clip(2.5 - (bureau_score - 600) * 0.008, 0.4, 6.0)
    inquiries_6m = np.random.poisson(lam=inquiries_lambda)
    
    # Delinquencies in last 24 months
    delinq_prob = np.clip(0.35 - (bureau_score - 550) * 0.0018, 0.02, 0.80)
    delinq_24m = (np.random.uniform(0, 1, size=n_records) < delinq_prob).astype(int) * np.random.poisson(1.2, size=n_records)
    
    open_credit_lines = np.clip(np.random.normal(11, 4, size=n_records), 1, 35).astype(int)
    
    # 4. Loan Financial Terms & Balances
    principal_amounts = np.zeros(n_records)
    interest_rates = np.zeros(n_records)
    terms_months = np.zeros(n_records, dtype=int)
    credit_limits = np.zeros(n_records)
    current_balances = np.zeros(n_records)
    
    for i in range(n_records):
        prod = assigned_products[i]
        b_score = bureau_score[i]
        inc = annual_income[i]
        
        # Risk-based pricing spread
        risk_premium = max(0.5, (780 - b_score) * 0.035)
        
        if prod == "MORTGAGE":
            principal = np.clip(inc * np.random.uniform(2.5, 4.5), 80000, 750000)
            rate = 4.2 + risk_premium * 0.4 + np.random.normal(0, 0.3)
            term = np.random.choice([180, 240, 360], p=[0.15, 0.15, 0.70])
            limit = principal
            balance = principal * np.random.uniform(0.40, 0.98)
        elif prod == "AUTO_LOAN":
            principal = np.clip(np.random.normal(32000, 11000), 8000, 85000)
            rate = 5.5 + risk_premium * 0.7 + np.random.normal(0, 0.5)
            term = np.random.choice([36, 48, 60, 72], p=[0.15, 0.25, 0.45, 0.15])
            limit = principal
            balance = principal * np.random.uniform(0.25, 0.95)
        elif prod == "PERSONAL_LOAN":
            principal = np.clip(np.random.normal(16000, 8000), 2000, 50000)
            rate = 8.5 + risk_premium * 1.1 + np.random.normal(0, 0.8)
            term = np.random.choice([24, 36, 48, 60], p=[0.20, 0.40, 0.25, 0.15])
            limit = principal
            balance = principal * np.random.uniform(0.30, 0.95)
        elif prod == "CREDIT_CARD":
            limit = np.clip(inc * np.random.uniform(0.12, 0.35), 1500, 45000)
            principal = limit
            rate = 14.5 + risk_premium * 1.4 + np.random.normal(0, 1.2)
            term = 12 # Revolving annual review
            balance = limit * (revolving_util[i] / 100.0)
        else: # SME_WORKING_CAP
            principal = np.clip(np.random.normal(85000, 35000), 15000, 250000)
            rate = 7.0 + risk_premium * 0.9 + np.random.normal(0, 0.6)
            term = np.random.choice([12, 24, 36], p=[0.4, 0.4, 0.2])
            limit = principal
            balance = limit * np.random.uniform(0.35, 0.92)
            
        principal_amounts[i] = round(principal, 2)
        interest_rates[i] = round(max(2.5, min(rate, 29.9)), 2)
        terms_months[i] = term
        credit_limits[i] = round(limit, 2)
        current_balances[i] = round(min(balance, limit * 1.25), 2)
        
    # 5. Origination & Vintage Generation (2020-2024)
    start_date = datetime(2020, 1, 1)
    origination_offsets = np.random.randint(0, 1800, size=n_records) # Days
    origination_dates = [start_date + timedelta(days=int(off)) for off in origination_offsets]
    
    # Portfolio reporting date: 2024-12-31
    reporting_date = datetime(2024, 12, 31)
    months_on_book = np.array([max(1, int((reporting_date - od).days / 30.4375)) for od in origination_dates])
    
    # 6. Latent Probability of Default (Basel Compliant Log-Odds Formula)
    # Calibrated non-linear default probability
    z_score = (
        -4.10
        - 0.0125 * (bureau_score - 650)
        + 0.038 * (dti_ratio - 30)
        + 0.022 * (revolving_util - 50)
        + 0.28 * inquiries_6m
        + 0.55 * delinq_24m
        - 0.035 * (employment_years - 5)
        + 0.06 * (interest_rates - 10)
        + 0.008 * (months_on_book - 18)
    )
    
    # Add product inherent risk adjustments
    prod_risk = {
        "MORTGAGE": -0.65,
        "AUTO_LOAN": -0.15,
        "PERSONAL_LOAN": +0.35,
        "CREDIT_CARD": +0.55,
        "SME_WORKING_CAP": +0.20
    }
    for p_name, p_adj in prod_risk.items():
        z_score[assigned_products == p_name] += p_adj
        
    true_pd = 1.0 / (1.0 + np.exp(-z_score))
    
    # Assign Default Flag (90+ DPD / Non-accrual)
    random_uniform = np.random.uniform(0, 1, size=n_records)
    default_flag = (random_uniform < true_pd).astype(int)
    
    # Assign Current Days Past Due (DPD) based on default status
    days_past_due = np.zeros(n_records, dtype=int)
    for i in range(n_records):
        if default_flag[i] == 1:
            days_past_due[i] = int(np.random.choice([90, 120, 150, 180, 240], p=[0.35, 0.25, 0.20, 0.12, 0.08]))
        else:
            # 88% completely current (0 DPD), 8% 1-30 DPD, 4% 31-60 DPD
            u = np.random.uniform(0, 1)
            if u < 0.88:
                days_past_due[i] = 0
            elif u < 0.96:
                days_past_due[i] = np.random.randint(1, 30)
            else:
                days_past_due[i] = np.random.randint(31, 89)
                
    # 7. Recovery Amount for Defaults (used for Empirical LGD Estimation)
    recovery_amount = np.zeros(n_records)
    for i in range(n_records):
        if default_flag[i] == 1:
            prod = assigned_products[i]
            bal = current_balances[i]
            if prod == "MORTGAGE":
                rec_rate = np.clip(np.random.normal(0.82, 0.08), 0.50, 0.98)
            elif prod == "AUTO_LOAN":
                rec_rate = np.clip(np.random.normal(0.65, 0.12), 0.30, 0.90)
            elif prod == "PERSONAL_LOAN":
                rec_rate = np.clip(np.random.normal(0.30, 0.10), 0.05, 0.60)
            elif prod == "CREDIT_CARD":
                rec_rate = np.clip(np.random.normal(0.15, 0.07), 0.01, 0.40)
            else:
                rec_rate = np.clip(np.random.normal(0.55, 0.14), 0.15, 0.85)
            recovery_amount[i] = round(bal * rec_rate, 2)
            
    # 8. Compile DataFrame
    df = pd.DataFrame({
        "loan_id": [f"LN-{100000 + i}" for i in range(n_records)],
        "customer_id": [f"CUST-{500000 + (i % 38000)}" for i in range(n_records)],
        "product_type": assigned_products,
        "origination_date": [d.strftime("%Y-%m-%d") for d in origination_dates],
        "origination_year": [d.year for d in origination_dates],
        "months_on_book": months_on_book,
        "loan_term_months": terms_months,
        "interest_rate_pct": interest_rates,
        "principal_amount": principal_amounts,
        "current_balance": current_balances,
        "credit_limit": credit_limits,
        "borrower_age": age,
        "annual_income": annual_income,
        "employment_years": employment_years,
        "home_ownership": home_ownership,
        "debt_to_income_ratio": dti_ratio,
        "bureau_credit_score": bureau_score,
        "revolving_utilization_pct": revolving_util,
        "inquiries_last_6m": inquiries_6m,
        "delinquencies_last_24m": delinq_24m,
        "open_credit_lines": open_credit_lines,
        "days_past_due": days_past_due,
        "default_flag": default_flag,
        "recovery_amount": recovery_amount
    })
    
    return df

if __name__ == "__main__":
    print("Generating enterprise synthetic banking portfolio dataset (50,000 accounts)...")
    portfolio = generate_banking_portfolio(50000)
    out_path = "data/raw/loan_portfolio_raw.csv"
    portfolio.to_csv(out_path, index=False)
    print(f"Successfully generated {len(portfolio):,} loan records.")
    print(f"Default rate: {portfolio['default_flag'].mean()*100:.2f}%")
    print(f"Saved to {out_path}")
