import React from 'react';
import { HeroSection } from '@/components/sections/hero/HeroSection';
import { AboutSection } from '@/components/sections/about/AboutSection';
import { SkillsSection } from '@/components/sections/skills/SkillsSection';
import { ProjectsSection } from '@/components/sections/projects/ProjectsSection';
import { SimulatorSection } from '@/components/sections/simulator/SimulatorSection';
import { ExperienceSection } from '@/components/sections/experience/ExperienceSection';
import { ContactSection } from '@/components/sections/contact/ContactSection';

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <AboutSection />
      <SkillsSection />
      <ProjectsSection />
      <SimulatorSection />
      <ExperienceSection />
      <ContactSection />
    </>
  );
}
