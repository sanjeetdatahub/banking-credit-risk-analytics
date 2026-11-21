'use client';

import React, { useState } from 'react';
import styles from './Simulator.module.css';
import { SectionHeader } from '@/components/common/SectionHeader/SectionHeader';
import { BankingSimulator } from './BankingSimulator';
import { AdidasSimulator } from './AdidasSimulator';

export function SimulatorSection() {
  const [activeTab, setActiveTab] = useState<'banking' | 'adidas'>('banking');

  return (
    <section className={`section ${styles.simulatorSection}`} id="simulator">
      <div className="container">
        <SectionHeader
          tag="Interactive Simulation"
          title="Live Data"
          highlight="Playground"
          subtitle="Test drive my analytical models in real time! Adjust the sliders and parameters below to witness instant quantitative recalculations."
        />

        <div className={styles.playgroundWrapper}>
          <div className={styles.playgroundNav}>
            <button
              className={`${styles.playgroundTab} ${activeTab === 'banking' ? styles.active : ''}`}
              onClick={() => setActiveTab('banking')}
            >
              <span>🏛️</span> Banking Risk Score Simulator
            </button>
            <button
              className={`${styles.playgroundTab} ${activeTab === 'adidas' ? styles.active : ''}`}
              onClick={() => setActiveTab('adidas')}
            >
              <span>👟</span> Adidas Profitability Engine
            </button>
          </div>

          <div className={styles.tabPane}>
            {activeTab === 'banking' ? <BankingSimulator /> : <AdidasSimulator />}
          </div>
        </div>
      </div>
    </section>
  );
}
