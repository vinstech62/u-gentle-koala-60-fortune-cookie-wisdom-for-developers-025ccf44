#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes exactly one original fortune-cookie line for a software
developer to /output/entry.txt.

The line: "The legacy code you curse was written by someone exactly
as tired as you."

Why this line: it reads like a real fortune cookie — one short,
balanced, second-person sentence that lands in a single breath. It
is true about a developer's day: every senior has inherited legacy
code and cursed its author. And it turns that truth around: the
author was not lazy or careless, just exactly as tired as you are
now — which quietly means the code you write tired tonight is the
legacy someone else will curse tomorrow. That second read is the
twist, and the empathy is what makes a tired senior engineer smile
and nod instead of shrug.
"""
import os

LINE = "The legacy code you curse was written by someone exactly as tired as you."


def main() -> None:
    # Gate self-check: one line, 1-120 UTF-8 characters, not blank.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE.encode("utf-8")) <= 120, "entry must be 1-120 UTF-8 chars"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
