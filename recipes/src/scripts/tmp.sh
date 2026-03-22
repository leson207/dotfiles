bash -c 'sudo pacman -Rns $(pacman -Qdtq)'
sudo rm -rf /var/cache/pacman/pkg/download-*
sudo pacman -Sc

# systemctl preset sddm.service

# - name: Disable root SSH login
#   ansible.builtin.lineinfile:
#     path: /etc/ssh/sshd_config
#     regexp: '^#?PermitRootLogin'
#     line: 'PermitRootLogin no'
#     create: yes
#     backup: yes

# sudo systemctl mask systemd-rfkill.service systemd-rfkill.socket

# chromium --disable-backgrounding-occluded-windows --disable-background-timer-throttling --disable-renderer-backgrounding

# reload all service
systemctl daemon-reload
systemctl --user daemon-reload

# turn amd gpu off
sudo modprobe acpi_call
echo '\_SB.PCI0.RP01.PEGP._OFF' | sudo tee /proc/acpi/call
cat /sys/bus/pci/devices/0000:01:00.0/power/control

# check gpu
# lspci | grep -E "VGA|3D"
# glxinfo | grep renderer
# lspci -k | grep -A3 VGA
# glxinfo | grep "OpenGL renderer"
# DRI_PRIME=1 glxinfo | grep "OpenGL renderer"
