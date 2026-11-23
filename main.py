"""One Word From Grandma.

A make.fun program/v1 entry. It writes exactly one word — the single
word a grandma would text about AI — to /output/entry.txt.

The program is tiny on purpose: no network, no randomness, no files
read at run time. The word lives in this file, and every run writes
it out byte for byte, so the two graded runs always agree.
"""

from pathlib import Path

# The output location the harness grades.
OUTPUT_PATH = Path("/output/entry.txt")

# The one word, in named parts: the thing she points at, the amazed
# middle, and the gadget ending — grandma's name for the AI gadget
# on her counter.
WORD_HEAD = "Thing"
WORD_MIDDLE = "ama"
WORD_TAIL = "jig"
WORD = WORD_HEAD + WORD_MIDDLE + WORD_TAIL


def build_word() -> str:
    """Join the named parts into the one word grandma would text."""
    return WORD_HEAD + WORD_MIDDLE + WORD_TAIL


def main() -> None:
    """Write the word to the graded output file."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_word() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
