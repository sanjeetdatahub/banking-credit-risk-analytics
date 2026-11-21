import React from 'react';
import Link from 'next/link';
import { SimulatorSection } from '@/components/sections/simulator/SimulatorSection';

export const metadata = {
  title: 'Live Analytics Simulator & Risk Playground | Sanjeet Kumar',
  description:
    'Test drive real-time predictive models: Banking Credit Risk Score Simulator & Adidas Retail Profitability Engine.',
};

export default function SimulatorPage() {
  return (
    <div style={{ paddingTop: '6rem', minHeight: '85vh' }}>
      <div className="container" style={{ marginBottom: '1.5rem' }}>
        <Link href="/" className="btn btn-outline btn-sm">
          ← Back to Portfolio
        </Link>
      </div>
      <SimulatorSection />
    </div>
  );
}
