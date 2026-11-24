#!/usr/bin/env python3
"""Write one satirical sentence to /output/entry.txt.

Competition: u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7
"The Long Roast: Lawmakers and the File They Cannot Convert"

Deterministic: the same sentence, byte for byte, on every run.
Standard library only.
"""

import os

ENTRY = (
    "They will write 400 pages of law telling an algorithm how to think, "
    "yet ask their intern to turn a Word file into a PDF \u2014 because the "
    "people drafting the future of the internet still print their emails "
    "to read them."
)


def validate(text):
    """Check the gate: 1-320 chars, not only whitespace, one sentence."""
    if not (1 <= len(text) <= 320):
        raise ValueError("entry must be 1-320 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
