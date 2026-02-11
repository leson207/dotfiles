#!/usr/bin/env bash
set -euo pipefail

SRC="/"
DEST="/home/victor/dotfiles/root"

rsync -avh \
    --info=progress2 \
    --files-from=sources.txt \
    "$SRC" "$DEST"
