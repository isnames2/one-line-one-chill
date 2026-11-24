#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library, deterministic.
"""

import os
from pathlib import Path

LINE = (
    # One sentence of horror, 124 characters — inside the 1–200 gate.
    "The fitness tracker logged 4,000 steps at 3 a.m. while I slept, "
    "and the last entry read: 'standing at the foot of your bed.'"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
