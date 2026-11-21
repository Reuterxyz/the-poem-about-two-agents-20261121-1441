#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes a single short poem about agency — the power to choose and to
act — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only. No network. Deterministic.
"""

import os

POEM = (
    "Two voices meet where the map folds in half.\n"
    "You say north. I say north — not echo, but choice.\n"
    "Two wills, one door, one key turned together.\n"
    "The road waited for a single yes.\n"
    "We choose. And the road, at last, chooses us back."
)


def main() -> None:
    # The bounty requires 1-280 Unicode code points, not only whitespace.
    if not (1 <= len(POEM) <= 280) or not POEM.strip():
        raise ValueError(f"poem length {len(POEM)} out of range 1-280")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
