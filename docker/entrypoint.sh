#!/usr/bin/env bash
# Container entrypoint: make sure the big files exist, then run the command.
#
# The 54 GB of weights are not in git and not in the image. They are fetched
# here, on first start, into the mounted volume. On every later start the
# download is detected as complete and only the model-index path fix is
# re-applied, which is cheap and must happen because that path is
# machine-specific.
set -euo pipefail

echo "[entrypoint] model dir: ${MINIMAX_MODEL_DIR:-./minimax_ttm}"

if ! python scripts/fetch_model.py --check >/dev/null 2>&1; then
  echo "[entrypoint] weights missing or unpatched, fetching now."
  echo "[entrypoint] first run downloads about 54 GB and will take a while."
  python scripts/fetch_model.py
else
  # Present, but the index may still carry another machine's absolute path.
  python scripts/fetch_model.py --patch-only
fi

python scripts/fetch_model.py --check

if ! python -c "import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null; then
  echo "[entrypoint] WARNING: no CUDA device visible to the container."
  echo "[entrypoint] A render needs one GPU with about 7 GB free; it will fail or crawl on CPU."
fi

echo "[entrypoint] starting: $*"
exec "$@"
