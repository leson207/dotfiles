sudo pacman -Rns $(pacman -Qtdq)

# systemctl preset sddm.service

# systemctl --user unset-environment GTK_IM_MODULE
# systemctl --user show-environment | grep GTK_IM_MODULE

/boot/loader/entries/arch.conf
options mitigations=auto,nosmt

# - name: Disable root SSH login
#   ansible.builtin.lineinfile:
#     path: /etc/ssh/sshd_config
#     regexp: '^#?PermitRootLogin'
#     line: 'PermitRootLogin no'
#     create: yes
#     backup: yes

# sudo systemctl mask systemd-rfkill.service systemd-rfkill.socket
