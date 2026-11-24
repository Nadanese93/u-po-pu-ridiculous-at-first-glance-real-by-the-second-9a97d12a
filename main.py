"""Entry program for "Ridiculous at First Glance, Real by the Second".

Writes a single-sentence startup pitch (max 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.
Python standard library only.

The pitch: retired switchboard operators answer small businesses' phones
in a warm 1950s voice. The ridiculous-but-real turn is the business logic —
a polite vintage "one moment, connecting you now" makes callers wait
patiently instead of hanging up and calling a rival, so the small
businesses paying for the service keep customers they would otherwise lose.
"""

import os

ENTRY = (
    "Retired switchboard operators answer small businesses' phones in a warm "
    "1950s voice, so callers who hear 'one moment, connecting you now' wait "
    "patiently instead of hanging up and calling a rival."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
