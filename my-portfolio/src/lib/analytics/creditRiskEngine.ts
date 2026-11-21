import { BorrowerInputs, RiskResult } from '@/types/simulator';

/**
 * Pure mathematical calculation engine for Banking Credit Risk
 * Evaluates empirical logistic probability of default and expected loss.
 */
export function calculateCreditRisk(inputs: BorrowerInputs): RiskResult {
  const { creditScore, dti, loanAmount } = inputs;

  // Empirical logistic approximation formula for Probability of Default (PD)
  // Base log-odds adjusted by FICO score and Debt-To-Income (DTI) ratio
  const z = 4.2 - (0.01 * creditScore) + (0.045 * dti);
  const pd = 1 / (1 + Math.exp(-z));
  const pdPctNum = pd * 100;
  const pdPct = pdPctNum.toFixed(2);

  // Expected Loss = Loan Amount * PD * LGD (assume 45% standard Basel regulatory recovery loss)
  const expectedLoss = Math.round(loanAmount * pd * 0.45);

  let tier = 'Subprime (High Risk)';
  let status = '❌ Decline / Collateral Required';
  let meterWidth = Math.min(100, Math.round(pdPctNum * 3.5));
  let statusType: 'success' | 'warning' | 'danger' = 'danger';

  if (creditScore >= 760 && dti <= 30) {
    tier = 'AAA (Super Prime)';
    status = '✅ Fast-Track Auto Approved';
    meterWidth = 15;
    statusType = 'success';
  } else if (creditScore >= 700 && dti <= 38) {
    tier = 'AA (Prime Segment)';
    status = '✅ Approved with Standard Rate';
    meterWidth = 30;
    statusType = 'success';
  } else if (creditScore >= 640 && dti <= 45) {
    tier = 'A (Near Prime)';
    status = '🟡 Conditional Approval (+1.5% APR)';
    meterWidth = 55;
    statusType = 'warning';
  } else {
    tier = 'Subprime (High Risk)';
    status = '❌ Decline / Additional Collateral Required';
    meterWidth = Math.max(75, Math.min(96, Math.round(pdPctNum * 3.5)));
    statusType = 'danger';
  }

  return {
    pdPct,
    expectedLoss,
    tier,
    status,
    meterWidth,
    statusType,
  };
}
