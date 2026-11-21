import React from 'react';
import styles from './Experience.module.css';
import { SectionHeader } from '@/components/common/SectionHeader/SectionHeader';
import { educationTimeline, experienceTimeline } from '@/data/timelineData';

export function ExperienceSection() {
  return (
    <section className="section" id="experience">
      <div className="container">
        <SectionHeader
          tag="Academic & Professional Journey"
          title="Education &"
          highlight="Experience"
          subtitle="A balanced fusion of Business Analytics education, quantitative risk modeling, and hands-on commercial experience."
        />

        <div className={styles.timelineColumns}>
          {/* Academic Background Column */}
          <div>
            <h3 className={styles.columnHeader} style={{ color: 'var(--brand-primary)' }}>
              <span>🎓</span> Academic Background
            </h3>

            <div className={styles.timeline}>
              {educationTimeline.map((item) => (
                <div key={item.id} className={styles.timelineItem}>
                  <div className={styles.timelineDot} />
                  <div className={styles.timelineCard}>
                    <span className={styles.timelineDate}>{item.period}</span>
                    <h3 className={styles.timelineTitle}>{item.title}</h3>
                    <h4 className={styles.timelineCompany}>{item.institution}</h4>
                    <p className={styles.timelineDescription}>{item.description}</p>
                    {item.tags && (
                      <div className={styles.tagRow}>
                        {item.tags.map((tag, idx) => (
                          <span key={idx} className="tech-tag">
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Work Experience Column */}
          <div>
            <h3 className={styles.columnHeader} style={{ color: 'var(--brand-secondary)' }}>
              <span>💼</span> Work Experience & Projects
            </h3>

            <div className={styles.timeline}>
              {experienceTimeline.map((item) => (
                <div key={item.id} className={styles.timelineItem}>
                  <div className={`${styles.timelineDot} ${styles.dotSecondary}`} />
                  <div className={styles.timelineCard}>
                    <span className={styles.timelineDate} style={{ color: 'var(--brand-secondary)' }}>
                      {item.period}
                    </span>
                    <h3 className={styles.timelineTitle}>{item.title}</h3>
                    <h4 className={styles.timelineCompany}>{item.institution}</h4>
                    <p className={styles.timelineDescription}>{item.description}</p>
                    {item.tags && (
                      <div className={styles.tagRow}>
                        {item.tags.map((tag, idx) => (
                          <span
                            key={idx}
                            className="tech-tag"
                            style={{
                              background: 'rgba(45, 212, 191, 0.1)',
                              color: 'var(--brand-secondary)',
                            }}
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
