import React from 'react';
import styles from './Hero.module.css';
import { ShieldIcon, TrendingUpIcon } from '@/components/common/Icons/Icons';
import { siteConfig } from '@/data/siteConfig';

export function AvatarGlow() {
  return (
    <div className={styles.avatarVisual}>
      <div className={styles.avatarWrapper}>
        <div className={styles.avatarGlowRing} />
        <div className={styles.avatarBorderRing} />
        <div className={styles.avatarContainer}>
          <img
            src={siteConfig.photoPath}
            alt={`${siteConfig.name} - ${siteConfig.role}`}
            id="profileImg"
          />
        </div>

        {/* Floating Badges */}
        <div className={`${styles.floatingBadge} ${styles.badge1}`}>
          <ShieldIcon size={22} style={{ color: 'var(--brand-primary)' }} />
          <div>
            <span>Risk Modeling</span>
            <p style={{ fontSize: '0.7rem', color: 'var(--text-muted)', margin: 0 }}>
              PD / LGD / EAD
            </p>
          </div>
        </div>

        <div className={`${styles.floatingBadge} ${styles.badge2}`}>
          <TrendingUpIcon size={22} style={{ color: 'var(--brand-secondary)' }} />
          <div>
            <span>Retail Intelligence</span>
            <p style={{ fontSize: '0.7rem', color: 'var(--text-muted)', margin: 0 }}>
              Adidas Sales EDA
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
