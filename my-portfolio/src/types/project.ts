export type ProjectCategory = 'banking' | 'retail' | 'bi' | 'ml';

export interface ProjectMetric {
  label: string;
  value: string;
}

export interface ProjectItem {
  id: string;
  title: string;
  category: string;
  filterCategory: 'banking' | 'retail' | 'bi';
  badge?: string;
  description: string;
  thumbnail: string;
  metrics: ProjectMetric[];
  techStack: string[];
  caseStudyKey: 'banking' | 'adidas';
  githubUrl: string;
  pageRoute?: string;
}

export interface CaseStudyMetric {
  label: string;
  val: string;
}

export interface CaseStudy {
  key: 'banking' | 'adidas';
  title: string;
  badge: string;
  image: string;
  overview: string;
  metrics: CaseStudyMetric[];
  technicalSteps: string[];
  businessImpact: string;
  githubLink: string;
  chartEmbed: string;
  pageRoute: string;
}
