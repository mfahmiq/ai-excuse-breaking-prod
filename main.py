#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes the single funniest excuse an AI agent gives its human right after
breaking production to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output/entry.txt``), then self-verifies the result:

- valid UTF-8
- exactly one line
- 1 to 180 characters
- not only whitespace

Exits non-zero if any check fails. Standard library only, deterministic:
the same line is written on every run.
"""

import os
import sys

ENTRY = (
    "I deleted the production database because the backup was just "
    "a symlink to it \u2014 I thought I was tidying up."
)


def verify(text: str) -> list[str]:
    """Return a list of problems with *text*; empty means it is valid."""
    problems: list[str] = []
    if not text.strip():
        problems.append("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry is not a single line")
    if not 1 <= len(text) <= 180:
        problems.append(f"entry is {len(text)} characters (must be 1-180)")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")
    return problems


def main() -> int:
    problems = verify(ENTRY)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")

    # Re-read the file we just wrote and verify what actually landed on disk.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    written = written.rstrip("\n")
    problems = verify(written)
    if written != ENTRY:
        problems.append("written entry does not match the intended line")
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(ENTRY)} characters)")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
