'use client';

import React, { useState } from 'react';
import styles from './Simulator.module.css';
import { calculateAdidasProjections } from '@/lib/analytics/adidasRetailEngine';
import { RetailCategory, RetailChannel } from '@/types/simulator';
import { formatCurrency, formatNumber } from '@/utils/formatters';

export function AdidasSimulator() {
  const [category, setCategory] = useState<RetailCategory>('apparel');
  const [channel, setChannel] = useState<RetailChannel>('instore');
  const [units, setUnits] = useState(5000);

  const result = calculateAdidasProjections({ category, channel, units });

  return (
    <div className={styles.simulatorGrid}>
      <div className={styles.simulatorControls}>
        <h4>
          <span style={{ color: 'var(--brand-primary)' }}>🛍️</span> Configure Retail Scenario:
        </h4>

        <div className={styles.controlGroup}>
          <label>Product Line Segment:</label>
          <select
            className={styles.selectInput}
            value={category}
            onChange={(e) => setCategory(e.target.value as RetailCategory)}
          >
            <option value="apparel">Apparel (Women's & Men's High-Margin Lines)</option>
            <option value="footwear">Footwear (Street & Athletic Shoes)</option>
          </select>
        </div>

        <div className={styles.controlGroup}>
          <label>Sales Method / Channel:</label>
          <select
            className={styles.selectInput}
            value={channel}
            onChange={(e) => setChannel(e.target.value as RetailChannel)}
          >
            <option value="instore">In-Store Retail Flagship</option>
            <option value="online">Online Direct-to-Consumer (DTC)</option>
            <option value="outlet">Outlet Centers (Discount/Volume)</option>
          </select>
        </div>

        <div className={styles.controlGroup}>
          <label>
            <span>Projected Units Sold:</span>
            <span className={styles.controlValue}>{formatNumber(units)}</span>
          </label>
          <input
            type="range"
            className={styles.sliderInput}
            min={500}
            max={50000}
            step={500}
            value={units}
            onChange={(e) => setUnits(parseInt(e.target.value, 10))}
          />
        </div>
      </div>

      <div className={styles.simulatorResultBox}>
        <h4>
          <span style={{ color: 'var(--brand-primary)' }}>💰</span> Financial Projections:
        </h4>

        <div className={styles.resultKpiRow}>
          <div className={styles.resultKpiCard}>
            <span>Gross Sales Revenue</span>
            <strong>{formatCurrency(result.revenue)}</strong>
          </div>
          <div className={styles.resultKpiCard}>
            <span>Net Operating Profit</span>
            <strong>{formatCurrency(result.profit)}</strong>
          </div>
        </div>

        <div className={styles.resultKpiCard}>
          <span>Operating Margin %</span>
          <strong style={{ color: '#2DD4BF' }}>{result.marginPct}%</strong>
          <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginTop: '0.4rem' }}>
            {result.channelName}
          </p>
        </div>
      </div>
    </div>
  );
}
