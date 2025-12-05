#!/bin/bash

# Wallpaper directory
WALLPAPER_DIR="$HOME/Pictures/Wallpapers"

# Select random wallpaper
WALLPAPER=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" \) | shuf -n 1)

if [ -z "$WALLPAPER" ]; then
    echo "No se encontraron wallpapers en $WALLPAPER_DIR"
    exit 1
fi

# Set the wallpaper for GNOME (light and dark mode)
if ! gsettings set org.gnome.desktop.background picture-uri "file://$WALLPAPER"; then
    echo "Error: Failed to set wallpaper (light mode)"
    exit 1
fi

if ! gsettings set org.gnome.desktop.background picture-uri-dark "file://$WALLPAPER"; then
    echo "Error: Failed to set wallpaper (dark mode)"
    exit 1
fi

echo "Wallpaper set successfully: $WALLPAPER"
