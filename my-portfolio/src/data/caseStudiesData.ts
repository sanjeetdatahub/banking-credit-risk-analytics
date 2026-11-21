import { CaseStudy } from '@/types/project';

export const caseStudiesData: Record<'banking' | 'adidas', CaseStudy> = {
  banking: {
    key: 'banking',
    title: 'Banking Credit Risk & Loan Portfolio Analytics',
    badge: 'Enterprise Risk Modeling & Basel III/IFRS 9',
    image: '/assets/images/banking/03_roc_auc_curve.png',
    overview:
      'An enterprise-grade quantitative credit risk analysis and machine learning framework designed for commercial lending. Evaluates Probability of Default (PD), Loss Given Default (LGD), Exposure at Default (EAD), and Expected Loss (EL) across 10,000+ credit facilities.',
    metrics: [
      { label: 'Model Discriminatory Power', val: '88.4% ROC-AUC' },
      { label: 'Kolmogorov-Smirnov (KS)', val: '61.2% Separation' },
      { label: 'Portfolio Expected Loss', val: '$14.2M Mitigated' },
      { label: 'Risk Tiers Classified', val: '5 Tiers (AAA - Subprime)' },
    ],
    technicalSteps: [
      'Built multi-factor feature store incorporating DTI, revolving utilization, credit age, and macroeconomic indicators.',
      'Trained calibrated Logistic Regression and LightGBM / XGBoost default classifiers with class weighting.',
      'Engineered transition matrices for delinquency migration tracking (Current -> 30DPD -> 60DPD -> 90+ Default).',
      'Conducted 3-scenario macroeconomic stress testing (Baseline, Adverse, Severe Downturn) simulating GDP contraction.',
    ],
    businessImpact:
      'Empowers retail risk managers to adjust underwriting cutoff thresholds dynamically, protecting bank capital reserves under regulatory stress scenarios while expanding loan origination in Prime segments.',
    githubLink: 'https://github.com/sanjeetdatahub/banking-credit-risk-analytics',
    chartEmbed: '/assets/images/banking/01_score_distribution_and_cutoff.png',
    pageRoute: '/projects/banking',
  },
  adidas: {
    key: 'adidas',
    title: 'Adidas US Sales Performance & Profitability Analytics',
    badge: 'Retail Analytics & Commercial Strategy',
    image: '/assets/images/adidas/01_total_sales_and_profit_by_product.png',
    overview:
      'Comprehensive business intelligence pipeline analyzing $157M+ across 9,648 US retail transactions. Unveils key revenue drivers, channel profit margins, partner performance (Foot Locker, Walmart, West Gear), and geographic footprint.',
    metrics: [
      { label: 'Total Gross Revenue', val: '$157.42M' },
      { label: 'Operating Profit', val: '$60.09M' },
      { label: 'Overall Profit Margin', val: '38.17%' },
      { label: 'Apparel vs Footwear Margin', val: '42.0% vs 36.0%' },
    ],
    technicalSteps: [
      'Cleaned raw currency strings, percentages, and commas into verified numeric data types using Pandas.',
      'Engineered temporal features (Month, Year, Quarter, Seasonality) and product category segments.',
      'Computed sales channel efficiency comparing In-store (48% volume) with Online (high margin DTC).',
      'Generated publication-grade Seaborn visualizations (clustered bar charts, donut charts, correlation matrix).',
    ],
    businessImpact:
      'Uncovered counter-intuitive business insight: while footwear drives maximum unit volume, apparel delivers 600 bps higher operating margins (~42% vs 36%), providing strategic justification for bundled cross-selling campaigns.',
    githubLink: 'https://github.com/sanjeetdatahub/adidas-sales-analysis',
    chartEmbed: '/assets/images/adidas/04_sales_method_profitability.png',
    pageRoute: '/projects/adidas',
  },
};
