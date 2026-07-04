#!/usr/bin/env python
"""Create or validate normalized market data for finance-trading-skill."""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path


FIELDS = ["date", "symbol", "open", "high", "low", "close", "volume", "amount"]


def write_sample(path: Path, symbol: str) -> None:
    rows = [
        ["2024-01-02", symbol, "10.00", "10.30", "9.90", "10.20", "1000000", "10200000"],
        ["2024-01-03", symbol, "10.20", "10.50", "10.10", "10.40", "1100000", "11440000"],
        ["2024-01-04", symbol, "10.40", "10.60", "10.00", "10.10", "980000", "9898000"],
    ]
    os.makedirs(path.parent, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(FIELDS)
        writer.writerows(rows)


def validate(path: Path) -> None:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [field for field in ["date", "close"] if field not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit(f"Missing required field(s): {', '.join(missing)}")
        rows = sum(1 for _ in reader)
    print(f"Validated {path} with {rows} rows.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="Output CSV path.")
    parser.add_argument("--symbol", default="SAMPLE", help="Symbol for sample data.")
    parser.add_argument("--validate-only", action="store_true", help="Validate an existing CSV.")
    args = parser.parse_args()

    path = Path(args.output).resolve()
    if args.validate_only:
        validate(path)
    else:
        write_sample(path, args.symbol)
        validate(path)


if __name__ == "__main__":
    main()
