# Intent Taxonomy

Classify the request before selecting tools or data.

## Research

Use for questions such as:

- "看看这只股票最近强不强"
- "财报质量怎么样"
- "最近有什么催化"
- "这个行业为什么涨"

Required output:

- One-sentence conclusion.
- Data range and source.
- Key evidence table or compact metric list.
- Risks, anomalies, and interpretation limits.

## Screening

Use for questions such as:

- "筛一批高 ROE 低负债的公司"
- "找最近放量突破的股票"
- "半导体里谁更强"

Required output:

- Universe definition.
- Filter rules.
- Sorted result table.
- Data timestamp and missing-data notes.

## Strategy Design

Use for questions such as:

- "做一个双均线策略"
- "用财务质量加动量构建策略"
- "这个策略规则补完整"

Before backtesting, make rules explicit:

- Universe.
- Signal.
- Entry.
- Exit.
- Position sizing.
- Rebalance frequency.
- Costs and slippage.
- Benchmark.

## Backtesting

Use for questions such as:

- "回测一下"
- "看看这个策略过去五年表现"
- "和沪深300比一下"

Required output:

- Strategy rules.
- Data source and range.
- Performance metrics.
- Benchmark comparison.
- Drawdown and trade behavior.
- Bias and risk warnings.
- Reproducible files when generated.

## Optimization

Use for parameter scans and robustness tests.

Do not recommend only the best historical parameter. Show stable regions, sensitivity, and overfitting risk.

## Export

Use for requests to produce CSV, parquet, Markdown, PNG, or Python scripts. Include metadata describing source, parameters, rows, fields, and generated time.
