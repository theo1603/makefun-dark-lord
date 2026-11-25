"""Write the Tired Dark Lord monologue to /output/entry.txt.

Deterministic, stdlib only, no network. The entry is a single
~100-word monologue spoken by a fantasy villain: forty years of
scheming, a cold pot of tea, and a hero at the door.
"""

import os

ENTRY = (
    "Come in, hero. Mind the third step \u2014 it sighs louder than the gargoyles, "
    "and I've stopped oiling it. Yes, the crown is on the pedestal. "
    "I've spent forty years polishing this speech, and tonight the candles keep guttering, "
    "the ravens keep filing complaints, and my tea has gone cold again. "
    "So. Take the sword. Take the crown. Take the ledger too; the tithes are three winters behind "
    "and the goblins unionised. I'll be in the east tower, counting ceiling cracks, "
    "waiting for the next bright-eyed child with a destiny. Do hurry. The dramatic pause only works once."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
