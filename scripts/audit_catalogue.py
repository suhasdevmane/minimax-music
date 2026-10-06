"""Audit every song folder under songs/ against the template and the model limits.

Usage:
    .venv\\Scripts\\python.exe scripts\\audit_catalogue.py            # all songs
    .venv\\Scripts\\python.exe scripts\\audit_catalogue.py 09 10 57   # by number prefix
    .venv\\Scripts\\python.exe scripts\\audit_catalogue.py --no-verify  # skip the slow tokenizer check

Checks per song:
  - required files present (README, caption, lyrics, submission, shot list, output/ and logs/)
  - sung-word count inside the pacing class range (600-640 ballad, 700-760 uptempo with render.json)
  - no character name, no "(repeat)", no quotation marks or em-dashes, no digits in lyrics
  - section tags from the allowed set, alone on their line, exactly one [instrumental]
  - README's fenced lyrics block is identical to lyrics.txt
  - shot list has one numbered entry for every lyric line (plus the instrumental shots)
  - voice-lock blocks byte-identical to song 01
  - duets and male-feature songs declare Duet Partner + Duet Structure
  - caption + lyrics under the 5000-token prompt limit (unless --no-verify)
Across songs:
  - no lyric line (>= 5 words) shared verbatim between two songs
  - no duplicate titles
"""

from __future__ import annotations

import re

import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SONGS = ROOT / "songs"
PY = ROOT / ".venv" / "Scripts" / "python.exe"
REF = SONGS / "01-fire-in-the-rain" / "caption.txt"
CATALOGUE = SONGS / "CATALOGUE.md"
REF_MALE = (SONGS / "101-the-day-you-found-me" / "caption.txt")
MALE_FAMILY = {"101", "102", "103", "104", "105"}

ALLOWED_TAGS = {"[intro]", "[verse]", "[pre-chorus]", "[chorus]", "[post-chorus]", "[instrumental]", "[bridge]", "[outro]"}
NAME = "mahima"

# Songs 01-08 were written before docs/SONG_TEMPLATE.md existed and most are
# already rendered. They are still checked, but their findings are reported
# as informational and do not fail the run: re-cutting a rendered song to a
# later template would mean burning two GPU hours to change nothing a
# listener hears. The character-name rule is the exception -- it applies to
# every song, legacy included, and still fails.
LEGACY = {f"{n:02d}" for n in range(1, 9)}
ALWAYS_FAIL = ("character name",)

MAX_TOKENS = 5000
SINGER_B: dict[str, str] = {}
# Anything but tab and newline. Real control bytes in a text file mean an
# escape sequence was interpreted when the file was written.
CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
TOKENIZER_DIR = ROOT / "minimax_ttm" / "tokenizer"

_tokenizer: object | None = None
_tokenizer_tried = False


def get_tokenizer():
    """Load the checkpoint tokenizer once per run, or None if unavailable."""
    global _tokenizer, _tokenizer_tried
    if not _tokenizer_tried:
        _tokenizer_tried = True
        try:
            from transformers import AutoTokenizer

            _tokenizer = AutoTokenizer.from_pretrained(str(TOKENIZER_DIR))
        except Exception:
            _tokenizer = None
    return _tokenizer


def songs_needing_singer_b() -> dict[str, str]:
    """Song numbers whose caption must declare a second singer.

    Two sources in songs/CATALOGUE.md: briefs tagged **duet**, and rows of
    the rap-and-delivery map that assign a male feature. A song where only
    the female lead raps does NOT need Singer B -- that is one voice.
    """
    out: dict[str, str] = {}
    cat = CATALOGUE.read_text(encoding="utf-8") if CATALOGUE.exists() else ""
    for m in re.finditer(r"^### (\d+) .*$", cat, re.M):
        number = m.group(1)
        brief = cat[m.end() : cat.find("\n### ", m.end())]
        if "**duet**" in brief.lower():
            out[number] = "duet"
    for m in re.finditer(r"^\| (\d+) [^|]*\| ([^|]*)\|", cat, re.M):
        number, treatment = m.group(1), m.group(2).lower()
        if "male" in treatment:
            out.setdefault(number, treatment.strip())
    return out


def block(text: str, start: str, end: str) -> str:
    i = text.index(start)
    return text[i : text.index(end, i)]


def sung_words(lyrics: str) -> int:
    return len(lyrics.split()) - lyrics.count("[")


def audit_song(d: Path, ref: str, run_verify: bool) -> list[str]:
    problems: list[str] = []
    need = ["README.md", "caption.txt", "lyrics.txt", "source/original-submission.md", "video/wan22-shot-list.md"]
    missing = [f for f in need if not (d / f).exists()]
    if missing:
        problems.append(f"missing files: {missing}")
    for sub in ("output", "logs"):
        if not (d / sub).is_dir():
            problems.append(f"missing dir {sub}/")
    if "lyrics.txt" in missing:
        return problems

    lyrics = (d / "lyrics.txt").read_text(encoding="utf-8")
    lines = [l for l in lyrics.splitlines()]
    lyric_lines = [l for l in lines if l.strip() and not l.strip().startswith("[")]
    tags = [l.strip() for l in lines if l.strip().startswith("[")]

    uptempo = (d / "render.json").exists()
    words = sung_words(lyrics)
    lo, hi = (700, 760) if uptempo else (600, 640)
    if not (lo <= words <= hi):
        problems.append(f"words {words} outside {lo}-{hi} ({'uptempo' if uptempo else 'ballad'})")

    if NAME in lyrics.lower():
        problems.append("character name in lyrics")
    if re.search(r"\(\s*repeat", lyrics, re.I):
        problems.append("'(repeat)' in lyrics")
    if re.search(r'["“”—]', lyrics):
        problems.append("quotation marks or em-dash in lyrics")
    if re.search(r"\d", lyrics):
        problems.append("digits in lyrics")
    if any(re.fullmatch(r"\s*\(.*\)\s*", l) for l in lines):
        problems.append("parenthesis-only line in lyrics")
    bad = [t for t in tags if t not in ALLOWED_TAGS]
    if bad:
        problems.append(f"unknown tags {bad}")
    # A song may have no instrumental section (songs 103-105 do not), but never more than one.
    if tags.count("[instrumental]") > 1:
        problems.append(f"{tags.count('[instrumental]')} [instrumental] sections (max 1)")

    cap = ""
    if (d / "caption.txt").exists():
        cap = (d / "caption.txt").read_text(encoding="utf-8")
        if NAME in cap.lower():
            problems.append("character name in caption")
        try:
            # 101-105 are a male family, checked against their own reference.
            fam_ref = REF_MALE if d.name.split("-")[0] in MALE_FAMILY else ref
            s, e = "Sonics & Production Profile:", "\nVocal Details"
            if block(fam_ref, s, e) != block(cap, s, e):
                problems.append("Sonics block differs from song 01")
            s, e = "Vocal Details\n", "\nArrangement"
            ref_lines = [l for l in block(fam_ref, s, e).splitlines() if l.strip() and l.strip() != "Vocal Details"]
            cb = block(cap, s, e)
            miss = [l.split(":")[0] for l in ref_lines if l not in cb]
            if miss:
                problems.append(f"Vocal Details lines changed: {miss}")
        except ValueError as exc:
            problems.append(f"caption structure: {exc}")

        reason = SINGER_B.get(d.name.split("-")[0])
        if reason:
            for field in ("Duet Partner:", "Duet Structure:"):
                if field not in cap:
                    problems.append(f"caption missing '{field}' ({reason})")

    if (d / "README.md").exists():
        rd = (d / "README.md").read_text(encoding="utf-8")
        m = re.search(r"## Lyrics as they will be sung\s*```\n(.*?)```", rd, re.S)
        if not m:
            problems.append("README has no lyrics block")
        elif m.group(1).strip() != lyrics.strip():
            problems.append("README lyrics block differs from lyrics.txt")

        # The render commands must survive intact. A README written through a
        # non-raw Python string eats the Windows separators as escapes
        # (songs\16-... -> a control char, songs\12-... -> a newline), which
        # silently produces an unrunnable command and a WAV the queue will
        # never find. Legacy songs 01-08 predate this wording.
        if d.name.split("-")[0] not in LEGACY:
            stem = re.sub(r"^\d+-", "", d.name).replace("-", "_")
            for want in (
                f"scripts\\render_queue.py {d.name}",
                f"--out songs\\{d.name}\\output\\{stem}.wav",
            ):
                if want not in rd:
                    problems.append(f"README render command wrong or corrupted: missing '{want}'")
                    break

    for f in ("README.md", "caption.txt", "lyrics.txt"):
        p = d / f
        if p.exists() and CONTROL_CHARS.search(p.read_text(encoding="utf-8")):
            problems.append(f"{f} contains control characters")

    sl = d / "video" / "wan22-shot-list.md"
    if sl.exists():
        st = sl.read_text(encoding="utf-8")
        entries = re.findall(r"^\d+\.\s", st, re.M)
        if len(entries) < len(lyric_lines):
            problems.append(f"shot list has {len(entries)} entries for {len(lyric_lines)} lyric lines")

    if run_verify and (d / "caption.txt").exists():
        # Token count against the 5000-token prompt limit. The tokenizer is
        # loaded once per run (see get_tokenizer) rather than by spawning
        # verify_lyrics.py per song -- that spawn reloaded transformers each
        # time and made a full-catalogue run take longer than any sane timeout.
        tok = get_tokenizer()
        if tok is None:
            problems.append("tokens: tokenizer unavailable")
        else:
            n = len(tok(cap + lyrics).input_ids)
            if n >= MAX_TOKENS:
                problems.append(f"tokens {n} over {MAX_TOKENS}")
    return problems


def main() -> int:
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if flags - {"--no-verify"}:
        # Anything unrecognised (including --help) prints usage instead of
        # silently falling through to a full verified run of the catalogue.
        print(__doc__)
        return 0 if "--help" in flags or "-h" in flags else 2
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    run_verify = "--no-verify" not in flags
    global SINGER_B
    SINGER_B = songs_needing_singer_b()
    ref = REF.read_text(encoding="utf-8")
    global REF_MALE
    REF_MALE = REF_MALE.read_text(encoding="utf-8")
    dirs = sorted([p for p in SONGS.iterdir() if p.is_dir() and re.match(r"^\d+-", p.name)], key=lambda p: int(p.name.split("-")[0]))
    if args:
        dirs = [p for p in dirs if p.name.split("-")[0] in args]

    total_problems = 0
    legacy_notes = 0
    seen_lines: dict[str, str] = {}
    dup: list[str] = defaultdict(list)  # type: ignore[assignment]
    titles: dict[str, str] = {}
    for d in dirs:
        probs = audit_song(d, ref, run_verify)
        lp = d / "lyrics.txt"
        if lp.exists():
            for l in lp.read_text(encoding="utf-8").splitlines():
                key = re.sub(r"[^a-z' ]", "", l.lower()).strip()
                if len(key.split()) >= 5:
                    if key in seen_lines and seen_lines[key] != d.name:
                        dup[key].append((seen_lines[key], d.name))  # type: ignore[index]
                    else:
                        seen_lines.setdefault(key, d.name)
        rp = d / "README.md"
        if rp.exists():
            first = rp.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip().lower()
            if first in titles:
                probs.append(f"title duplicates {titles[first]}")
            titles[first] = d.name
        is_legacy = d.name.split("-")[0] in LEGACY
        if is_legacy:
            # Legacy findings are notes, except the ones that always fail.
            hard = [p for p in probs if p.startswith(ALWAYS_FAIL)]
            soft = [p for p in probs if p not in hard]
            status = "BAD" if hard else ("OLD" if soft else "OK ")
            print(f"[{status}] {d.name}" + (" (pre-template)" if soft else ""))
            for p in hard:
                print(f"      - {p}")
            for p in soft:
                print(f"      ~ {p}")
            total_problems += len(hard)
            legacy_notes += len(soft)
        else:
            status = "OK " if not probs else "BAD"
            print(f"[{status}] {d.name}")
            for p in probs:
                print(f"      - {p}")
            total_problems += len(probs)

    if dup:
        print("\nLyric lines shared between songs:")
        for key, pairs in dup.items():
            for a, b in pairs:
                print(f"  {a} / {b}: \"{key}\"")
        total_problems += len(dup)

    note = f", {legacy_notes} pre-template notes on songs 01-08" if legacy_notes else ""
    print(f"\n{len(dirs)} songs audited, {total_problems} problems{note}")
    return 0 if total_problems == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
