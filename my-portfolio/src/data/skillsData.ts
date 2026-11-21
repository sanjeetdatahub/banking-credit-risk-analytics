import { SkillCategory } from '@/types/skills';

export const skillsCategories: SkillCategory[] = [
  {
    id: 'datascience',
    title: 'Core Data Science & SQL',
    iconName: 'code',
    tags: [
      { name: 'Python (Pandas / NumPy)' },
      { name: 'MySQL Relational DB' },
      { name: 'Data Cleaning & Wrangling' },
      { name: 'Feature Engineering' },
      { name: 'Automated ETL Pipelines' },
      { name: 'Self-Taught Practitioner' },
    ],
  },
  {
    id: 'bi',
    title: 'BI & Statistical Visualization',
    iconName: 'chart',
    tags: [
      { name: 'Tableau Public & Desktop' },
      { name: 'Power BI Dashboards' },
      { name: 'Matplotlib & Seaborn' },
      { name: 'Executive KPI Cockpits' },
      { name: 'Heatmaps & Cohort Matrices' },
      { name: 'Interactive Drilldowns' },
    ],
  },
  // {
  //   id: 'erp',
  //   title: 'Commercial ERP & Inventory',
  //   iconName: 'box',
  //   tags: [
  //     { name: 'Tally ERP 9' },
  //     { name: 'Hotel F&B & Liquor Inventory' },
  //     { name: 'ShawMan POS Reconciliation' },
  //     { name: 'Stock Variance & Shrinkage' },
  //     { name: 'COGS & Margin Auditing' },
  //     { name: 'Bank Account Reconciliation' },
  //   ],
  // },
  {
    id: 'risk',
    title: 'Financial Risk Modeling & ML',
    iconName: 'shield',
    tags: [
      { name: 'Scikit-Learn Machine Learning' },
      { name: 'Probability of Default (PD)' },
      { name: 'Loss Given Default (LGD)' },
      { name: 'Expected Loss (EL) Calculation' },
      { name: 'Logistic Regression & XGBoost' },
      { name: 'Basel III & Stress Testing' },
    ],
  },
  // {
  //   id: 'design',
  //   title: 'Visual Storytelling & UI/UX',
  //   iconName: 'palette',
  //   tags: [
  //     { name: 'Adobe Photoshop' },
  //     { name: 'Adobe Illustrator' },
  //     { name: 'Canva Pro' },
  //     { name: 'CorelDRAW' },
  //     { name: 'Adobe PageMaker' },
  //     { name: 'C-Suite Deck & Infographic Design' },
  //   ],
  // },
  {
    id: 'enterprise',
    title: 'Enterprise Suite & Multimedia',
    iconName: 'laptop',
    tags: [
      { name: 'Advanced MS Excel (XLOOKUP/Pivot)' },
      { name: 'Microsoft Access (Relational DB)' },
      { name: 'Microsoft PowerPoint' },
      { name: 'MS Word & MS Publisher' },
      // { name: 'Video Editing (EDIUS Pro & Filmora)' },
      // { name: 'KineMaster Video Mixing' },
    ],
  },
];
