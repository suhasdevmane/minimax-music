"""Tick songs/CATALOGUE.md's checklist from what is actually on disk.

Usage:
    .venv\\Scripts\\python.exe scripts\\update_checklist.py          # write
    .venv\\Scripts\\python.exe scripts\\update_checklist.py --dry-run

A song is ticked `[x]` only when its folder holds all five required files
(README.md, caption.txt, lyrics.txt, source/original-submission.md,
video/wan22-shot-list.md). Anything less stays `[ ]`. Idempotent: safe to
re-run at any point while songs are still being written.

This only reflects state; it never edits a song. Run
scripts/audit_catalogue.py for the checks that decide whether a song is
actually correct.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SONGS = ROOT / "songs"
CATALOGUE = SONGS / "CATALOGUE.md"

REQUIRED = (
    "README.md",
    "caption.txt",
    "lyrics.txt",
    "source/original-submission.md",
    "video/wan22-shot-list.md",
)


def complete(number: str) -> bool:
    matches = [p for p in SONGS.iterdir() if p.is_dir() and p.name.split("-")[0] == number]
    if not matches:
        return False
    d = matches[0]
    return all((d / f).exists() for f in REQUIRED)


def main() -> int:
    dry = "--dry-run" in sys.argv
    text = CATALOGUE.read_text(encoding="utf-8")
    line_re = re.compile(r"^- \[([ x!])\] (\d+) (.*)$", re.M)

    ticked = untick = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal ticked, untick
        mark, number, title = m.group(1), m.group(2), m.group(3)
        done = complete(number)
        new = "x" if done else " "
        if new != mark:
            if done:
                ticked += 1
            else:
                untick += 1
        return f"- [{new}] {number} {title}"

    out = line_re.sub(repl, text)
    total = len(line_re.findall(out))
    done_now = sum(1 for m in line_re.finditer(out) if m.group(1) == "x")

    if not dry and out != text:
        CATALOGUE.write_text(out, encoding="utf-8")

    verb = "would tick" if dry else "ticked"
    print(f"{verb} {ticked}, cleared {untick}")
    print(f"checklist now {done_now}/{total} complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
