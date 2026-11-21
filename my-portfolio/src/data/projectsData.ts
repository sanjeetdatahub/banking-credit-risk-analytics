import { ProjectItem } from '@/types/project';

export const projectsData: ProjectItem[] = [
  {
    id: 'banking-credit-risk',
    title: 'Banking Credit Risk & Loan Portfolio Analytics',
    category: 'Banking & Credit Risk',
    filterCategory: 'banking',
    badge: 'Flagship Risk Project',
    description:
      'Quantitative risk management engine built for commercial lending. Evaluates Probability of Default (PD), Loss Given Default (LGD), Expected Loss (EL), and IFRS 9 multi-stage impairment across 10,000+ credit facilities.',
    thumbnail: '/assets/images/banking/03_roc_auc_curve.png',
    metrics: [
      { label: 'Model Power', value: '88.4% ROC-AUC' },
      { label: 'Capital Protected', value: '$14.2M Mitigated' },
    ],
    techStack: ['Python', 'Scikit-Learn', 'Pandas', 'Seaborn', 'Basel III', 'Stress Testing'],
    caseStudyKey: 'banking',
    githubUrl: 'https://github.com/sanjeetdatahub/banking-credit-risk-analytics',
    pageRoute: '/projects/banking',
  },
  {
    id: 'adidas-sales-analysis',
    title: 'Adidas US Sales Performance & Margin Analytics',
    category: 'Retail & Profitability EDA',
    filterCategory: 'retail',
    badge: 'Commercial Retail Project',
    description:
      'Comprehensive business intelligence analysis across 9,648 retail transactions. Discovered product mix margin dynamics (Apparel 42% vs Footwear 36%), channel efficiencies (In-Store, Outlet, Online), and partner concentration.',
    thumbnail: '/assets/images/adidas/01_total_sales_and_profit_by_product.png',
    metrics: [
      { label: 'Total Revenue', value: '$157.4M Gross' },
      { label: 'Operating Margin', value: '38.2% Average' },
    ],
    techStack: ['Python', 'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Jupyter'],
    caseStudyKey: 'adidas',
    githubUrl: 'https://github.com/sanjeetdatahub/adidas-sales-analysis',
    pageRoute: '/projects/adidas',
  },
  {
    id: 'retail-omnichannel-cockpit',
    title: 'Omnichannel Retail BI Cockpit & Store Analytics',
    category: 'Executive BI Dashboard',
    filterCategory: 'bi',
    description:
      'Multi-dimensional commercial reporting dashboard tracking partner revenue share (Foot Locker, West Gear, Walmart), regional transaction velocity across 50 US states, and seasonal inventory demand swings.',
    thumbnail: '/assets/images/adidas/03_sales_by_region_and_retailer.png',
    metrics: [
      { label: 'US Coverage', value: '50 States' },
      { label: 'Key Partners', value: '6 Retail Chains' },
    ],
    techStack: ['Tableau', 'SQL', 'Excel', 'KPI Modeling'],
    caseStudyKey: 'adidas',
    githubUrl: 'https://github.com/sanjeetdatahub/adidas-sales-analysis',
    pageRoute: '/projects/adidas',
  },
  {
    id: 'loan-delinquency-matrix',
    title: 'Loan Delinquency Roll-Rate & Migration Matrix',
    category: 'Credit Portfolio Risk',
    filterCategory: 'banking',
    description:
      'Markov-chain transition matrix framework tracking loan delinquency migrations between buckets (Current -> 30 DPD -> 60 DPD -> 90+ Default) with macroeconomic scenario stress sensitivity.',
    thumbnail: '/assets/images/banking/05_delinquency_transition_heatmap.png',
    metrics: [
      { label: 'Separation Power', value: '61.2% KS Stat' },
      { label: 'Risk Tiers', value: '5 Calibrated' },
    ],
    techStack: ['Python', 'Markov Chains', 'Seaborn', 'Credit Bureau'],
    caseStudyKey: 'banking',
    githubUrl: 'https://github.com/sanjeetdatahub/banking-credit-risk-analytics',
    pageRoute: '/projects/banking',
  },
];
