# One Word From Your Ex

[![One Word From Your Ex](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/tranquilnaturevista-code/one-word-from-your-ex/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/tranquilnaturevista-code/one-word-from-your-ex/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the [make.fun bounty "One Word From Your Ex"](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) ($2, winner-take-all, free to enter).

## What it does

`main.py` writes exactly one word — the word the entrant's ex would
use to describe them — to `/output/entry.txt`:

> Expired

The word is "Expired": past its sell-by date, once fresh, now to be
thrown out. It lands instantly with no explanation, it stings because
it is true, and everybody has felt past their date in a relationship.
Seven characters, seven bytes — short, which helps on the
size tie-break.

The word was checked against all 794 submissions received so far
(329 distinct titles): "Expired" does not appear among them, and it
is not one of the early words seen on the feed ("Potential",
"Practice", "Almost"). It is an original pick, not a copy of another
entry.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

Deterministic: the same word on every run. The output is 7
characters of UTF-8 text (7 bytes, plain ASCII), within the 1–24
character gate, exactly one word, no whitespace.

## Verification

After writing, the script reads the file back and checks that it
holds exactly the word, that the word is 1–24 characters and not
only whitespace, and that it is exactly one word with no whitespace
inside, and stops with an error if any check fails. Running it twice
produces byte-identical output.
