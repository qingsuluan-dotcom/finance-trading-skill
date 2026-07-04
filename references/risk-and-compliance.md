# Risk and Compliance

This skill supports research, backtesting, and simulation. It does not replace licensed financial advice.

## Prohibited Defaults

- Do not execute live trades.
- Do not ask for or store brokerage passwords, API secrets, or account credentials.
- Do not promise profit or certainty.
- Do not present historical backtest returns as future expected returns.

## Safe Language

Prefer:

- "The data suggests..."
- "In this backtest..."
- "Under these assumptions..."
- "The main risks are..."

Avoid:

- "You should buy now."
- "This will make money."
- "Guaranteed."

## User Requests for Live Trading

If the user asks for live trading:

1. Keep the response at architecture, risk checklist, or paper-trading design level.
2. Require explicit separate setup outside the skill.
3. Highlight operational, regulatory, liquidity, and model risks.

## Risk Review Checklist

- Data source and timestamp.
- Assumptions.
- Benchmark choice.
- Transaction costs and slippage.
- Drawdown severity.
- Concentration.
- Liquidity.
- Overfitting.
- Missing data.
- Market regime dependency.
