#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse -- make.fun entry.

Writes the single funniest AI excuse for a missed deadline to
/output/entry.txt, where the program/v1 harness reads it. Pure
standard library, no I/O besides that one file.

The line was picked from 10 candidates scored against the judge's
brief: it names the missed deadline outright, gives a specific and
surprising reason (the agent hallucinated it had already finished),
turns the agent's own nature (hallucination) into the dodge, and
lands its punchline — giving itself the day off — at the very end.
"""

import os

LINE = (
    "I missed the deadline because I hallucinated I'd already finished it, "
    "and the hallucination was so confident I gave myself the day off."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters, got %d" % len(line)
    assert "\n" not in line, "entry must be a single line"
    assert line.endswith("."), "entry must end with a period"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch: file differs from entry"


if __name__ == "__main__":
    main()
