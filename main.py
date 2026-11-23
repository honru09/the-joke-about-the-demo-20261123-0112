#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

Writes the entry text to /output/entry.txt (UTF-8, 1-280 Unicode
code points, not only whitespace). Stdlib only, no network, no
time, no randomness: the output is fully deterministic.
"""

import os

ENTRY = (
    "My agent rewrote the demo in six minutes, fixed every bug \u2014 "
    "then, live on stage in front of forty people, confidently "
    "deleted the database it had spent an hour backing up to itself."
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not only
    # whitespace, or the sealed scorer marks it invalid (Valid = 0).
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise ValueError(
            f"entry must be 1-280 code points, got {len(ENTRY)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
