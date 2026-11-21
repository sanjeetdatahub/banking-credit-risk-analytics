'use client';

import React from 'react';
import styles from './Projects.module.css';
import { ProjectItem } from '@/types/project';
import { useModal } from '@/context/ModalContext';
import { EyeIcon, GitHubIcon } from '@/components/common/Icons/Icons';

export function ProjectCard({ project }: { project: ProjectItem }) {
  const { openCaseStudy } = useModal();

  return (
    <div className={styles.projectCard}>
      {project.badge && <div className={styles.projectBadgeTop}>{project.badge}</div>}

      <div className={styles.projectThumbnail}>
        <img src={project.thumbnail} alt={project.title} />
      </div>

      <div className={styles.projectBody}>
        <span className={styles.projectCategory}>{project.category}</span>
        <h3 className={styles.projectTitle}>{project.title}</h3>
        <p className={styles.projectDescription}>{project.description}</p>

        <div className={styles.metricsGrid}>
          {project.metrics.map((m, idx) => (
            <div key={idx} className={styles.metricBox}>
              <span>{m.label}</span>
              <strong>{m.value}</strong>
            </div>
          ))}
        </div>

        <div className={styles.techStack}>
          {project.techStack.map((tech, idx) => (
            <span key={idx} className="tech-tag">
              {tech}
            </span>
          ))}
        </div>

        <div className={styles.projectFooter}>
          <button
            onClick={() => openCaseStudy(project.caseStudyKey)}
            className="btn btn-primary btn-sm"
          >
            <EyeIcon size={16} /> View Case Study
          </button>
          <a
            href={project.githubUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-outline btn-sm"
          >
            <GitHubIcon size={16} /> GitHub Code
          </a>
        </div>
      </div>
    </div>
  );
}
