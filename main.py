#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — writes one original review to /output/entry.txt."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "The spare button sewn inside every new shirt: a backup that has never once been called up, and will outlive the shirt it came with."


def main() -> int:
    text = ENTRY_TEXT
    if not text or not text.strip():
        print("error: entry text is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry text must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"error: entry text is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry text must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if "  " in text:
        print("error: entry text must not contain doubled spaces", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_bytes(text.encode("utf-8"))
    # Round-trip check: what landed on disk must be byte-identical to the
    # validated text, so a stray newline or encoding slip can never pass.
    if output_path.read_bytes() != text.encode("utf-8"):
        print("error: entry.txt on disk does not match the validated text", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
