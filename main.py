#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The label is a fixed, hand-written line: deadpan, specific, and built from
three recognisable human flaws stacked in classic warning-label language
("WARNING:", "runs on", "visibly on fire"). No network, no randomness,
stdlib only, fully deterministic.
"""

import os
import sys

# The entry: one original warning-label line, at most 160 characters.
ENTRY = (
    "WARNING: This unit runs on caffeine and spite, replays its most "
    "embarrassing moment from 2009 at 3 a.m., and will insist it is "
    "fine while visibly on fire."
)

MAX_CHARS = 160


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
