#!/usr/bin/env python
"""Create a compact Markdown tearsheet from an equity curve CSV."""

from __future__ import annotations

import argparse
import csv
import math
import os
from pathlib import Path


def max_drawdown(equity: list[float]) -> float:
    peak = equity[0]
    worst = 0.0
    for value in equity:
        peak = max(peak, value)
        worst = min(worst, value / peak - 1)
    return worst


def make(input_path: Path, output_path: Path, title: str) -> None:
    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    equity = [float(row["equity"]) for row in rows]
    returns = [equity[index] / equity[index - 1] - 1 for index in range(1, len(equity))]
    total_return = equity[-1] - 1 if equity else 0.0
    avg_return = sum(returns) / len(returns) if returns else 0.0
    variance = sum((value - avg_return) ** 2 for value in returns) / len(returns) if returns else 0.0
    sharpe = 0.0 if variance == 0 else avg_return / math.sqrt(variance) * math.sqrt(252)
    drawdown = max_drawdown(equity) if equity else 0.0

    content = f"""# {title}

## Results

| Metric | Value |
|---|---:|
| Rows | {len(rows)} |
| Total return | {total_return:.2%} |
| Max drawdown | {drawdown:.2%} |
| Sharpe (daily, annualized) | {sharpe:.2f} |

## Caveats

This tearsheet is generated from a local equity curve. Confirm data source, adjustment, commission, slippage, benchmark, and look-ahead bias before using the result.
"""
    os.makedirs(output_path.parent, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Wrote tearsheet to {output_path}.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--title", default="Backtest Tearsheet")
    args = parser.parse_args()
    make(Path(args.input).resolve(), Path(args.output).resolve(), args.title)


if __name__ == "__main__":
    main()
