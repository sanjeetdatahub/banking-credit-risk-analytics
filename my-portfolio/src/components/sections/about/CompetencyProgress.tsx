import React from 'react';
import styles from './About.module.css';
import { siteConfig } from '@/data/siteConfig';

export function CompetencyProgress() {
  return (
    <div className={styles.competencyCard}>
      <h3 className={styles.competencyTitle}>
        <span style={{ color: 'var(--brand-primary)' }}>⚡</span> Quick Competency Summary
      </h3>

      <div className={styles.competencyList}>
        {siteConfig.competencies.map((comp, idx) => (
          <div key={idx}>
            <div className={styles.competencyHeader}>
              <span>{comp.name}</span>
              <span>{comp.percentage}%</span>
            </div>
            <div className={styles.progressBarTrack}>
              <div
                className={styles.progressBarFill}
                style={{ width: `${comp.percentage}%` }}
              />
            </div>
          </div>
        ))}
      </div>

      <div className={styles.quoteCard}>
        <p className={styles.quoteText}>
          &ldquo;A self-taught mindset powered by rigorous MBA business acumen: bridging real-world
          ERP operations with advanced quantitative data science.&rdquo;
        </p>
      </div>
    </div>
  );
}
