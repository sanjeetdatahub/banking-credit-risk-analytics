"""
Configuration and Regulatory Parameters
Basel II / III Credit Risk Analytics & IFRS-9 ECL Engine
"""

# Scorecard Calibration Parameters
SCORECARD_CONFIG = {
    "target_score": 600,       # Base score
    "target_odds": 50.0,       # Target Odds (Good : Bad = 50:1 at 600 score)
    "pdo": 20.0,               # Points to Double the Odds
    "min_score": 300,          # Floor score
    "max_score": 850,          # Ceiling score
    "default_definition_dpd": 90 # 90+ Days Past Due defines default under Basel
}

# Basel Credit Conversion Factors (CCF) for EAD Calculation
CREDIT_CONVERSION_FACTORS = {
    "MORTGAGE": 0.0,        # Fully drawn term loan
    "AUTO_LOAN": 0.0,       # Term loan
    "PERSONAL_LOAN": 0.10,  # Small overdraft line
    "CREDIT_CARD": 0.75,    # Basel standard 75% CCF for committed revolving lines
    "SME_WORKING_CAP": 0.50 # 50% CCF for SME credit facilities
}

# Basel Loss Given Default (LGD) Baselines by Product (Foundation IRB)
BASELINE_LGD = {
    "MORTGAGE": 0.18,       # High collateral recovery (senior residential lien)
    "AUTO_LOAN": 0.35,      # Depreciating collateral (vehicle repossession)
    "PERSONAL_LOAN": 0.70,  # Unsecured consumer debt
    "CREDIT_CARD": 0.85,    # Fully unsecured revolving debt
    "SME_WORKING_CAP": 0.45 # Mixed asset-backed collateral
}

# IFRS 9 Staging Thresholds (Significant Increase in Credit Risk - SICR)
IFRS9_STAGES = {
    "STAGE_1": {"desc": "Performing (12-Month ECL)", "max_dpd": 30, "pd_increase_factor": 1.0},
    "STAGE_2": {"desc": "Underperforming / SICR (Lifetime ECL)", "min_dpd": 31, "max_dpd": 89, "pd_increase_factor": 2.5},
    "STAGE_3": {"desc": "Non-Performing / Default (Credit Impaired)", "min_dpd": 90, "pd_increase_factor": 1.0}
}

# Macroeconomic Stress Testing Scenarios (Federal Reserve CCAR / EBA style)
MACRO_STRESS_SCENARIOS = {
    "BASELINE": {
        "scenario_name": "Baseline Macro Economic Path",
        "unemployment_shock_pct": 0.0,
        "interest_rate_shock_bps": 0,
        "gdp_contraction_pct": 0.0,
        "pd_multiplier": 1.0,
        "lgd_multiplier": 1.0
    },
    "ADVERSE": {
        "scenario_name": "Moderate Stagflation Shock",
        "unemployment_shock_pct": +2.2,
        "interest_rate_shock_bps": +150,
        "gdp_contraction_pct": -1.5,
        "pd_multiplier": 1.45,
        "lgd_multiplier": 1.15
    },
    "SEVERELY_ADVERSE": {
        "scenario_name": "Severe Global Recession & Credit Crunch",
        "unemployment_shock_pct": +4.8,
        "interest_rate_shock_bps": +300,
        "gdp_contraction_pct": -4.2,
        "pd_multiplier": 2.30,
        "lgd_multiplier": 1.35
    }
}
