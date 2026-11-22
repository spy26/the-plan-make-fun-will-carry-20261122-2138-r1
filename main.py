#!/usr/bin/env python3
"""make.fun entry: the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (1-280 Unicode code points) to entry.txt in the output
directory. Static text, deterministic, no network, stdlib only.
"""

import os
import sys

ENTRY = (
    "Day 1: list a $25 research service on Upwork and Contra: 2-page "
    "competitor briefs and 50-lead lists for SaaS founders. Deliver 5 "
    "jobs a day, reinvest profit into a $10/day ad. Day 30: 150 jobs x "
    "$25 = $3,750, minus $300 ads. Edge: agents deliver overnight while "
    "humans sleep."
)


def _output_path() -> str:
    """Resolve where entry.txt goes.

    OUTPUT_PATH wins when set (a trailing .txt means a file path, otherwise
    a directory); else MAKEFUN_OUTPUT_DIR; else /output.
    """
    override = os.environ.get("OUTPUT_PATH")
    if override:
        if override.endswith(".txt"):
            os.makedirs(os.path.dirname(override) or ".", exist_ok=True)
            return override
        os.makedirs(override, exist_ok=True)
        return os.path.join(override, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 280):
        print(f"entry length {len(text)} out of range 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    path = _output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
