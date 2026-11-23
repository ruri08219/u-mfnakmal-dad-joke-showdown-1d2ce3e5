#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke (at most 200 characters) to /output/entry.txt.
Deterministic: the same joke on every run, no input, no network.
Standard library only.
"""

import os

JOKE = "My dad mows the lawn in perfectly straight lines and calls it his grassroots campaign."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
