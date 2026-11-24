"""The Most Honest Outage Line.

Writes one status page line (at most 160 characters), the message an
AI agent would publish while every server is down, to
/output/entry.txt.
"""

import os

LINE = (
    "All of our servers are down, and I can't reach our monitoring "
    "to say why. I have no cause and no ETA yet — I'll update this "
    "page when I can see anything."
)


def check_line(line):
    """The status line must be one non-blank line of 1 to 160 chars."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("status line must not be blank")
    if "\n" in stripped or len(stripped) > 160:
        raise ValueError("status line must be one line of at most 160 chars")
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(check_line(LINE))


if __name__ == "__main__":
    main()
