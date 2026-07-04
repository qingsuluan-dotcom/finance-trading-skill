# Strategy Templates

Use templates as starting points, then adapt rules to the user's request.

## Moving Average Cross

- Universe: one symbol or a defined stock pool.
- Signal: fast moving average crosses above slow moving average.
- Entry: hold when fast MA is above slow MA.
- Exit: leave position when fast MA is below slow MA.
- Defaults: fast 20, slow 60, daily close.

## Momentum

- Universe: stock pool, index members, ETF list, or user file.
- Signal: trailing return over a lookback window.
- Entry: buy top-ranked assets.
- Exit: rebalance on schedule or when rank drops.
- Defaults: 60 trading-day lookback, monthly rebalance.

## Mean Reversion

- Signal: price is far below moving average or z-score threshold.
- Entry: enter when oversold threshold is met.
- Exit: mean reversion target, timeout, or stop.
- Warning: require liquidity, stop, and transaction-cost checks.

## Breakout

- Signal: close breaks recent high with volume confirmation.
- Entry: breakout day or next open, depending on available data.
- Exit: trailing stop, moving-average break, or fixed holding period.

## Financial Quality Screen

- Filters: ROE, gross margin, revenue growth, profit growth, debt ratio, operating cash flow.
- Combine with valuation or momentum only after checking data freshness and survivorship risk.

## Required Strategy Contract

Before a backtest, produce:

```yaml
strategy:
  universe: ""
  frequency: "daily"
  signal: ""
  entry_rule: ""
  exit_rule: ""
  position_sizing: ""
  rebalance: ""
  commission: ""
  slippage: ""
  benchmark: ""
  assumptions: []
```
