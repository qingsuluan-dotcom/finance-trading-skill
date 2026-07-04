#!/usr/bin/env python
"""Minimal vectorized moving-average backtest from normalized CSV."""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path


def moving_average(values: list[float], window: int) -> list[float | None]:
    result: list[float | None] = []
    for index in range(len(values)):
        if index + 1 < window:
            result.append(None)
        else:
            result.append(sum(values[index + 1 - window : index + 1]) / window)
    return result


def run(input_path: Path, output_path: Path, fast: int, slow: int) -> None:
    if fast >= slow:
        raise SystemExit("--fast must be lower than --slow")

    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    rows.sort(key=lambda row: row["date"])
    closes = [float(row["close"]) for row in rows]
    fast_ma = moving_average(closes, fast)
    slow_ma = moving_average(closes, slow)

    equity = 1.0
    previous_close = None
    out = []
    for row, close, fast_value, slow_value in zip(rows, closes, fast_ma, slow_ma):
        signal = 1 if fast_value is not None and slow_value is not None and fast_value > slow_value else 0
        daily_return = 0.0 if previous_close is None else close / previous_close - 1
        strategy_return = daily_return * signal
        equity *= 1 + strategy_return
        previous_close = close
        out.append(
            {
                "date": row["date"],
                "close": f"{close:.6f}",
                "signal": signal,
                "strategy_return": f"{strategy_return:.8f}",
                "equity": f"{equity:.8f}",
            }
        )

    os.makedirs(output_path.parent, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "close", "signal", "strategy_return", "equity"])
        writer.writeheader()
        writer.writerows(out)
    print(f"Wrote equity curve to {output_path}.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--fast", type=int, default=20)
    parser.add_argument("--slow", type=int, default=60)
    args = parser.parse_args()
    run(Path(args.input).resolve(), Path(args.output).resolve(), args.fast, args.slow)


if __name__ == "__main__":
    main()
