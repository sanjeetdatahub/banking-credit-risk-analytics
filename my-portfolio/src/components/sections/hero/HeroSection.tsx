import React from 'react';
import styles from './Hero.module.css';
import { HeroStatsCounter } from './HeroStatsCounter';
import { AvatarGlow } from './AvatarGlow';
import { ChartPieIcon, LinkedInIcon, GitHubIcon, DownloadIcon } from '@/components/common/Icons/Icons';
import { siteConfig } from '@/data/siteConfig';

export function HeroSection() {
  return (
    <section className={styles.heroSection} id="hero">
      <div className={`container ${styles.heroGrid}`}>
        <div className={styles.heroContent}>
          <div className={styles.pulseBadge}>
            <span className={styles.pulseDot} />
            <span>{siteConfig.status}</span>
          </div>

          <h1 className={styles.heroTitle}>
            Hi, I'm <span className="gradient-text">{siteConfig.name}</span>
          </h1>

          <p className={styles.heroDescription}>
            <strong>Data Analyst & Business Intelligence Specialist</strong> with a passion for
            transforming massive, messy datasets into executive clarity. Proficient in quantitative
            risk modeling, commercial profitability analytics, automated Python pipelines (Pandas,
            NumPy, Seaborn), and high-impact business storytelling.
          </p>

          <div className={styles.heroButtons}>
            <a href="#projects" className="btn btn-primary">
              <ChartPieIcon size={18} /> Explore Projects
            </a>
            <a
              href={siteConfig.socialLinks.linkedin}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-outline"
              style={{ borderColor: '#0A66C2', color: '#0A66C2' }}
            >
              <LinkedInIcon size={18} /> LinkedIn Profile
            </a>
            <a
              href={siteConfig.socialLinks.github}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-outline"
            >
              <GitHubIcon size={18} /> GitHub Profile
            </a>
            <a href={siteConfig.resumePath} download className="btn btn-outline">
              <DownloadIcon size={18} /> Download CV
            </a>
          </div>

          <HeroStatsCounter />
        </div>

        <AvatarGlow />
      </div>
    </section>
  );
}
