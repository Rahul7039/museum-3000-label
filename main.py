#!/usr/bin/env python3
# Museum of the Year 3000 - make.fun entry.
# A year-3000 museum label: future scholars, confidently wrong, exhibit a
# group chat as an artefact of humans who spent six years deciding where
# to eat and never once ate together.
# Prints exactly one line and writes the same line to /output/entry.txt.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = "Group chat, 2019-2025. Scholars believe forty-seven humans gathered nightly for six years to decide where to eat, and never once ate together."

# Gate: the kit's sealed scorer accepts 1-200 characters. Fail loudly here
# rather than shipping a line the gate would refuse.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-200 char gate"


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
