import React from 'react';
import styles from './Skills.module.css';
import { SectionHeader } from '@/components/common/SectionHeader/SectionHeader';
import { skillsCategories } from '@/data/skillsData';

export function SkillsSection() {
  const getCategoryIcon = (id: string) => {
    switch (id) {
      case 'datascience':
        return '🐍';
      case 'bi':
        return '📊';
      case 'erp':
        return '📦';
      case 'risk':
        return '🛡️';
      case 'design':
        return '🎨';
      case 'enterprise':
        return '💻';
      default:
        return '⚡';
    }
  };

  return (
    <section className={`section ${styles.skillsSection}`} id="skills">
      <div className="container">
        <SectionHeader
          tag="Technical & Operational Competencies"
          title="The Comprehensive"
          highlight="Analytical Toolkit"
          subtitle="A balanced multi-disciplinary stack spanning quantitative data science, commercial ERP operations, and executive visual design."
        />

        <div className={styles.skillsGrid}>
          {skillsCategories.map((cat) => (
            <div key={cat.id} className={styles.skillCategoryCard}>
              <div className={styles.categoryHeader}>
                <div className={styles.categoryIcon}>{getCategoryIcon(cat.id)}</div>
                <h3>{cat.title}</h3>
              </div>

              <div className={styles.skillPills}>
                {cat.tags.map((tag, idx) => (
                  <span key={idx} className={styles.skillPill}>
                    {tag.name}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
