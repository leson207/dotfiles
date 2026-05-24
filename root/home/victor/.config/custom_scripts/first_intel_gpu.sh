#!/bin/bash
set -euo pipefail

ID=$(lspci -d 8086::03xx | awk '{print $1}' | head -n1)

UDEV_RULE=$(
    cat <<EOF
KERNEL=="card*", KERNELS=="0000:$ID", SUBSYSTEM=="drm", SUBSYSTEMS=="pci", SYMLINK+="dri/first-intel-gpu"
EOF
)

echo "$UDEV_RULE" | sudo tee /etc/udev/rules.d/99-first-intel-gpu.rules >/dev/null

# Reload and trigger
sudo udevadm control --reload
sudo udevadm trigger

echo "Symlink created: /dev/dri/first-intel-gpu"
echo "Verify with: ls -l /dev/dri/ | grep intel"
