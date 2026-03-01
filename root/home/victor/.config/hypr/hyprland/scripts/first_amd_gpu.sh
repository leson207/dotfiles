#!/bin/bash
set -euo pipefail

ID=$(lspci -d 1002::03xx | awk '{print $1}' | head -n1)

UDEV_RULE=$(
    cat <<EOF
KERNEL=="card*", KERNELS=="0000:$ID", SUBSYSTEM=="drm", SUBSYSTEMS=="pci", SYMLINK+="dri/first-amd-gpu"
EOF
)

echo "$UDEV_RULE" | sudo tee /etc/udev/rules.d/99-first-amd-gpu.rules >/dev/null

# Reload and trigger
sudo udevadm control --reload
sudo udevadm trigger

echo "Symlink created: /dev/dri/first-amd-gpu"
echo "Verify with: ls -l /dev/dri/ | grep amd"
