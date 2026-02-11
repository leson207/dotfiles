#!/usr/bin/env bash
# chmod +x ~/.config/hypr/scripts/wallpaper-selector.sh

WALLDIR="$HOME/.config/hypr/wallpaper"
SETWALL="$HOME/.config/hypr/scripts/setwall.sh"
THEME="$HOME/.config/rofi/wallpaper.rasi"

entries=()

while IFS= read -r img; do
    name="$(basename "$img")"
    entries+=("$name\0icon\x1f$img")
done < <(
    find "$WALLDIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.webp" \) | sort
)

choice=$(printf '%b\n' "${entries[@]}" |
    rofi -dmenu \
        -show-icons \
        -format s \
        -theme "$THEME")

# 👇 prepend wallpaper directory
[ -n "$choice" ] && "$SETWALL" "$WALLDIR/$choice"
