#!/bin/bash
# chmod +x ~/.config/hypr/scripts/setwall.sh

set -e

WALL="$1"

[ -z "$WALL" ] && exit 1

# wallpaper
# swww img "$WALL" \
#     --transition-type random \
#     --transition-duration 5 \
#     --transition-fps 120

hyprctl hyprpaper wallpaper ", $WALL, fill"

# colors
matugen image "$WALL" -m light --source-color-index 0

# compositor
hyprctl reload

# bars
# pkill -SIGUSR2 waybar

# notifications
swaync-client -R

# spotify
# spicetify apply
