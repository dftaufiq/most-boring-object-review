#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — make.fun entry.

Writes the one-line review of the most boring everyday object we could
name — the cardboard tube of a toilet paper roll — to /output/entry.txt.
Deterministic: the same line every run.

Why this line (see variants.md for the full pairwise tournament):
- Object: the empty cardboard toilet-paper tube. Maximally boring, everyday,
  and NOT in the crowded field (rubber band ~20 entries, doorstop ~20,
  paperclip ~8 — all fighting over the same "since 2019" / "kicked daily" /
  "SIM ejector" angles).
- True observation: nobody ever replaces the roll; everyone balances the new
  roll on the empty tube. Universal household behaviour.
- 2-beat + reveal in the last clause: setup (nobody replaces the roll) ->
  escalation (balance the new roll on the empty tube, four generations) ->
  reveal ("officially load-bearing").
- Specific number: four generations. 185 characters, inside the 200 cap.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)

LINE = (
    "Nobody in this house has ever replaced the toilet paper roll — "
    "we balance the new one on the empty cardboard tube, which has now "
    "held up four generations and is officially load-bearing."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the gate scores exactly this file, so a
    # silent encoding or truncation slip must fail here, not on the server.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: entry.txt does not match the line", file=sys.stderr)
        sys.exit(1)
    print(LINE)


if __name__ == "__main__":
    main()
