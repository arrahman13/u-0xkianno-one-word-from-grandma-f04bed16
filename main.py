#!/usr/bin/env python3
"""One Word From Grandma — make.fun bounty entry.

The task: exactly one word, the word grandma would text about AI.

The word is KNOWITALL. Grandma has met the new machine that answers
every question instantly, in a cheerful voice, at any hour — and she
has filed it under the oldest category she has: a know-it-all. It is
her voice in one word (warm, a little baffled, teasing the way she
teases a grandchild who shows off), the joke needs no caption, and it
is tied to what AI actually does — it knows everything, or acts like
it. Typed the way she types it: caps lock on, no time for spaces.

The program writes the word to entry.txt in the output directory and
checks it against the competition gate before finishing: UTF-8 text,
1 to 30 characters, not only whitespace, exactly one word.
"""

import os
import sys

WORD = "KNOWITALL"


def check_gate(text: str) -> None:
    """Raise ValueError unless text passes the competition gate:
    UTF-8 text of 1 to 30 characters, not only whitespace, one word."""
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry must be 1-30 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text.split()) != 1:
        raise ValueError(f"entry must be exactly one word, got {text!r}")


def main() -> int:
    check_gate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(WORD)
    # Read it back and gate the bytes on disk, not just the constant:
    # what the judge reads is the file, so the file is what is checked.
    with open(path, "rb") as fh:
        written = fh.read().decode("utf-8")
    check_gate(written)
    if written != WORD:
        raise ValueError(f"entry.txt holds {written!r}, expected {WORD!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
