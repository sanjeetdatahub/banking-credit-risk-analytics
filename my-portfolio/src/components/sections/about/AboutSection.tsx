import React from 'react';
import styles from './About.module.css';
import { SectionHeader } from '@/components/common/SectionHeader/SectionHeader';
import { CompetencyProgress } from './CompetencyProgress';

export function AboutSection() {
  const highlights = [
    {
      icon: '🏛️',
      title: 'Banking & Risk',
      description: 'Default Probability, Stress Testing & Expected Loss.',
    },
    {
      icon: '📦',
      title: 'Commercial ERP & Inventory',
      description: 'Tally ERP 9, F&B/Liquor Auditing & POS Reconciliation.',
    },
    {
      icon: '🐍',
      title: 'Self-Taught Python & SQL',
      description: 'Independent mastery of MySQL, Pandas & ML Pipelines.',
    },
    {
      icon: '🎨',
      title: 'Executive UI/UX Design',
      description: 'Photoshop, Illustrator, Canva & Tableau C-Suite Decks.',
    },
  ];

  return (
    <section className="section" id="about">
      <div className="container">
        <SectionHeader
          tag="About Me"
          title="Bridging Data Science with"
          highlight="Business Strategy"
          subtitle="I don't just calculate numbers; I extract commercial leverage, mitigate financial risk, and discover untapped margin opportunities."
        />

        <div className={styles.aboutGrid}>
          <div className={styles.aboutContent}>
            <p>
              I am a <strong>self-taught data analytics enthusiast</strong> pursuing an
              <strong> MBA in Business Analytics</strong> from Manipal University Jaipur.
              I have skills in <strong>Python, Pandas, NumPy, MySQL, Tableau, and Excel</strong>,
              developed through self-learning and practical projects.
            </p>

            <p>
              I have hands-on experience in <strong>restaurant operations, sales reporting,
                inventory management, and financial reconciliation</strong>. I enjoy analyzing
              data, creating interactive dashboards, and using business insights to support
              <strong>better decision-making</strong>.
            </p>
            <div className={styles.highlightsGrid}>
              {highlights.map((item, idx) => (
                <div key={idx} className={styles.highlightCard}>
                  <div className={styles.highlightIcon}>{item.icon}</div>
                  <div className={styles.highlightInfo}>
                    <h4>{item.title}</h4>
                    <p>{item.description}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <CompetencyProgress />
        </div>
      </div>
    </section>
  );
}
