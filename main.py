#!/usr/bin/env python3
# Museum of the Year 3000 - make.fun one-line entry.
# Prints exactly one line: the entry text, nothing else.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = 'Group chat, 2019-2025. Forty-seven humans spent six years deciding where to eat, and never once ate together.'


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
