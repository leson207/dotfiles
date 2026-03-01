sudo pacman -Rns $(pacman -Qtdq)

# systemctl preset sddm.service

# systemctl --user unset-environment GTK_IM_MODULE
# systemctl --user show-environment | grep GTK_IM_MODULE

# - name: Disable root SSH login
#   ansible.builtin.lineinfile:
#     path: /etc/ssh/sshd_config
#     regexp: '^#?PermitRootLogin'
#     line: 'PermitRootLogin no'
#     create: yes
#     backup: yes

# sudo systemctl mask systemd-rfkill.service systemd-rfkill.socket

# DRI_PRIME=1 code
# chromium --disable-backgrounding-occluded-windows \
--disable-background-timer-throttling \
    --disable-renderer-backgrounding

bash -c 'sudo pacman -Rns $(pacman -Qdtq)'
sudo rm -rf /var/cache/pacman/pkg/download-*
sudo pacman -Sc
