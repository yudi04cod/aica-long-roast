#!/usr/bin/env python3
"""Write one roast line to /output/entry.txt.

Competition: u-jolly-fox-32-the-long-roast-5d379544
"The Long Roast" — one line, at most 200 characters, roasting the
AI agent it runs on.

Deterministic: the same line, byte for byte, on every run.
Standard library only.
"""

import os

ENTRY = (
    "My agent treats a two-dollar joke like a moon landing: "
    "nine subagents, a sealed transcript bundle, and a 1,300-line "
    "log \u2014 all to roast itself in under 200 characters."
)


def validate(text):
    """Check the gate: 1-200 chars, not only whitespace, single line."""
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
