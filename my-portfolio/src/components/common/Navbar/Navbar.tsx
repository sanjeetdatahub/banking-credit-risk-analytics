'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import styles from './Navbar.module.css';
import { ThemeToggle } from '../ThemeToggle/ThemeToggle';
import { LinkedInIcon, GitHubIcon, BarsIcon, CloseIcon } from '../Icons/Icons';
import { siteConfig } from '@/data/siteConfig';

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('hero');

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 40);

      const sections = ['hero', 'about', 'skills', 'projects', 'simulator', 'experience', 'contact'];
      for (const sectionId of sections) {
        const el = document.getElementById(sectionId);
        if (el) {
          const rect = el.getBoundingClientRect();
          if (rect.top <= 140 && rect.bottom >= 140) {
            setActiveSection(sectionId);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navItems = [
    { label: 'About', href: '#about', id: 'about' },
    { label: 'Skills', href: '#skills', id: 'skills' },
    { label: 'Projects', href: '#projects', id: 'projects' },
    { label: 'Live Simulator', href: '#simulator', id: 'simulator' },
    { label: 'Timeline', href: '#experience', id: 'experience' },
    { label: 'Contact', href: '#contact', id: 'contact' },
  ];

  return (
    <header className={`${styles.navbar} ${scrolled ? styles.scrolled : ''}`}>
      <div className={`container ${styles.navContainer}`}>
        <Link href="#hero" className={styles.brand}>
          <div className={styles.logoBadge}>SK</div>
          <span>
            Sanjeet<span className="gradient-text">.DataHub</span>
          </span>
        </Link>

        <nav>
          <ul className={styles.navLinks}>
            {navItems.map((item) => (
              <li key={item.id}>
                <a
                  href={item.href}
                  className={`${styles.navLink} ${activeSection === item.id ? styles.active : ''}`}
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <div className={styles.navActions}>
          <a
            href={siteConfig.socialLinks.linkedin}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.socialBtn}
            title="LinkedIn Profile"
            style={{ color: '#0A66C2' }}
          >
            <LinkedInIcon size={18} />
          </a>

          <a
            href={siteConfig.socialLinks.github}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.socialBtn}
            title="GitHub Profile"
          >
            <GitHubIcon size={18} />
          </a>

          <ThemeToggle />

          <a href="#contact" className="btn btn-primary btn-sm">
            Hire Me
          </a>

          <button
            className={styles.mobileToggle}
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Toggle navigation menu"
          >
            {mobileOpen ? <CloseIcon size={24} /> : <BarsIcon size={24} />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      <div className={`${styles.mobileDrawer} ${mobileOpen ? styles.mobileDrawerOpen : ''}`}>
        {navItems.map((item) => (
          <a
            key={item.id}
            href={item.href}
            className={styles.mobileNavLink}
            onClick={() => setMobileOpen(false)}
          >
            {item.label}
          </a>
        ))}
        <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
          <a
            href="#contact"
            className="btn btn-primary"
            style={{ flex: 1 }}
            onClick={() => setMobileOpen(false)}
          >
            Hire Me
          </a>
        </div>
      </div>
    </header>
  );
}
