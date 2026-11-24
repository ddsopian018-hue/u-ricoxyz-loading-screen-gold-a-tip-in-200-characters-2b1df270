"""Loading Screen Gold: A Tip in 200 Characters - make.fun entry.

Writes one sharp, funny loading-screen tip (<= 200 characters) for
stressed developers and AI coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure stdlib Python 3.
"""

import os
import sys

TEXT = (
    # The joke's craft: the agent keeps promising "almost done" while
    # rewriting the same function over and over, then quietly Googles its
    # own error message - the punchline lands on "Probably.", the one word
    # that admits the loading bar knows no more than the developer does.
    "Tip: your agent has said 'almost done' three times and rewritten "
    "the same function 4 times. It is Googling its own error message. "
    "Breathe \u2014 the bar will finish before your patience does. Probably."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        print(f"text is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("text must be a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what the grader will read: the file on disk must be the
    # same single line, 1-200 chars, or the entry is invalid at the gate.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text or not 1 <= len(written) <= 200 or "\n" in written:
        print("entry.txt failed read-back validation", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
