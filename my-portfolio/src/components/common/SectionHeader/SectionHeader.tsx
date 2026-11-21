import React from 'react';

interface SectionHeaderProps {
  tag: string;
  title: string;
  highlight: string;
  subtitle: string;
  className?: string;
}

export function SectionHeader({ tag, title, highlight, subtitle, className = '' }: SectionHeaderProps) {
  return (
    <div className={`section-header ${className}`}>
      <span className="section-tag">{tag}</span>
      <h2 className="section-title">
        {title} <span className="gradient-text">{highlight}</span>
      </h2>
      <p className="section-subtitle">{subtitle}</p>
    </div>
  );
}
