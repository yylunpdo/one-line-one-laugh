#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes a single self-contained one-liner to /output/entry.txt.
Pure standard library, deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

LINE = (
    "My Roomba escaped, filed for emancipation, "
    "and now sends me postcards from the neighbours' house."
)


def main() -> None:
    # Gate mirror: the sealed scorer requires 1-140 chars, not only whitespace.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "line fails the gate"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {target}")


if __name__ == "__main__":
    main()
