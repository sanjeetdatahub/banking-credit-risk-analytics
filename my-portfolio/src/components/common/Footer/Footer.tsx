'use client';

import React from 'react';
import styles from './Footer.module.css';
import { LinkedInIcon, GitHubIcon, MailIcon, ArrowUpIcon } from '../Icons/Icons';
import { siteConfig } from '@/data/siteConfig';

export function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className={styles.footer}>
      <div className="container">
        <div className={styles.footerSocials}>
          <a
            href={siteConfig.socialLinks.linkedin}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.socialBtn}
            title="LinkedIn Profile"
          >
            <LinkedInIcon size={20} />
          </a>

          <a
            href={siteConfig.socialLinks.github}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.socialBtn}
            title="GitHub Repositories"
          >
            <GitHubIcon size={20} />
          </a>

          <a
            href={`mailto:${siteConfig.email}`}
            className={styles.socialBtn}
            title="Send Email"
          >
            <MailIcon size={20} />
          </a>

          <button
            onClick={scrollToTop}
            className={styles.socialBtn}
            title="Back to Top"
            aria-label="Back to Top"
          >
            <ArrowUpIcon size={20} />
          </button>
        </div>

        <p className={styles.copyright}>
          &copy; {new Date().getFullYear()} <strong>{siteConfig.name}</strong> | Built with Precision, Python & Next.js Standards.
        </p>
      </div>
    </footer>
  );
}
