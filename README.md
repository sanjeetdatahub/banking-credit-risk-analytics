# 💼 Sanjeet Kumar — Data Analytics & Business Intelligence Portfolio Hub

Welcome to the centralized analytics repository and portfolio hub for **Sanjeet Kumar**. This repository contains production-grade data analytics pipelines, statistical modeling systems, executive dashboards, and a fully interactive portfolio web platform.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sanjeet%20Kumar-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanjeetdatahub/)
[![GitHub](https://img.shields.io/badge/GitHub-sanjeetdatahub-181717?logo=github&logoColor=white)](https://github.com/sanjeetdatahub)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Regulatory Accord](https://img.shields.io/badge/Compliance-Basel%20II%2FIII%20%7C%20IFRS--9-green.svg)](#regulatory-framework)
[![Model Discrimination](https://img.shields.io/badge/Model%20Discrimination-ROC--AUC%200.827%20%7C%20Gini%200.654-purple.svg)](#scorecard-performance)
[![Status](https://img.shields.io/badge/Status-Organized%20%26%20Production%20Ready-success)](#)

---

## 🗂️ Clean Workspace Structure

The workspace is organized into two primary pillars:
1. **`my-portfolio/`** — A modern **Next.js 14 App Router + TypeScript** portfolio web application featuring interactive simulators, project showcases, and responsive dual-theme UI.
2. **`projects/`** — Dedicated, self-contained repositories for each data analytics and machine learning project.

```text
banking-credit-risk-analytics/
│
├── my-portfolio/                              # 🌐 Next.js 14 Production Portfolio Web Application
│   ├── src/                                   # TypeScript, App Router, Components & Engines
│   ├── public/                                # Resume, assets, and project visuals
│   ├── package.json                           # Dependencies & run scripts
│   └── README.md                              # Application documentation & setup
│
├── projects/                                  # 📁 Enterprise Data Analytics Projects
│   │
│   ├── banking-credit-risk-analytics/         # 🏦 Banking Credit Risk & Basel II/III Scorecard
│   │   ├── config/                            # Parameter configurations
│   │   ├── data/                              # Raw, processed, and reference portfolios
│   │   ├── notebooks/                         # 01_credit_risk_modeling_walkthrough.ipynb
│   │   ├── reports/                           # Executive risk report & publication figures
│   │   ├── src/                               # WoE/IV, Scorecard, ECL & Stress Testing modules
│   │   ├── requirements.txt                   # Project dependencies
│   │   ├── run_pipeline.py                    # End-to-end execution script
│   │   └── README.md                          # Comprehensive technical documentation
│   │
│   └── adidas-sales-analysis/                 # 👟 Adidas US Sales Performance & Margin BI
│       ├── data/                              # Raw & cleaned transaction datasets
│       ├── notebooks/                         # 01_exploratory_data_analysis.ipynb
│       ├── reports/                           # Executive visualizations & figures
│       ├── src/                               # Data cleaner, EDA insights & visualizers
│       ├── requirements.txt                   # Project dependencies
│       ├── run_analysis.py                    # End-to-end analysis runner
│       └── README.md                          # Business analytics report & documentation
│
├── .gitignore                                 # Workspace-wide ignore rules
└── README.md                                  # Hub overview & navigation guide (this file)
```

---

## 🚀 Projects Overview

### 1. 🏦 Banking Credit Risk & Basel II/III ECL Analytics
- **Domain**: Financial Risk Modeling & Banking Analytics
- **Key Metrics**: **88.4% ROC-AUC**, **62.1% KS Statistic**, **IFRS-9 Multi-Stage Impairment**.
- **Core Components**:
  - Weight of Evidence (WoE) & Information Value (IV) selection
  - Logistic Regression Credit Scorecard calibrated to (600 base score, 20 PDO)
  - Expected Loss ($ECL = PD \times LGD \times EAD$) Engine across 3 economic stress scenarios
  - Vintage Delinquency Curves & Roll-Rate Transition Matrices
- **Quick Run**:
  ```bash
  cd projects/banking-credit-risk-analytics
  python3 -m venv venv && source venv/bin/activate
  pip install -r requirements.txt
  python run_pipeline.py
  ```

---

### 2. 👟 Adidas US Sales & Profitability Analytics
- **Domain**: Retail Omnichannel & Business Intelligence
- **Scale**: $157.4M Gross Sales across 9,648 Transactions across 6 major US retailers.
- **Key Insights**:
  - Apparel drives highest margin rate (42.1%) vs Footwear (36.4%)
  - West Region generated peak revenue ($46.8M) led by Foot Locker
  - In-store vs Online channel margin divergence & seasonal demand surges
- **Quick Run**:
  ```bash
  cd projects/adidas-sales-analysis
  python3 -m venv venv && source venv/bin/activate
  pip install -r requirements.txt
  python run_analysis.py
  ```

---

## 🌐 Personal Portfolio Application (`my-portfolio/`)

A high-performance Next.js 14 + TypeScript web portfolio showcasing live data analytics:

### Features:
- **Dual Themes**: Switch between Cyber Dark Mode and Vibrant Modern Light Mode.
- **Interactive Credit Risk Simulator**: Adjust Debt-to-Income, Delinquencies, and Utilization to calculate default probability and credit tier dynamically.
- **Interactive Retail Margin Simulator**: Test channel mix changes and margin impact in real-time.
- **Modal Case Studies**: View deep-dive problem statements, methodologies, formulas, and chart previews directly.

### How to Run:
```bash
cd my-portfolio
npm install
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 👤 Author & Contact

**Sanjeet Kumar**  
Data Analyst | Business Intelligence & Machine Learning  
- **LinkedIn**: [linkedin.com/in/sanjeetdatahub](https://www.linkedin.com/in/sanjeetdatahub/)  
- **GitHub**: [github.com/sanjeetdatahub](https://github.com/sanjeetdatahub)  
- **Portfolio**: [sanjeetdatahub.github.io](https://sanjeetdatahub.github.io/)
