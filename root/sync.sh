#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 [pull|push]"
    exit 1
fi

MODE="$1"

# Files relative to /
sources=(
    "boot/loader/entries/arch.conf"
    "boot/loader/entries/arch-zen.conf"
)

LOCAL_ROOT="/home/victor/dotfiles/root"
SYSTEM_ROOT="/"

tmpfile=$(mktemp)
printf "%s\n" "${sources[@]}" >"$tmpfile"

case "$MODE" in
pull)
    SRC="$SYSTEM_ROOT"
    DEST="$LOCAL_ROOT"
    ;;
push)
    SRC="$LOCAL_ROOT"
    DEST="$SYSTEM_ROOT"
    ;;
*)
    echo "Invalid mode: $MODE"
    echo "Usage: $0 [pull|push]"
    rm -f "$tmpfile"
    exit 1
    ;;
esac

# Ensure local root exists when pulling
if [ "$MODE" = "pull" ]; then
    mkdir -p "$LOCAL_ROOT"
fi

sudo rsync -avh \
    --delete \
    --info=progress2 \
    --files-from="$tmpfile" \
    "$SRC" "$DEST"

rm -f "$tmpfile"
"$SRC" "$DEST"
