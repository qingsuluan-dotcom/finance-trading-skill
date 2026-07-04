#!/usr/bin/env python
"""Minimal event-style moving-average backtest from CSV."""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def run(input_path: Path, output_path: Path, fast: int, slow: int, commission: float) -> None:
    if fast >= slow:
        raise SystemExit("--fast must be lower than --slow")

    with input_path.open(newline="", encoding="utf-8") as f:
        rows = sorted(csv.DictReader(f), key=lambda row: row["date"])

    cash = 1.0
    shares = 0.0
    closes: list[float] = []
    output = []

    for row in rows:
        close = float(row["close"])
        closes.append(close)
        if len(closes) >= slow:
            fast_ma = mean(closes[-fast:])
            slow_ma = mean(closes[-slow:])
            target_position = 1.0 if fast_ma > slow_ma else 0.0
        else:
            target_position = 0.0

        equity_before_trade = cash + shares * close
        current_position = 0.0 if equity_before_trade == 0 else shares * close / equity_before_trade
        trade_value = (target_position - current_position) * equity_before_trade
        if abs(trade_value) > 1e-12:
            cost = abs(trade_value) * commission
            cash -= trade_value + cost
            shares += trade_value / close

        equity = cash + shares * close
        output.append(
            {
                "date": row["date"],
                "close": f"{close:.6f}",
                "target_position": f"{target_position:.4f}",
                "cash": f"{cash:.8f}",
                "shares": f"{shares:.8f}",
                "equity": f"{equity:.8f}",
            }
        )

    os.makedirs(output_path.parent, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "close", "target_position", "cash", "shares", "equity"])
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote event-style backtest to {output_path}.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--fast", type=int, default=20)
    parser.add_argument("--slow", type=int, default=60)
    parser.add_argument("--commission", type=float, default=0.0003)
    args = parser.parse_args()
    run(Path(args.input).resolve(), Path(args.output).resolve(), args.fast, args.slow, args.commission)


if __name__ == "__main__":
    main()
