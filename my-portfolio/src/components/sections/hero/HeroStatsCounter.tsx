'use client';

import React, { useEffect, useState, useRef } from 'react';
import styles from './Hero.module.css';
import { siteConfig } from '@/data/siteConfig';

export function HeroStatsCounter() {
  const [counts, setCounts] = useState<number[]>(siteConfig.stats.map(() => 0));
  const hasAnimated = useRef(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        const [entry] = entries;
        if (entry.isIntersecting && !hasAnimated.current) {
          hasAnimated.current = true;

          const duration = 1800;
          const stepTime = 20;
          const steps = duration / stepTime;

          siteConfig.stats.forEach((stat, index) => {
            const increment = stat.target / steps;
            let current = 0;

            const timer = setInterval(() => {
              current += increment;
              if (current >= stat.target) {
                current = stat.target;
                clearInterval(timer);
              }
              setCounts((prev) => {
                const next = [...prev];
                next[index] = current;
                return next;
              });
            }, stepTime);
          });
        }
      },
      { threshold: 0.3 }
    );

    if (containerRef.current) {
      observer.observe(containerRef.current);
    }

    return () => observer.disconnect();
  }, []);

  return (
    <div ref={containerRef} className={styles.heroStats}>
      {siteConfig.stats.map((stat, i) => {
        const val = counts[i];
        const formattedVal =
          stat.target % 1 === 0 ? Math.round(val).toLocaleString() : val.toFixed(1);

        return (
          <div key={i} className={styles.statItem}>
            <h3>
              {stat.prefix}
              {formattedVal}
              {stat.suffix}
            </h3>
            <p>{stat.label}</p>
          </div>
        );
      })}
    </div>
  );
}
