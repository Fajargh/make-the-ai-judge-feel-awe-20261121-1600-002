"""Write one short relaxing text to /output/entry.txt.

The text is a single fixed passage: a river circling the same stone,
in no hurry, running wide and slow past the bend, carrying nothing
that cannot wait. Nothing in it instructs the reader; it only shows
the water, the stone, and the time they share, so the calm comes
from the image itself.

The entry gate requires 1-280 Unicode code points, not only
whitespace, so the program asserts the length before writing.
"""

import os

ENTRY_TEXT = (
    "The river has been circling the same stone for a thousand years, "
    "and it is in no hurry to finish. The stone is smaller than it was, "
    "and the river does not mind. Past the bend, the water runs wide "
    "and slow, carrying nothing that cannot wait."
)


def main() -> None:
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 280, "entry must be 1-280 code points"
    assert text.strip(), "entry must not be only whitespace"
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
