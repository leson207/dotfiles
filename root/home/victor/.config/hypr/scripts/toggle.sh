#!/bin/sh
hyprctl dispatch togglespecialworkspace magic
hyprctl dispatch movetoworkspacesilent +0
hyprctl dispatch togglespecialworkspace magic
hyprctl dispatch movetoworkspacesilent special:magic
hyprctl dispatch togglespecialworkspace magic
