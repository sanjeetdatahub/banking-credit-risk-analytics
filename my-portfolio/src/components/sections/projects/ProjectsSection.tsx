'use client';

import React, { useState } from 'react';
import styles from './Projects.module.css';
import { SectionHeader } from '@/components/common/SectionHeader/SectionHeader';
import { ProjectCard } from './ProjectCard';
import { projectsData } from '@/data/projectsData';

type FilterType = 'all' | 'banking' | 'retail' | 'bi';

export function ProjectsSection() {
  const [activeFilter, setActiveFilter] = useState<FilterType>('all');

  const filteredProjects = projectsData.filter((project) => {
    if (activeFilter === 'all') return true;
    return project.filterCategory === activeFilter;
  });

  const filterButtons: { label: string; value: FilterType }[] = [
    { label: 'All Projects', value: 'all' },
    { label: 'Banking & Risk Analytics', value: 'banking' },
    { label: 'Retail & Sales Intelligence', value: 'retail' },
    { label: 'BI & Dashboards', value: 'bi' },
  ];

  return (
    <section className="section" id="projects">
      <div className="container">
        <SectionHeader
          tag="Portfolio Highlights"
          title="Featured"
          highlight="Analytics Projects"
          subtitle="Real-world end-to-end case studies covering financial risk modeling and retail profitability."
        />

        <div className={styles.projectFilters}>
          {filterButtons.map((btn) => (
            <button
              key={btn.value}
              className={`${styles.filterBtn} ${activeFilter === btn.value ? styles.active : ''}`}
              onClick={() => setActiveFilter(btn.value)}
            >
              {btn.label}
            </button>
          ))}
        </div>

        <div className={styles.projectsGrid}>
          {filteredProjects.map((project) => (
            <ProjectCard key={project.id} project={project} />
          ))}
        </div>
      </div>
    </section>
  );
}
