export interface TimelineItem {
  id: string;
  period: string;
  title: string;
  institution: string;
  description: string;
  tags?: string[];
  isHighlighted?: boolean;
}
