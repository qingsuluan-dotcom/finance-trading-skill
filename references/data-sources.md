# Data Sources

Choose the smallest reliable source set that can answer the task.

## A-share Defaults

- Tushare: structured A-share, index, fund, financial, valuation, money-flow, macro, and announcement data when `TUSHARE_TOKEN` is configured.
- AKShare: broad public Chinese financial data access and useful fallback for market, macro, industry, and concept data.
- iWenCai-style search: natural-language finance news, company, theme, and market information when an iWenCai-compatible API key or tool is available.
- Local CSV/parquet: preferred when the user provides data or reproducibility matters more than freshness.

## Other Markets

- US stocks: use user-provided files, yfinance-style sources, or available finance tools.
- Crypto: use exchange data or Freqtrade-style data conventions for research and paper simulations.
- Funds/ETF: separate fund NAV, ETF market price, index tracking, and holdings where possible.

## Source Selection Rules

- Confirm credentials before relying on permissioned APIs.
- Prefer official or structured APIs over scraped pages when both are available.
- For long ranges, fetch in segments and merge deterministically.
- Record data source, API name, parameters, pull time, field list, and row count.
- When multiple sources disagree, state the conflict and avoid false precision.

## Normalized Price Schema

For scripts and local exports, use:

```text
date,symbol,open,high,low,close,volume,amount
```

Required fields: `date`, `close`.

Recommended rules:

- Dates: `YYYY-MM-DD`.
- Sort ascending by date.
- Deduplicate by `date,symbol`.
- Keep numeric columns numeric.
- State whether prices are adjusted.
