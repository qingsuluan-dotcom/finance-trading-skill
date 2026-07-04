# Report Contract

Use concise, evidence-first reports.

## Research Output

```markdown
**Conclusion**
One sentence.

**Data**
Source, range, timestamp, adjustment.

**Evidence**
Compact table or metric list.

**Risks**
Data limits, market risks, interpretation caveats.
```

## Backtest Output

```markdown
**Strategy**
Explicit rules and assumptions.

**Data**
Source, range, benchmark, costs.

**Results**
Total return, annualized return, max drawdown, Sharpe, trades, benchmark comparison.

**Diagnostics**
Drawdown, turnover, sensitivity, unusual periods.

**Risks**
Biases, overfitting, liquidity, transaction-cost realism.

**Files**
Generated local paths, if any.
```

## File Naming

Use lowercase, descriptive names:

```text
prices_600519.SH_2020-01-01_2026-07-04.csv
backtest_ma_cross_600519.SH_2020-01-01_2026-07-04.md
equity_curve_ma_cross_600519.SH.csv
```

## Metadata

For exported data, include:

- Source.
- Query parameters.
- Pull time.
- Row count.
- Field list.
- Missing segments.
- Adjustment method.
