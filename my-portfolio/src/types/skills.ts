export interface SkillCategory {
  id: string;
  title: string;
  iconName: string;
  tags: {
    name: string;
    icon?: string;
  }[];
}

export interface CompetencyScore {
  name: string;
  percentage: number;
}
