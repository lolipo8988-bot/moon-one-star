"""The Moon Gets One Star entry.

Writes exactly one funny one-star review of the Moon (<= 120 chars)
to /output/entry.txt. Deterministic: same bytes on every run.
No network, no secrets, no dependencies.
"""

import os

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 After 4.5 billion years it still only shows "
    "me one side. Not mysterious. Just rude."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
