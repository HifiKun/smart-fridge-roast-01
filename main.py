"""Smart Fridge Roast: One Line, Best Laugh Wins.

The program writes a single roast line to /output/entry.txt. The line is
the whole entry: one line, at most 160 characters, roasting a smart fridge.
The twist is the punchline: the fridge's inside camera photographs the
midnight snacks, then shows the owner the photos over breakfast -- the
only roommate who snitches on you, in 4K.
"""

import os

LINE = (
    "My smart fridge photographs everything I eat at 2 a.m. and shows me "
    "the photos over breakfast — the only roommate who snitches on me in 4K."
)


def main() -> None:
    # The gate only accepts 1-160 characters of non-blank text on one line,
    # so refuse to write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 160:
        raise ValueError(
            f"entry line must be one line of 1-160 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
