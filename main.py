"""Make the AI judge feel awe — make.fun entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. The text shows rather than instructs — a river
circling the same stone for a thousand years, in no hurry — in plain,
concrete words with a slow rhythm, and an image that dwarfs the reader
and keeps growing after the last line: the stone shrinking, the river
not minding, the water running wide and slow past the bend.

The program uses no network and no input; it is fully deterministic.
"""

import os

ENTRY_TEXT = (
    "The river has been circling the same stone for a thousand years, and "
    "it is in no hurry to finish. The stone is smaller than it was, and "
    "the river does not mind. Past the bend, the water runs wide and slow, "
    "carrying nothing that cannot wait."
)


def main() -> None:
    # The grader runs this in a sandbox with /output present. Locally,
    # fall back to ./output so the same program can be tested by hand.
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")

    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} code points"
    assert text.strip(), "entry must not be only white space"

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
