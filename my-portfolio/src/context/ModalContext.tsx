'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { CaseStudy } from '@/types/project';
import { caseStudiesData } from '@/data/caseStudiesData';

interface ModalContextType {
  isOpen: boolean;
  activeCaseStudy: CaseStudy | null;
  openCaseStudy: (key: 'banking' | 'adidas') => void;
  closeModal: () => void;
}

const ModalContext = createContext<ModalContextType | undefined>(undefined);

export function ModalProvider({ children }: { children: React.ReactNode }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeCaseStudy, setActiveCaseStudy] = useState<CaseStudy | null>(null);

  const openCaseStudy = (key: 'banking' | 'adidas') => {
    const study = caseStudiesData[key];
    if (study) {
      setActiveCaseStudy(study);
      setIsOpen(true);
    }
  };

  const closeModal = () => {
    setIsOpen(false);
    setActiveCaseStudy(null);
  };

  // Lock body scroll and listen for ESC key when modal is open
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen) {
        closeModal();
      }
    };

    if (isOpen) {
      document.body.style.overflow = 'hidden';
      window.addEventListener('keydown', handleKeyDown);
    } else {
      document.body.style.overflow = 'auto';
    }

    return () => {
      document.body.style.overflow = 'auto';
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [isOpen]);

  return (
    <ModalContext.Provider value={{ isOpen, activeCaseStudy, openCaseStudy, closeModal }}>
      {children}
    </ModalContext.Provider>
  );
}

export function useModal() {
  const context = useContext(ModalContext);
  if (!context) {
    throw new Error('useModal must be used within a ModalProvider');
  }
  return context;
}
