"""Render a queue of song folders one after another, unattended.

Runs each song through scripts/generate.py as a subprocess, logs to
songs/<song>/logs/render.log, appends a status line to render_queue.status,
and ticks TODO.md. A failure in one song does not stop the queue. Songs whose
output WAV already exists are skipped, so the queue is safe to re-run.

Usage (from repo root, detached):
    .venv\\Scripts\\python.exe scripts\\render_queue.py
"""

from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = ROOT / ".venv" / "Scripts" / "python.exe"
STATUS = ROOT / "render_queue.status"
TODO = ROOT / "TODO.md"
VOICE_REF = ROOT / "songs" / "01-fire-in-the-rain"
# The female lead of songs 01-100 is locked to song 01. Songs 101-105 are a
# male voice family with its own lock, defined by song 101. Each family is
# verified against its own reference; mixing them fails pre-flight by design.
MALE_FAMILY_REF = ROOT / "songs" / "101-the-day-you-found-me"
MALE_FAMILY_NUMBERS = {"101", "102", "103", "104", "105"}


def voice_ref_for(song: str) -> Path:
    """The voice-lock reference a song must match before it may render."""
    return MALE_FAMILY_REF if song.split("-")[0] in MALE_FAMILY_NUMBERS else VOICE_REF

QUEUE = [
    ("02-someone-elses-forever", "someone_elses_forever"),
    ("03-hey-stranger", "hey_stranger"),
    ("04-polaroids-in-my-pocket", "polaroids_in_my_pocket"),
    ("05-last-train-home", "last_train_home"),
]


def log(line: str) -> None:
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with STATUS.open("a", encoding="utf-8") as f:
        f.write(f"{stamp} {line}\n")
    print(f"{stamp} {line}", flush=True)


def mark_todo(song: str, mark: str, note: str = "") -> None:
    if not TODO.exists():
        return
    text = TODO.read_text(encoding="utf-8")
    pattern = re.compile(rf"^- \[[ x!~]\] (`songs/{re.escape(song)}`.*)$", re.M)
    suffix = f" — {note}" if note else ""
    text, n = pattern.subn(lambda m: f"- [{mark}] {m.group(1).split(' — ')[0]}{suffix}", text)
    if n:
        TODO.write_text(text, encoding="utf-8")


def queue_from_args(args: list[str]) -> list[tuple[str, str]]:
    """Song folder names on the command line override the default QUEUE.
    The WAV stem is the folder name without its NN- prefix, hyphens -> underscores."""
    out = []
    for a in args:
        name = Path(a).name
        stem = re.sub(r"^\d+-", "", name).replace("-", "_")
        out.append((name, stem))
    return out


def main() -> int:
    queue = queue_from_args(sys.argv[1:]) or QUEUE
    log("QUEUE_START " + " ".join(s for s, _ in queue))
    for song, stem in queue:
        song_dir = ROOT / "songs" / song
        out = song_dir / "output" / f"{stem}.wav"
        logs = song_dir / "logs"
        logs.mkdir(exist_ok=True)

        if out.exists():
            log(f"SKIP {song} output already exists")
            mark_todo(song, "x", "already rendered")
            continue

        log(f"START {song}")
        mark_todo(song, "~", "rendering")

        verify = subprocess.run(
            [str(PY), str(ROOT / "scripts" / "verify_lyrics.py"), str(song_dir), "--voice-ref", str(voice_ref_for(song))],
            capture_output=True, text=True, cwd=ROOT,
        )
        (logs / "verify.log").write_text(verify.stdout + verify.stderr, encoding="utf-8")
        if verify.returncode != 0:
            log(f"FAIL {song} pre-flight verify failed (see logs/verify.log)")
            mark_todo(song, "!", "verify failed")
            continue

        t0 = time.time()
        with (logs / "render.log").open("w", encoding="utf-8") as lf:
            result = subprocess.run(
                [
                    str(PY), "-u", str(ROOT / "scripts" / "generate.py"),
                    "--prompt-file", str(song_dir / "caption.txt"),
                    "--lyrics-file", str(song_dir / "lyrics.txt"),
                    "--duration", "355", "--seed", "42",
                    "--out", str(out),
                ],
                stdout=lf, stderr=subprocess.STDOUT, cwd=ROOT,
            )
        elapsed = int(time.time() - t0)

        if result.returncode == 0 and out.exists():
            log(f"DONE {song} {elapsed}s")
            mark_todo(song, "x", f"rendered in {elapsed // 60} min")
        else:
            log(f"FAIL {song} exit={result.returncode} after {elapsed}s (see logs/render.log)")
            mark_todo(song, "!", f"failed after {elapsed // 60} min")

    log("QUEUE_COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
