import React from 'react';
import Link from 'next/link';
import { caseStudiesData } from '@/data/caseStudiesData';
import { GitHubIcon, LinkedInIcon } from '@/components/common/Icons/Icons';

export const metadata = {
  title: 'Adidas US Sales Performance & Margin Analytics | Sanjeet Kumar',
  description:
    'Comprehensive business intelligence analysis across 9,648 retail transactions and $157M+ gross revenue.',
};

export default function AdidasProjectPage() {
  const data = caseStudiesData.adidas;

  return (
    <div style={{ paddingTop: '7rem', paddingBottom: '6rem' }}>
      <div className="container" style={{ maxWidth: '960px' }}>
        <Link
          href="/#projects"
          className="btn btn-outline btn-sm"
          style={{ marginBottom: '2rem', display: 'inline-flex' }}
        >
          ← Back to Portfolio
        </Link>

        <span className="section-tag">{data.badge}</span>
        <h1
          style={{
            fontFamily: 'var(--font-heading)',
            fontSize: '2.8rem',
            fontWeight: 800,
            lineHeight: 1.2,
            margin: '0.8rem 0 1.5rem',
          }}
        >
          {data.title}
        </h1>

        <div
          style={{
            borderRadius: '16px',
            overflow: 'hidden',
            marginBottom: '2rem',
            border: '1px solid var(--border-light)',
          }}
        >
          <img src={data.image} alt={data.title} style={{ width: '100%' }} />
        </div>

        <p
          style={{
            fontSize: '1.2rem',
            lineHeight: 1.8,
            color: 'var(--text-secondary)',
            marginBottom: '2.5rem',
          }}
        >
          {data.overview}
        </p>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
            gap: '1.2rem',
            marginBottom: '3rem',
          }}
        >
          {data.metrics.map((m, idx) => (
            <div
              key={idx}
              style={{
                background: 'var(--bg-card)',
                border: '1px solid var(--border-light)',
                borderRadius: '14px',
                padding: '1.4rem',
              }}
            >
              <span
                style={{
                  fontSize: '0.78rem',
                  textTransform: 'uppercase',
                  color: 'var(--text-muted)',
                  display: 'block',
                  marginBottom: '0.4rem',
                }}
              >
                {m.label}
              </span>
              <strong
                style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: '1.6rem',
                  color: 'var(--brand-primary)',
                }}
              >
                {m.val}
              </strong>
            </div>
          ))}
        </div>

        <h3
          style={{
            fontFamily: 'var(--font-heading)',
            fontSize: '1.6rem',
            fontWeight: 700,
            marginBottom: '1rem',
            color: 'var(--brand-primary)',
          }}
        >
          🛠️ Engineering & Modeling Methodology:
        </h3>
        <ul
          style={{
            listStyle: 'disc',
            marginLeft: '1.8rem',
            color: 'var(--text-secondary)',
            lineHeight: 1.9,
            marginBottom: '2.5rem',
            fontSize: '1.05rem',
          }}
        >
          {data.technicalSteps.map((step, idx) => (
            <li key={idx}>{step}</li>
          ))}
        </ul>

        <h3
          style={{
            fontFamily: 'var(--font-heading)',
            fontSize: '1.6rem',
            fontWeight: 700,
            marginBottom: '1rem',
            color: 'var(--brand-primary)',
          }}
        >
          📊 Visual Evidence & Analysis:
        </h3>
        <div
          style={{
            borderRadius: '16px',
            overflow: 'hidden',
            margin: '1.5rem 0 2.5rem',
            border: '1px solid var(--border-light)',
          }}
        >
          <img src={data.chartEmbed} alt="Sales method profitability preview" style={{ width: '100%' }} />
        </div>

        <h3
          style={{
            fontFamily: 'var(--font-heading)',
            fontSize: '1.6rem',
            fontWeight: 700,
            marginBottom: '1rem',
            color: 'var(--brand-primary)',
          }}
        >
          💡 Strategic Commercial Impact:
        </h3>
        <p
          style={{
            color: 'var(--text-secondary)',
            lineHeight: 1.8,
            background: 'var(--bg-card)',
            padding: '1.6rem',
            borderRadius: '14px',
            borderLeft: '4px solid var(--brand-primary)',
            fontSize: '1.1rem',
            marginBottom: '3rem',
          }}
        >
          {data.businessImpact}
        </p>

        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <a
            href={data.githubLink}
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-primary"
          >
            <GitHubIcon size={18} /> View GitHub Repository
          </a>
          <a
            href="https://www.linkedin.com/in/sanjeetdatahub"
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-outline"
            style={{ borderColor: '#0A66C2', color: '#0A66C2' }}
          >
            <LinkedInIcon size={18} /> Connect on LinkedIn
          </a>
        </div>
      </div>
    </div>
  );
}
