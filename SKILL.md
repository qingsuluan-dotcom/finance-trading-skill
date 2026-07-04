---
name: finance-trading-skill
description: 中文金融投研、量化分析与交易策略回测 Skill。Use when Codex needs to turn natural-language finance requests into reproducible research workflows, including stock or ETF trend analysis, financial statement review, industry research, screening, strategy design, historical backtesting, parameter scans, risk review, report generation, and data export. Supports A-share-first workflows with Tushare, AKShare, iWenCai-style search, Backtrader-style event backtests, VectorBT-style vectorized tests, and strict no-live-trading safety boundaries.
---

# Finance Trading Skill

Use this skill to convert Chinese natural-language finance questions into verifiable research, screening, and backtesting workflows. Treat it as a research and simulation assistant, not as an investment adviser or live trading bot.

## Core Rules

- Understand the user intent first, then choose data sources, analysis workflow, and output format.
- Default to A-share interpretation unless the user clearly says Hong Kong stocks, US stocks, crypto, futures, funds, or another market.
- Do not provide guaranteed returns, direct buy/sell instructions, or automatic live order execution.
- Always bind conclusions to data source, time range, assumptions, and limitations.
- For "latest", "today", "now", or real-time requests, verify the latest available data timestamp before answering.
- If requested data is unavailable, permission-gated, stale, empty, or ambiguous, state that plainly and do not fabricate.

## Intent Routing

Use `references/intent-taxonomy.md` when the request includes unclear or mixed intent.

- Market research: stock trend, relative strength, volume, volatility, valuation, financial quality, news or announcement review.
- Screening: build a stock pool by industry, concept, valuation, financial quality, liquidity, or momentum.
- Strategy design: translate a plain-language strategy into explicit universe, signal, position, cost, and rebalance rules.
- Backtesting: run historical tests, compare benchmarks, calculate performance metrics, and produce a reproducible report.
- Optimization: scan parameter ranges, show stability, and warn about overfitting.
- Export: produce CSV, parquet, Markdown reports, charts, or Python scripts when useful.

## Workflow

1. Resolve market, entity, universe, time range, frequency, and output expectations.
2. Select the minimum necessary data source. Read `references/data-sources.md` when choosing among APIs or local files.
3. Normalize dates, symbols, adjusted prices, missing values, and benchmark.
4. For research tasks, compute key evidence and produce a concise conclusion with caveats.
5. For strategy tasks, write explicit rules before running any backtest. Read `references/strategy-templates.md`.
6. For backtests, choose the engine style. Read `references/backtest-rules.md`.
7. Apply risk and compliance checks from `references/risk-and-compliance.md`.
8. Deliver the result using the contract in `references/report-contract.md`.

## Engine Selection

- Use vectorized logic for simple single-asset, cross-sectional, or parameter-grid tests.
- Use event-driven logic for order-level behavior, rebalancing, stop rules, cash, commissions, slippage, or position state.
- Use portfolio-style logic for allocation, rotation, and benchmark comparison.
- Use crypto-bot patterns only for crypto research or paper-trading design; do not enable live trading by default.

## Default Assumptions

- Market: A-share.
- Price frequency: daily.
- Adjustment: forward-adjusted when studying price performance; unadjusted only when explicitly needed.
- "Recent trend": last 20 trading days.
- "This period" or "recent months": last 3 months.
- "Financial report": latest 8 quarters plus latest annual data when available.
- "Capital flow": last 5 to 10 trading days.
- Benchmark: CSI 300 for broad A-share large-cap comparisons unless a better benchmark is obvious.

## Scripts

- `scripts/fetch_market_data.py`: create or validate a normalized market-data CSV schema.
- `scripts/normalize_prices.py`: normalize OHLCV CSV files and compute simple returns.
- `scripts/run_vector_backtest.py`: run a minimal moving-average vectorized backtest from CSV.
- `scripts/run_event_backtest.py`: run a minimal event-style moving-average backtest from CSV.
- `scripts/make_tearsheet.py`: create a Markdown performance summary from an equity curve CSV.

Prefer these scripts for repeatable local work, and patch them when a task requires a more specific workflow.
