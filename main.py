#!/usr/bin/env python3
"""One Line, No Deadline Met — one-line deadline excuse writer.

Writes a single original excuse line (1-200 chars) to entry.txt
in the output directory and nothing else.
"""

import os

EXCUSE = "I treated the deadline like a software update and kept clicking 'remind me tomorrow' until I ran out of tomorrows."


def output_dir():
    """Grader contract: MAKEFUN_OUTPUT_DIR is /output; fall back to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars"
    assert "\n" not in text, "excuse must be a single line"
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
