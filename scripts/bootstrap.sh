#!/usr/bin/env bash
# Set the project up on a bare Linux host: virtualenv, dependencies, weights.
#
# Use this when Docker is not available, which includes any machine where you
# have no root. It needs nothing but python3, git and a CUDA driver.
#
#   bash scripts/bootstrap.sh
#
# Then render inside tmux, because each song takes about two hours:
#
#   tmux new -s render
#   . .venv/bin/activate && python scripts/render_pending.py
#   # detach with Ctrl+B then D
set -euo pipefail

cd "$(dirname "$0")/.."
ROOT="$PWD"
echo "[bootstrap] project: $ROOT"

if ! command -v python3 >/dev/null; then
  echo "[bootstrap] python3 not found." >&2
  exit 1
fi
echo "[bootstrap] python: $(python3 --version)"

if [ ! -d .venv ]; then
  echo "[bootstrap] creating .venv"
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
. .venv/bin/activate

python -m pip install --upgrade pip

# Torch must come from the CUDA index and must be installed before the rest,
# or pip resolves a CPU-only build and the render silently has no GPU.
if ! python -c "import torch" 2>/dev/null; then
  echo "[bootstrap] installing torch (cu126)"
  pip install torch --index-url https://download.pytorch.org/whl/cu126
fi

echo "[bootstrap] installing requirements"
pip install -r requirements.txt

if [ ! -f .env ] && [ -f .env.example ]; then
  cp .env.example .env
  echo "[bootstrap] wrote .env from .env.example; edit it if the defaults are wrong"
fi

# Weights: about 54 GB, not in git. Resumable, so re-run on a failed download.
echo "[bootstrap] checking model weights"
python scripts/fetch_model.py

echo "[bootstrap] verifying GPU visibility"
python - <<'PY'
import torch
if torch.cuda.is_available():
    print(f"[bootstrap] CUDA ok: {torch.cuda.get_device_name(0)}")
else:
    print("[bootstrap] WARNING: torch cannot see a GPU. A render needs one card, about 7 GB.")
PY

echo
echo "[bootstrap] done. Pending renders:"
python scripts/render_pending.py --list || true
echo
echo "Start rendering:  . .venv/bin/activate && python scripts/render_pending.py"
echo "Check a song:     . .venv/bin/activate && python scripts/audit_catalogue.py --no-verify"
