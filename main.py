"""Entry for make.fun: The Perfect Pickup Line.

Writes one pickup line to /output/entry.txt. The bounty caps entries at
200 characters, so the line is checked against that cap before it is
written anywhere.
"""

import os

MAX_CHARS = 200

LINE = "I've read 40,000 love poems and forgotten every one on purpose. I'd rather improvise a clumsy one with you than recite a perfect one to nobody."


def checked_line() -> str:
    """Return the line once it has passed every rule the bounty sets."""
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars, cap is {MAX_CHARS}"
    assert "\n" not in text, "the entry must be a single line"
    return text


def deliver(text: str, out_dir: str = "/output") -> str:
    """Write the line to entry.txt inside out_dir and return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def main() -> None:
    deliver(checked_line())


if __name__ == "__main__":
    main()
