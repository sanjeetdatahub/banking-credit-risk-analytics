'use client';

import React, { useState } from 'react';
import styles from './Contact.module.css';
import { SectionHeader } from '@/components/common/SectionHeader/SectionHeader';
import { LinkedInIcon, GitHubIcon, MailIcon, MapPinIcon, PaperPlaneIcon } from '@/components/common/Icons/Icons';
import { siteConfig } from '@/data/siteConfig';

export function ContactSection() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.name || !formData.email || !formData.message) return;

    setIsSubmitting(true);

    // Simulate reliable dispatch
    setTimeout(() => {
      setIsSubmitting(false);
      setToastMessage(`Thank you ${formData.name}! Your message has been sent to Sanjeet.`);
      setFormData({ name: '', email: '', subject: '', message: '' });

      setTimeout(() => {
        setToastMessage(null);
      }, 4000);
    }, 1200);
  };

  return (
    <section className={`section ${styles.contactSection}`} id="contact">
      <div className="container">
        <SectionHeader
          tag="Get in Touch"
          title="Let's Discuss"
          highlight="Your Data Goals"
          subtitle="Have an opening, a consulting project, or just want to connect over analytics? Reach out anytime!"
        />

        <div className={styles.contactGrid}>
          <div className={styles.contactInfo}>
            <h3>Direct Channels</h3>
            <p>
              I am actively open to full-time Data Analyst, BI Analyst, and Risk Analytics roles, as
              well as freelance data science engagements.
            </p>

            <div className={styles.contactInfoList}>
              <div className={styles.contactInfoItem}>
                <div className={styles.iconBox}>
                  <LinkedInIcon size={20} />
                </div>
                <div className={styles.infoDetails}>
                  <span>LinkedIn Profile</span>
                  <a href={siteConfig.socialLinks.linkedin} target="_blank" rel="noopener noreferrer">
                    linkedin.com/in/sanjeetdatahub
                  </a>
                </div>
              </div>

              <div className={styles.contactInfoItem}>
                <div className={styles.iconBox}>
                  <GitHubIcon size={20} />
                </div>
                <div className={styles.infoDetails}>
                  <span>GitHub Repositories</span>
                  <a href={siteConfig.socialLinks.github} target="_blank" rel="noopener noreferrer">
                    github.com/sanjeetdatahub
                  </a>
                </div>
              </div>

              <div className={styles.contactInfoItem}>
                <div className={styles.iconBox}>
                  <MailIcon size={20} />
                </div>
                <div className={styles.infoDetails}>
                  <span>Email Address</span>
                  <a href={`mailto:${siteConfig.email}`}>{siteConfig.email}</a>
                </div>
              </div>

              <div className={styles.contactInfoItem}>
                <div className={styles.iconBox}>
                  <MapPinIcon size={20} />
                </div>
                <div className={styles.infoDetails}>
                  <span>Location</span>
                  <strong>{siteConfig.location}</strong>
                </div>
              </div>
            </div>
          </div>

          <div className={styles.formContainer}>
            <form onSubmit={handleSubmit}>
              <div className={styles.formGroup}>
                <label htmlFor="contactName">Your Full Name</label>
                <input
                  type="text"
                  id="contactName"
                  className={styles.formControl}
                  placeholder="e.g. Rahul Sharma"
                  required
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                />
              </div>

              <div className={styles.formGroup}>
                <label htmlFor="contactEmail">Email Address</label>
                <input
                  type="email"
                  id="contactEmail"
                  className={styles.formControl}
                  placeholder="name@company.com"
                  required
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                />
              </div>

              <div className={styles.formGroup}>
                <label htmlFor="contactSubject">Subject / Opportunity</label>
                <input
                  type="text"
                  id="contactSubject"
                  className={styles.formControl}
                  placeholder="e.g. Data Analyst Role Inquiry"
                  value={formData.subject}
                  onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                />
              </div>

              <div className={styles.formGroup}>
                <label htmlFor="contactMessage">Message / Project Details</label>
                <textarea
                  id="contactMessage"
                  className={styles.formControl}
                  placeholder="Tell me about your requirements, data stack, or timeline..."
                  required
                  value={formData.message}
                  onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                />
              </div>

              <button
                type="submit"
                className="btn btn-primary"
                style={{ width: '100%' }}
                disabled={isSubmitting}
              >
                <PaperPlaneIcon size={18} />
                {isSubmitting ? 'Sending Message...' : 'Send Message'}
              </button>
            </form>
          </div>
        </div>
      </div>

      {toastMessage && (
        <div className={styles.toast}>
          <span>✅</span>
          <span>{toastMessage}</span>
        </div>
      )}
    </section>
  );
}
