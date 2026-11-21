'use client';

import React from 'react';
import Link from 'next/link';
import styles from './Modal.module.css';
import { useModal } from '@/context/ModalContext';
import { CloseIcon, GitHubIcon, LinkedInIcon, EyeIcon } from '../Icons/Icons';

export function CaseStudyModal() {
  const { isOpen, activeCaseStudy, closeModal } = useModal();

  if (!isOpen || !activeCaseStudy) return null;

  return (
    <div
      className={`${styles.modalOverlay} ${styles.active}`}
      onClick={(e) => {
        if (e.target === e.currentTarget) closeModal();
      }}
      role="dialog"
      aria-modal="true"
      aria-labelledby="modalTitle"
    >
      <div className={styles.modalDialog}>
        <div className={styles.modalHeader}>
          <h3 id="modalTitle">{activeCaseStudy.title}</h3>
          <button
            className={styles.modalCloseBtn}
            onClick={closeModal}
            aria-label="Close modal dialog"
          >
            <CloseIcon size={20} />
          </button>
        </div>

        <div className={styles.modalBody}>
          <div className={styles.modalImageBanner}>
            <img src={activeCaseStudy.image} alt={activeCaseStudy.title} />
          </div>

          <span className="section-tag">{activeCaseStudy.badge}</span>
          <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.8rem', margin: '0.8rem 0' }}>
            {activeCaseStudy.title}
          </h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem', lineHeight: 1.7 }}>
            {activeCaseStudy.overview}
          </p>

          <div className={styles.metricsGrid}>
            {activeCaseStudy.metrics.map((m, idx) => (
              <div key={idx} className={styles.metricCard}>
                <span className={styles.metricLabel}>{m.label}</span>
                <strong className={styles.metricVal}>{m.val}</strong>
              </div>
            ))}
          </div>

          <h4 className={styles.modalSectionTitle}>🛠️ Engineering & Modeling Methodology:</h4>
          <ul className={styles.methodologyList}>
            {activeCaseStudy.technicalSteps.map((step, idx) => (
              <li key={idx}>{step}</li>
            ))}
          </ul>

          <h4 className={styles.modalSectionTitle}>📊 Visual Evidence & Analysis:</h4>
          <div className={styles.chartContainer}>
            <img src={activeCaseStudy.chartEmbed} alt="Visual analytics chart preview" />
          </div>

          <h4 className={styles.modalSectionTitle}>💡 Strategic Commercial Impact:</h4>
          <p className={styles.impactBox}>{activeCaseStudy.businessImpact}</p>

          <div className={styles.modalFooterActions}>
            <a
              href={activeCaseStudy.githubLink}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-primary"
            >
              <GitHubIcon size={18} /> View GitHub Repository
            </a>
            {activeCaseStudy.pageRoute && (
              <Link href={activeCaseStudy.pageRoute} className="btn btn-outline" onClick={closeModal}>
                <EyeIcon size={18} /> Open Dedicated Page
              </Link>
            )}
            <a
              href="https://www.linkedin.com/in/sanjeetdatahub"
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-outline"
              style={{ borderColor: '#0A66C2', color: '#0A66C2' }}
            >
              <LinkedInIcon size={18} /> Connect on LinkedIn
            </a>
            <button className="btn btn-outline" onClick={closeModal}>
              Close Window
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
