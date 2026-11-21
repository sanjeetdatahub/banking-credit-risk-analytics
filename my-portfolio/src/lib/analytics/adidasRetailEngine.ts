import { AdidasInputs, AdidasResult } from '@/types/simulator';

/**
 * Pure mathematical calculation engine for Adidas Sales & Margin Projections
 * Derived from the 9,648 US retail transaction benchmark dataset.
 */
export function calculateAdidasProjections(inputs: AdidasInputs): AdidasResult {
  const { category, channel, units } = inputs;

  // Baseline unit pricing & operating margin dynamics
  let unitPrice = category === 'apparel' ? 65.0 : 52.0;
  let marginPct = category === 'apparel' ? 42.2 : 36.1;

  // Channel adjustments based on retail overhead & DTC efficiency
  if (channel === 'outlet') {
    unitPrice *= 0.85; // 15% discount pricing
    marginPct += 0.3;  // lower fixed retail overhead
  } else if (channel === 'online') {
    unitPrice *= 0.95; // digital promotional pricing
    marginPct += 0.5;  // Direct-to-Consumer logistics savings
  }

  const revenue = Math.round(units * unitPrice);
  const profit = Math.round(revenue * (marginPct / 100));

  const channelNames: Record<string, string> = {
    instore: 'In-Store Retail (Flagship & Partner Malls)',
    outlet: 'Outlet Center (Volume & Off-Price Clearing)',
    online: 'Direct-to-Consumer Digital (Adidas App & Web)',
  };

  return {
    revenue,
    profit,
    marginPct: parseFloat(marginPct.toFixed(1)),
    channelName: channelNames[channel] || 'Omnichannel Distribution',
  };
}
