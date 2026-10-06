# Torch's cu126 wheels bundle the CUDA runtime they need, so a plain Python
# base is enough. Only the host NVIDIA driver has to be visible, which the
# container runtime provides.
FROM python:3.12-slim

# git is required at install time: requirements.txt pins diffusers to a
# commit on GitHub, because the MiniMax Music 3 pipeline is not in a
# released diffusers yet.
RUN apt-get update \
 && apt-get install -y --no-install-recommends git ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies before copying the project so edits to songs or
# scripts do not invalidate the slowest layer.
COPY requirements.txt ./
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cu126 \
 && pip install --no-cache-dir -r requirements.txt

COPY . .

# Weights land in a mounted volume, not in the image. A 54 GB image would
# be unusable, and the download resumes across restarts this way.
ENV MINIMAX_MODEL_DIR=/models/minimax_ttm \
    HF_HOME=/models/hf \
    PYTHONUNBUFFERED=1

RUN chmod +x docker/entrypoint.sh

ENTRYPOINT ["docker/entrypoint.sh"]
CMD ["python", "scripts/render_pending.py"]
