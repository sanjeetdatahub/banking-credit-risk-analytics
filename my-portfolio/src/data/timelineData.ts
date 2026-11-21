import { TimelineItem } from '@/types/timeline';

export const educationTimeline: TimelineItem[] = [
  {
    id: 'edu-mba',
    period: '2026 — 2028 (Pursuing)',
    title: 'Master of Business Administration (MBA)',
    institution: 'Manipal University Jaipur (Online Manipal)',
    description:
      'Specialization in Business Analytics & Data-Driven Decision Making. Developing advanced competencies in business strategy, financial modeling, KPI performance measurement, managerial statistics, and organizational leadership.',
    tags: ['Business Analytics', 'Data-Driven Strategy', 'KPI Management'],
    isHighlighted: true,
  },
  {
    id: 'edu-ba',
    period: '2017 — 2020',
    title: 'Bachelor of Arts (B.A. Hons) — Political Science',
    institution: 'Lalit Narayan Mithila University (LNMU), Darbhanga (Bihar)',
    description:
      'Developed strong critical thinking, qualitative & quantitative analytical reasoning, institutional governance, public policy analysis, and structured research methodologies.',
    tags: ['Research & Analysis', 'Critical Reasoning'],
  },
  {
    id: 'edu-intermediate',
    period: '2015 — 2017',
    title: 'Intermediate (12th) — Science (Mathematics)',
    institution: 'Bihar School Examination Board (BSEB), Patna',
    description:
      'Rigorous foundational education in Mathematics, Physics, Chemistry, and numerical problem solving.',
  },
];

export const experienceTimeline: TimelineItem[] = [
  {
    id: 'exp-datahub',
    period: '2024 — Present',
    title: 'Data Analyst & Analytics Researcher',
    institution: 'DataHub Analytics Showcase',
    description:
      'Spearheading end-to-end data analytics pipelines in Python (Pandas, NumPy, Seaborn) and SQL. Engineered Banking Credit Risk default models (88.4% ROC-AUC) and commercial retail profitability engines across $157M+ transaction benchmarks.',
    tags: ['Python', 'Credit Risk', 'Tableau'],
    isHighlighted: true,
  },
  {
    id: 'exp-savaaser',
    period: 'Oct 2021 — Dec 2023',
    title: 'Cashier & Commercial Inventory Specialist',
    institution: 'Savaa Ser Pvt. Ltd. (LUPA Bengaluru)',
    description:
      'Directed daily high-volume digital & POS settlements, ShawMan software data reconciliation, and comprehensive Food & Beverage (F&B) and liquor inventory auditing. Resolved daily physical stock variances, tracked shrinkage & wastage metrics, and generated executive Excel revenue reconciliation reports.',
    tags: [
      'F&B & Liquor Inventory',
      'ShawMan POS',
      'Advanced Excel',
      'Stock Variance',
      'Financial Reconciliation',
    ],
  },
  {
    id: 'exp-subhalakshmi',
    period: '2017 — 2018',
    title: 'Assistant Accountant & ERP Operator',
    institution: 'Subha Lakshmi Pvt. Ltd., Madhwapur (Bihar)',
    description:
      'Managed Tally ERP 9 accounting ledgers (Sales, Purchases, Cash/Bank Vouchers, Invoices), prepared monthly balance sheet schedules, reconciled commercial bank statements, and maintained physical goods inventory registers.',
    tags: ['Tally ERP 9', 'Bank Reconciliation', 'Stock Ledger', 'Financial Reporting'],
  },
];
