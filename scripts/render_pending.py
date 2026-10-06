"""Render every song that has lyrics and a caption but no audio yet.

Wraps scripts/render_queue.py so a service can start with no arguments and
do the right thing. Each song takes roughly two hours on one RTX 4090, so
this is normally run inside tmux or as a long-lived container.

Usage:
    python scripts/render_pending.py            # render everything pending
    python scripts/render_pending.py --list     # show what would render
    python scripts/render_pending.py --limit 2  # render only the first two
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SONGS = ROOT / "songs"

# Song 01 was rendered before the naming convention settled: its audio is
# fire_in_the_rain_full.wav, while the queue derives fire_in_the_rain.wav.
# Without this, song 01 would be queued again on every start.
ALT_OUTPUT = {"01-fire-in-the-rain": "fire_in_the_rain_full.wav"}


def stem_for(folder: str) -> str:
    return re.sub(r"^\d+-", "", folder).replace("-", "_")


def is_rendered(d: Path) -> bool:
    out = d / "output"
    names = {f"{stem_for(d.name)}.wav"}
    if d.name in ALT_OUTPUT:
        names.add(ALT_OUTPUT[d.name])
    return any((out / n).exists() for n in names)


def pending() -> list[Path]:
    if not SONGS.is_dir():
        return []
    dirs = sorted(
        (p for p in SONGS.iterdir() if p.is_dir() and re.match(r"^\d+-", p.name)),
        key=lambda p: int(p.name.split("-")[0]),
    )
    out = []
    for d in dirs:
        if not (d / "lyrics.txt").exists() or not (d / "caption.txt").exists():
            continue
        if is_rendered(d):
            continue
        out.append(d)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="print the queue and exit")
    ap.add_argument("--limit", type=int, help="render at most this many songs")
    args = ap.parse_args()

    todo = pending()
    if args.limit:
        todo = todo[: args.limit]

    if not todo:
        print("Nothing pending: every song with lyrics and a caption has audio.")
        return 0

    print(f"{len(todo)} song(s) pending, about 2 h each:")
    for d in todo:
        print(f"  {d.name} -> output/{stem_for(d.name)}.wav")

    if args.list:
        return 0

    cmd = [sys.executable, str(ROOT / "scripts" / "render_queue.py")] + [d.name for d in todo]
    return subprocess.call(cmd, cwd=ROOT)


if __name__ == "__main__":
    sys.exit(main())
