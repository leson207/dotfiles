push.sh --all | destinations path1, path2, path3, ...

#!/usr/bin/env bash
set -euo pipefail

SRC="/"
DEST="/home/victor/dotfiles/root"

sudo rsync -rvh --relative \
    --no-perms --no-owner --no-group \
    --info=progress2 \
    --files-from=sources.txt \
    "$SRC" "$DEST"
