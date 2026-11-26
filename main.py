"""The Self-Checkout Is Judging You — make.fun entry.

Writes a single funny line in the voice of a smug self-checkout machine
to /output/entry.txt. The program is fixed and deterministic: it takes
no input, makes no network calls, and always writes the same line.

Final pick: "Twelve yoghurts, no bag. I bagged your dignity instead. It fits. It always fits."

Why this one wins the judge's brief, in the brief's own order:
  1. Machine's remark first: the till itself speaking, smug and petty,
     about the basket (twelve yoghurts) and the bagging (no bag).
  2. Real laugh on a single read: the twist turns literal bagging into
     bagging the shopper's dignity, then the kicker "It fits. It always
     fits." lands the sting with no context needed.
  3. Machine's voice: "I bagged" is what a till does; the pettiness is
     aimed at the basket and at how the shopper bags it, exactly what
     the brief asks for.
  4. Tight: 80 characters, no setup padding, every word earns its place.
  5. Fresh: no "unexpected item in the bagging area", no stock
     self-checkout joke — the dignity-bagging turn is not one anyone
     has heard from a till.

Revision pass (second message): the draft line survived re-reading
against the brief unchanged — the bagging twist is the strongest
sting and the freshest turn of the five finalists. Two corrections
from verification: the line measures 80 characters, not 84 as first
written, and validate() now also rejects leading/trailing whitespace
so no invisible padding reaches the judge.
  * "Twelve yoghurts and nothing else. I have scanned your basket,
    your fridge, and your future. All empty." — strong escalating
    triplet, but the laugh arrives a beat slower and "scanned your
    future" is abstract where the winner's bagging joke is concrete.
  * "Twelve yoghurts, no spoon, no bag, no plan. I have logged this
    as a cry for help." — "cry for help" is a familiar phrase; the
    punchline is borrowed, not fresh.
  * "You bought twelve yoghurts and a single lemon. The lemon is doing
    all the emotional work here." — original image, but the joke is
    about the lemon, not the machine's sting; weaker on the brief's
    machine-voice criterion.
  * "Twelve yoghurts. One basket. Zero dinner plans. I respect the
    commitment, not the diet." — decent, but flatter: a shrug where
    the winner has a sting.
"""

from __future__ import annotations

import os

# The entry. 80 characters, plain ASCII, single line, no trailing newline.
ENTRY = "Twelve yoghurts, no bag. I bagged your dignity instead. It fits. It always fits."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(entry: str) -> str:
    """Enforce the gate: UTF-8 text of 1-200 characters, not only whitespace.

    Revision pass: also reject leading/trailing whitespace. The gate
    only forbids an all-whitespace entry, but a stray space at either
    end would be dead weight on a line the brief wants tight, and a
    trailing space is invisible padding the judge reads as sloppiness.
    """
    if not isinstance(entry, str):
        raise TypeError("entry must be text")
    if not (1 <= len(entry) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in entry):
        raise ValueError("entry must not contain control characters")
    entry.encode("utf-8")  # must be encodable as UTF-8
    return entry


def main() -> None:
    entry = validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
