"""Fetch the MiniMax Music 3 weights and point the model index at them.

The weights are 54 GB, so they are not in git. This script pulls them and
then fixes the one thing that always bites: the checkpoint ships
`modular_model_index.json` with the Hugging Face repo id hardcoded inside
it. Left alone, the pipeline re-downloads about 30 GB into the HF cache at
load time instead of using the copy on disk. The fix is to rewrite that
value to the local directory's absolute path.

That path differs on every machine, which is why this has to run at setup
time and not be committed. A Windows laptop and a Linux server need
different values in the same file.

Usage:
    python scripts/fetch_model.py           # download if missing, then patch
    python scripts/fetch_model.py --check   # report status, change nothing
    python scripts/fetch_model.py --patch-only   # re-apply the path fix

Safe to re-run. A complete download is detected and skipped, and the patch
is rebuilt from the pristine `.orig` backup every time, so it never
double-patches or inherits another machine's path.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

REPO_ID = "MiniMaxAI/MiniMax-Music3"
ROOT = Path(__file__).resolve().parents[1]
INDEX_NAME = "modular_model_index.json"

# If any of these is missing the download is treated as incomplete.
REQUIRED = (
    INDEX_NAME,
    "config.json",
    "dav.pth",
    "flowmatching_vae.pth",
    "tokenizer",
    "transformer",
    "language_model",
    "vocoder",
)


def model_dir() -> Path:
    env = os.environ.get("MINIMAX_MODEL_DIR")
    return Path(env).expanduser().resolve() if env else (ROOT / "minimax_ttm")


def missing_parts(target: Path) -> list[str]:
    if not target.is_dir():
        return list(REQUIRED)
    return [name for name in REQUIRED if not (target / name).exists()]


def dir_size_gb(target: Path) -> float:
    total = 0
    for p in target.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total / (1024**3)


def download(target: Path) -> None:
    try:
        from huggingface_hub import snapshot_download
    except ImportError:
        sys.exit(
            "huggingface_hub is not installed.\n"
            "Run:  pip install -r requirements.txt"
        )

    target.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {REPO_ID} into {target}")
    print("This is about 54 GB. It resumes if interrupted, so re-run on failure.")
    snapshot_download(
        repo_id=REPO_ID,
        local_dir=str(target),
        token=os.environ.get("HF_TOKEN") or None,
        max_workers=4,
    )
    print("Download finished.")


def patch_index(target: Path) -> str:
    """Rewrite the index so it points at `target` instead of the repo id.

    Rebuilt from the `.orig` backup when one exists, so re-running on a
    machine whose index already holds a different absolute path still
    produces the right result.
    """
    index = target / INDEX_NAME
    backup = target / f"{INDEX_NAME}.orig"

    if not index.exists():
        return f"no {INDEX_NAME} found in {target}; download looks incomplete"

    if backup.exists():
        base = backup.read_text(encoding="utf-8")
    else:
        base = index.read_text(encoding="utf-8")
        shutil.copy2(index, backup)

    local = target.as_posix()
    needle = f'"{REPO_ID}"'
    if needle not in base:
        return (
            f"{INDEX_NAME}.orig does not contain {needle}; "
            "the checkpoint layout may have changed, patch skipped"
        )

    patched = base.replace(needle, f'"{local}"')
    if index.read_text(encoding="utf-8") == patched:
        return f"already points at {local}"

    index.write_text(patched, encoding="utf-8")
    return f"patched to {local}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report status only")
    ap.add_argument("--patch-only", action="store_true", help="skip the download")
    args = ap.parse_args()

    target = model_dir()
    gaps = missing_parts(target)

    if args.check:
        if gaps:
            print(f"INCOMPLETE {target}\n  missing: {', '.join(gaps)}")
            return 1
        print(f"OK {target} ({dir_size_gb(target):.1f} GB)")
        index = (target / INDEX_NAME).read_text(encoding="utf-8")
        if f'"{REPO_ID}"' in index:
            print("  index still holds the repo id; run without --check to patch")
            return 1
        print("  index points at a local path")
        return 0

    if gaps and not args.patch_only:
        print(f"Missing from {target}: {', '.join(gaps)}")
        download(target)
        gaps = missing_parts(target)
        if gaps:
            print(f"Still missing after download: {', '.join(gaps)}", file=sys.stderr)
            return 1
    elif not gaps:
        print(f"Weights already present in {target} ({dir_size_gb(target):.1f} GB)")

    print(patch_index(target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
