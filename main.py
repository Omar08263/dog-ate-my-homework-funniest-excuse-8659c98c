"""Dog Ate My Homework: Funniest Excuse — entry program (program/v1).

A single-line excuse, spoken by the dog itself after being caught eating
the homework. The program is deterministic: every run writes exactly the
same bytes to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for a
local run). Standard library only; no network, no randomness, no reads
from anywhere outside this file.
"""

import os
from pathlib import Path

EXCUSE = "It had my name on it \u2014 right there at the top, in pencil. If my name's on it, it's mine. I ate it. That's the law."

MAX_CHARS = 200


def emit(target: Path) -> None:
    """Write the excuse to target, then make it world-readable."""
    if not 1 <= len(EXCUSE) <= MAX_CHARS:
        raise SystemExit(f"excuse is {len(EXCUSE)} chars, must be 1-200")
    if not EXCUSE.strip():
        raise SystemExit("excuse must not be only whitespace")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(EXCUSE.encode("utf-8"))
    target.chmod(0o644)


def confirm(target: Path) -> None:
    """Read the file back: it must hold exactly the approved excuse."""
    found = target.read_bytes().decode("utf-8")
    if found != EXCUSE:
        raise IOError("entry.txt does not match the approved excuse")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    entry = out_dir / "entry.txt"
    emit(entry)
    confirm(entry)


if __name__ == "__main__":
    main()
