#!/usr/bin/env bash
set -euo pipefail

SRC="/home/victor/dotfiles/root"
DEST="/"

read -rp "Do you want to continue? [y/n]: " answer

case "$answer" in
[Yy])
    echo "✅ Continuing..."
    ;;
[Nn] | "")
    echo "❌ Cancelled."
    exit 1
    ;;
*)
    echo "⚠ Invalid input. Please enter y or n."
    exit 1
    ;;
esac

sudo rsync -rvh --relative \
    --no-perms --no-owner --no-group \
    --info=progress2 \
    --files-from=destinations.txt \
    "$SRC" "$DEST"
