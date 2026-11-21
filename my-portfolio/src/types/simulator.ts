export interface BorrowerInputs {
  creditScore: number;
  dti: number;
  loanAmount: number;
}

export interface RiskResult {
  pdPct: string;
  expectedLoss: number;
  tier: string;
  status: string;
  meterWidth: number;
  statusType: 'success' | 'warning' | 'danger';
}

export type RetailCategory = 'apparel' | 'footwear';
export type RetailChannel = 'instore' | 'online' | 'outlet';

export interface AdidasInputs {
  category: RetailCategory;
  channel: RetailChannel;
  units: number;
}

export interface AdidasResult {
  revenue: number;
  profit: number;
  marginPct: number;
  channelName: string;
}
