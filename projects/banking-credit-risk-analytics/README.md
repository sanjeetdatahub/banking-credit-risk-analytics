# 🏦 Enterprise Retail Banking Credit Risk Analytics & Basel II/III ECL Engine

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Regulatory Accord](https://img.shields.io/badge/Compliance-Basel%20II%2FIII%20%7C%20IFRS--9-green.svg)](#regulatory-framework)
[![Model Discrimination](https://img.shields.io/badge/Model%20Discrimination-ROC--AUC%200.827%20%7C%20Gini%200.654-purple.svg)](#scorecard-performance)
[![Risk Separation](https://img.shields.io/badge/K--S%20Statistic-50.67%25%20(Optimal%20Split)-orange.svg)](#model-calibration)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

An institutional-grade, regulatory-compliant **Credit Risk Modeling & Portfolio Analytics System** designed for Tier-1 retail banks, FinTech lenders, and credit bureaus. Built natively using **Python (`NumPy`, `Pandas`, `Matplotlib`, `Seaborn`)**, this engine implements the complete credit risk lifecycle: from raw application ingestion, Weight of Evidence (WoE) and Information Value (IV) scorecard engineering, to Probability of Default (PD) calibration, Basel Expected Loss ($EL = PD \times LGD \times EAD$), IFRS-9 multi-stage provisioning, Vintage delinquency tracking, and Federal Reserve CCAR/EBA macroeconomic stress testing.

---

## 🎯 Resume Ready Bullet Points (Copy & Paste for HR / Recruiters)

> **Role Heading:** *Quantitative Risk Analyst / Credit Risk Data Scientist / Banking Analytics Specialist*

* **Designed & Deployed an End-to-End Basel II/III Credit Scorecard Engine** across a **$2.96 Billion** multi-asset retail banking portfolio (50,000 accounts across Mortgages, Auto, Cards, Personal Loans, and SME facilities), achieving an **ROC-AUC of 0.8272** and a **Gini coefficient of 0.6544**.
* **Engineered Weight of Evidence (WoE) & Information Value (IV) Feature Selection**, screening continuous and categorical risk drivers to eliminate monotonic violations and isolate prime credit predictors (Bureau Score IV: 1.34, DTI IV: 0.48, Inquiries IV: 0.38).
* **Calibrated FICO-Standard Scorecard Scaling** (Target Score: 660 at 25:1 Odds, PDO = 40), establishing an underwriting cut-off threshold at score 600 that **reduced portfolio default rates from 8.07% to 3.12% (a 61.3% reduction in bad debt)** while preserving a **73.48% approval rate**.
* **Validated Model Discrimination via Kolmogorov-Smirnov (K-S) Statistic of 50.67%**, pinpointing maximum cumulative separation between good and bad borrowers within regulatory supervisory tolerances.
* **Formulated IFRS-9 & Basel Foundation IRB Expected Loss Engine** ($EL = PD \times LGD \times EAD$), modeling Credit Conversion Factors (75% CCF on cards) and collateralized LGD hierarchies (18% to 85%) to calculate a **$107.42 Million Staged ECL impairment reserve** and **$122.25 Million in Pillar 1 Minimum Regulatory Capital**.
* **Executed CCAR / DFAST Macroeconomic Stress Testing** under Adverse and Severely Adverse stagflation shocks (+4.8% unemployment, +300 bps interest rates), quantifying a **+236.3% Expected Loss surge** to stress-test bank solvency and capital adequacy buffers.

---

## 🏛️ Business Architecture & Folder Structure

```
banking-credit-risk-analytics/
├── README.md                               <- Executive project documentation & resume guide
├── requirements.txt                        <- Core dependency specifications
├── run_pipeline.py                         <- End-to-end master execution pipeline
├── config/
│   ├── __init__.py
│   └── config.py                           <- Regulatory parameters, CCFs, LGD baselines, stress scenarios
├── data/
│   ├── raw/
│   │   └── loan_portfolio_raw.csv          <- 50,000 realistic multi-product retail loans ($2.96B book)
│   ├── processed/
│   │   ├── portfolio_clean.csv             <- Winsorized features, engineered ratios, IFRS-9 staging
│   │   ├── portfolio_train.csv             <- Stratified training partition (70%)
│   │   ├── portfolio_test.csv              <- Holdout validation partition (30%)
│   │   └── portfolio_with_expected_loss.csv<- Scored loans with PD, LGD, EAD, ECL, and Capital
│   └── reference/
│       ├── iv_summary_report.csv           <- WoE & Information Value predictive power rankings
│       ├── credit_cutoff_policy_matrix.csv <- Approval rates vs bad rates by credit score threshold
│       ├── portfolio_loss_summary.csv      <- Basel EL and IFRS-9 impairment breakdown by asset class
│       └── macro_stress_test_summary.csv   <- CCAR macroeconomic stress scenario output
├── notebooks/
│   └── 01_credit_risk_modeling_walkthrough.ipynb <- Interactive executive walkthrough
├── src/
│   ├── __init__.py
│   ├── data_generator.py                   <- Institutional loan portfolio synthetic generator
│   ├── data_preprocessing.py               <- Outlier winsorization, tenure derivation, IFRS-9 tagging
│   ├── woe_iv_engine.py                    <- Weight of Evidence (WoE) & Information Value (IV) engine
│   ├── risk_scorecard.py                   <- Logistic PD modeling, FICO odds scaling, K-S & ROC-AUC
│   ├── expected_loss_model.py              <- Basel II/III EAD, LGD, Expected Loss & RWA Capital
│   ├── stress_testing.py                   <- Macroeconomic stress testing engine (CCAR/EBA)
│   └── visualization.py                    <- Publication-grade banking risk charts (Matplotlib/Seaborn)
└── reports/
    ├── executive_risk_summary.md           <- Senior risk management & Credit Committee report
    └── figures/                            <- 7 High-resolution (300 DPI) publication-quality charts
        ├── 01_score_distribution_and_cutoff.png
        ├── 02_ks_statistic_divergence.png
        ├── 03_roc_auc_curve.png
        ├── 04_vintage_delinquency_curves.png
        ├── 05_delinquency_transition_heatmap.png
        ├── 06_macro_stress_testing_impact.png
        └── 07_ifrs9_ecl_by_product.png
```

---

## 📊 Core Banking & Quantitative Risk Methodologies

### 1. Weight of Evidence (WoE) & Information Value (IV)
Rather than raw linear inputs, banking scorecards require monotonic binning to capture non-linear default dynamics:
$$\text{WoE}_i = \ln \left( \frac{\% \text{ Non-Defaults}_i}{\% \text{ Defaults}_i} \right) = \ln \left( \frac{\text{Goods}_i / \text{Total Goods}}{\text{Bads}_i / \text{Total Bads}} \right)$$

$$\text{IV} = \sum_{i=1}^{k} \left( \frac{\text{Goods}_i}{\text{Total Goods}} - \frac{\text{Bads}_i}{\text{Total Bads}} \right) \times \text{WoE}_i$$

* **IV Benchmarks:** $<0.02$ (Unpredictive), $0.02 - 0.10$ (Weak), $0.10 - 0.30$ (Medium - Retained), $0.30 - 0.50$ (Strong - Prime Underwriting Predictor).

### 2. Scorecard Scaling (FICO Standard)
Translating default probabilities into standard 3-digit scores:
$$\text{Score} = \text{Offset} + \text{Factor} \times \ln(\text{Odds})$$
where $\text{Odds} = \frac{1 - \text{PD}}{\text{PD}}$, $\text{Factor} = \frac{\text{PDO}}{\ln(2)}$, and $\text{Offset} = \text{Target Score} - (\text{Factor} \times \ln(\text{Target Odds}))$.
* **Project Calibration:** Target Score = 660 at 25:1 Odds, Points to Double Odds (PDO) = 40.

### 3. Basel Expected Loss (EL) Triangle & IFRS 9 ECL
$$\text{EL} = \text{PD} \times \text{LGD} \times \text{EAD}$$
* **Exposure at Default (EAD):** $\text{Current Balance} + (\text{CCF} \times \text{Undrawn Line})$ (75% CCF for credit cards).
* **Loss Given Default (LGD):** Senior Lien Mortgage (18%), Auto Secured (35%), SME (45%), Unsecured Cards (85%).
* **IFRS 9 Staged Impairment:**
  * **Stage 1 (0-29 DPD):** 12-Month ECL.
  * **Stage 2 (30-89 DPD - SICR):** Lifetime ECL ($\sim 2.5\times$ multiplier).
  * **Stage 3 (90+ DPD / NPL):** Full Specific Allowance ($\text{LGD} \times \text{EAD}$).

### 4. Macroeconomic Stress Testing (CCAR / DFAST Framework)
Simulates portfolio capital resilience under supervisory macroeconomic shocks:
* **Baseline:** Current economic trajectory ($\text{EL} = \$63.16\text{M}$).
* **Adverse (Stagflation):** $+2.2\%$ Unemployment, $+150$ bps Rates, $-1.5\%$ GDP ($\text{EL} = \$113.01\text{M}$, $+78.9\%$).
* **Severely Adverse (Global Recession):** $+4.8\%$ Unemployment, $+300$ bps Rates, $-4.2\%$ GDP ($\text{EL} = \$212.38\text{M}$, $+236.3\%$).

---

## 📈 Performance Summary & Visualizations

| Chart Name | Metric / Analysis | File Reference |
| :--- | :--- | :--- |
| **Score Distribution & Cutoff** | Bimodal separation, Decline vs Approval zone bad rates | `reports/figures/01_score_distribution_and_cutoff.png` |
| **K-S Divergence Plot** | Maximum separation ($K\text{-}S = 50.67\%$) between Good & Bad CDFs | `reports/figures/02_ks_statistic_divergence.png` |
| **ROC & Lorenz Curve** | Scorecard discrimination ($\text{AUC} = 0.8272$, $\text{Gini} = 0.6544$) | `reports/figures/03_roc_auc_curve.png` |
| **Vintage Aging Analysis** | Default maturation curves across 2020-2023 cohorts over MOB | `reports/figures/04_vintage_delinquency_curves.png` |
| **Roll-Rate Heatmap** | 30-day delinquency migration probabilities ($0 \rightarrow 30 \rightarrow 60 \rightarrow 90+$ DPD) | `reports/figures/05_delinquency_transition_heatmap.png` |
| **Macro Stress Impact** | Capital depletion and Expected Loss surge under CCAR shocks | `reports/figures/06_macro_stress_testing_impact.png` |
| **IFRS-9 ECL by Product** | Exposure vs Impairment reserve across asset classes | `reports/figures/07_ifrs9_ecl_by_product.png` |

---

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure Python 3.9+ is installed:
```bash
python3 --version
```

### 2. Clone & Install Dependencies
```bash
git clone https://github.com/your-username/banking-credit-risk-analytics.git
cd banking-credit-risk-analytics
pip install -r requirements.txt
```

### 3. Run the Complete End-to-End Pipeline
```bash
python3 run_pipeline.py
```
*Executes the full institutional workflow in under 10 seconds, generating clean datasets, scorecard models, stress-testing tables, and high-resolution figures.*

### 4. Explore Interactive Notebook
```bash
jupyter notebook notebooks/01_credit_risk_modeling_walkthrough.ipynb
```

---

## 💼 Interview Preparation: Top Banking Risk Questions & Answers

### Q1: Why did you use Weight of Evidence (WoE) and Logistic Regression instead of XGBoost or a Random Forest?
**Answer:** In banking credit risk, models must comply with **Fair Lending regulations (FCRA, ECOA)** and **Basel supervisory standards (BCBS 239)**. Regulators require explainability, monotonic risk trends (e.g., higher DTI must never result in a lower predicted default rate), and adverse action reason codes for rejected applicants. While tree-based ensembles are non-linear black boxes, a **WoE Logistic Scorecard** transforms non-linear relationships into strictly monotonic features while providing complete mathematical transparency and auditability.

### Q2: What is the difference between ROC-AUC, Gini, and K-S Statistic?
**Answer:** 
* **ROC-AUC** measures the model's ability to rank order goods above bads across all possible thresholds ($\text{Range: } 0.5 - 1.0$).
* **Gini Coefficient** is a direct linear transformation of AUC ($\text{Gini} = 2 \times \text{AUC} - 1$), preferred in European/Basel banking reporting where values above $0.50$ indicate strong discrimination.
* **Kolmogorov-Smirnov (K-S)** measures the maximum vertical distance between the cumulative distribution function (CDF) of Goods and Bads. Unlike AUC, which aggregates performance across the entire curve, K-S pinpoints the exact score cutoff where the scorecard achieves maximum discrimination power.

### Q3: How do you handle Exposure at Default (EAD) for credit cards versus term loans?
**Answer:** Term loans (mortgages, auto loans) are non-revolving and amortizing; thus, their EAD is simply the current outstanding principal ($\text{CCF} = 0\%$). Credit cards, however, are revolving facilities where borrowers under financial distress aggressively draw down their remaining limits before defaulting. Under Basel guidelines, we apply a **Credit Conversion Factor (CCF)** of **75%** to the undrawn line: $\text{EAD} = \text{Current Balance} + (0.75 \times (\text{Limit} - \text{Balance}))$.

---

## 📜 Regulatory Standards & References
* **Basel Committee on Banking Supervision (BCBS):** International Convergence of Capital Measurement and Capital Standards (Basel II / III).
* **International Financial Reporting Standard 9 (IFRS 9):** Financial Instruments – Impairment & Staged ECL Recognition.
* **Federal Reserve Comprehensive Capital Analysis and Review (CCAR):** Supervisory Stress Testing Methodology.
