# Backtest Rules

Backtests must be reproducible and bias-aware.

## Engine Choice

- Vectorized: use for simple signal-to-position tests, parameter grids, and quick comparisons.
- Event-driven: use for cash, order timing, commissions, slippage, stops, rebalancing, or stateful positions.
- Portfolio: use for rotation, allocation, multi-asset rebalance, and benchmark comparisons.

## Required Inputs

- Clean price data.
- Clear signal and execution timing.
- Start and end dates.
- Benchmark.
- Commission and slippage.
- Position sizing.

## Required Metrics

- Total return.
- Annualized return.
- Maximum drawdown.
- Sharpe ratio when returns are frequent enough.
- Win rate when trades are available.
- Trade count.
- Turnover or average exposure when available.
- Benchmark-relative return.

## Bias Checks

Always check and mention:

- Future function or look-ahead bias.
- Survivorship bias.
- Overfitting.
- Stop-limit and limit-up/down behavior for A-shares.
- Suspensions and missing trading days.
- Liquidity and transaction-cost realism.
- Data adjustment and dividend handling.

## Optimization Rules

- Define parameter ranges before running.
- Report stable regions, not only best parameters.
- Penalize unrealistic turnover and fragile single-point optima.
- Use walk-forward or out-of-sample checks when scope allows.
