'use client';

import React, { useState } from 'react';
import styles from './Simulator.module.css';
import { calculateCreditRisk } from '@/lib/analytics/creditRiskEngine';
import { formatCurrency, formatNumber } from '@/utils/formatters';

export function BankingSimulator() {
  const [creditScore, setCreditScore] = useState(710);
  const [dti, setDti] = useState(32);
  const [loanAmount, setLoanAmount] = useState(25000);

  const riskResult = calculateCreditRisk({ creditScore, dti, loanAmount });

  const getMeterColor = () => {
    switch (riskResult.statusType) {
      case 'success':
        return '#10B981';
      case 'warning':
        return '#F59E0B';
      case 'danger':
        return '#EF4444';
      default:
        return 'var(--brand-primary)';
    }
  };

  return (
    <div className={styles.simulatorGrid}>
      <div className={styles.simulatorControls}>
        <h4>
          <span style={{ color: 'var(--brand-primary)' }}>⚙️</span> Adjust Borrower Attributes:
        </h4>

        <div className={styles.controlGroup}>
          <label>
            <span>Borrower FICO / Credit Score:</span>
            <span className={styles.controlValue}>{creditScore}</span>
          </label>
          <input
            type="range"
            className={styles.sliderInput}
            min={500}
            max={850}
            value={creditScore}
            onChange={(e) => setCreditScore(parseInt(e.target.value, 10))}
          />
        </div>

        <div className={styles.controlGroup}>
          <label>
            <span>Debt-to-Income (DTI Ratio %):</span>
            <span className={styles.controlValue}>{dti}%</span>
          </label>
          <input
            type="range"
            className={styles.sliderInput}
            min={5}
            max={65}
            value={dti}
            onChange={(e) => setDti(parseFloat(e.target.value))}
          />
        </div>

        <div className={styles.controlGroup}>
          <label>
            <span>Requested Loan Exposure ($):</span>
            <span className={styles.controlValue}>{formatCurrency(loanAmount)}</span>
          </label>
          <input
            type="range"
            className={styles.sliderInput}
            min={2000}
            max={100000}
            step={1000}
            value={loanAmount}
            onChange={(e) => setLoanAmount(parseInt(e.target.value, 10))}
          />
        </div>
      </div>

      <div className={styles.simulatorResultBox}>
        <h4>
          <span style={{ color: 'var(--brand-primary)' }}>📈</span> Real-Time Risk Calculations:
        </h4>

        <div className={styles.resultKpiRow}>
          <div className={styles.resultKpiCard}>
            <span>Probability of Default (PD)</span>
            <strong>{riskResult.pdPct}%</strong>
          </div>
          <div className={styles.resultKpiCard}>
            <span>Expected Loss (EL = PD * LGD)</span>
            <strong>{formatCurrency(riskResult.expectedLoss)}</strong>
          </div>
        </div>

        <div className={styles.resultKpiCard}>
          <span>Credit Quality Rating Tier</span>
          <strong style={{ color: getMeterColor(), fontSize: '1.3rem' }}>{riskResult.tier}</strong>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginTop: '0.4rem' }}>
            {riskResult.status}
          </p>
          <div className={styles.riskMeterBar}>
            <div
              className={styles.riskMeterFill}
              style={{
                width: `${riskResult.meterWidth}%`,
                backgroundColor: getMeterColor(),
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
