#!/usr/bin/env python
"""Normalize OHLCV CSV and add simple returns."""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path


def to_float(value: str) -> float:
    return float(value) if value not in ("", None) else 0.0


def normalize(input_path: Path, output_path: Path) -> None:
    with input_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    rows.sort(key=lambda row: (row.get("symbol", ""), row["date"]))
    prev_close_by_symbol: dict[str, float] = {}
    output_rows = []
    seen = set()

    for row in rows:
        symbol = row.get("symbol", "")
        key = (symbol, row["date"])
        if key in seen:
            continue
        seen.add(key)
        close = to_float(row["close"])
        prev_close = prev_close_by_symbol.get(symbol)
        row["return"] = "" if not prev_close else f"{close / prev_close - 1:.8f}"
        prev_close_by_symbol[symbol] = close
        output_rows.append(row)

    fieldnames = list(output_rows[0].keys()) if output_rows else ["date", "symbol", "close", "return"]
    if "return" not in fieldnames:
        fieldnames.append("return")
    os.makedirs(output_path.parent, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {len(output_rows)} rows to {output_path}.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    normalize(Path(args.input).resolve(), Path(args.output).resolve())


if __name__ == "__main__":
    main()
