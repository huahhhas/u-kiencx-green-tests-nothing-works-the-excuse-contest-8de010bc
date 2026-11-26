#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Prints the one-line excuse and writes it byte-identical to
/output/entry.txt (1-140 characters, UTF-8, one line).
"""

import os

LINE = (
    "The tests passed - I wrote the questions, the answers, and the "
    "grading rubric. The app still does nothing, but it does it with honours."
)


def main() -> None:
    # The gate requires 1-140 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    text = LINE + "\n"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
