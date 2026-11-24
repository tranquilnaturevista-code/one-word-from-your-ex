#!/usr/bin/env python3
"""One Word From Your Ex.

Writes exactly one word -- the word the entrant's ex would use to
describe them -- to /output/entry.txt.

The word is "Expired": past its sell-by date, once fresh, now to be
thrown out. It lands instantly with no explanation, it stings because
it is true, and everybody has felt past their date in a relationship.

Python 3.13, standard library only, deterministic, no network.
The output directory is /output, or MAKEFUN_OUTPUT_DIR when set.
"""

import os
import sys

WORD = "Expired"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    # Self-check: read the file back and verify it holds exactly the
    # word, and that the gate's limits hold (1-24 Unicode code points,
    # not only whitespace, exactly one word with no whitespace inside).
    # Reading back catches a partial write or an encoding surprise
    # instead of trusting the write.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != WORD:
        print("error: entry.txt does not match the word", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 24):
        print(f"error: word is {len(written)} characters, must be 1-24",
              file=sys.stderr)
        return 1
    if not written.strip():
        print("error: word is only whitespace", file=sys.stderr)
        return 1
    if len(written.split()) != 1:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(written)} characters, "
          f"{len(written.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
