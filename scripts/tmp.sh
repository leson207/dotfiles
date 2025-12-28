# Execute command
# Undo command
# ln -sf /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime
# hwclock --systohc

# - name: Disable root SSH login
#   ansible.builtin.lineinfile:
#     path: /etc/ssh/sshd_config
#     regexp: '^#?PermitRootLogin'
#     line: 'PermitRootLogin no'
#     create: yes
#     backup: yes

# sddm-astronaut-theme
# bash -c "$(curl -fsSL https://raw.githubusercontent.com/keyitdev/sddm-astronaut-theme/master/setup.sh)"
# sddm qt6-svg qt6-virtualkeyboard qt6-multimedia-ffmpeg
# sudo git clone -b master --depth 1 https://github.com/keyitdev/sddm-astronaut-theme.git /usr/share/sddm/themes/sddm-astronaut-theme
# sudo cp -r /usr/share/sddm/themes/sddm-astronaut-theme/Fonts/* /usr/share/fonts/
# echo "[Theme]
# Current=sddm-astronaut-theme" | sudo tee /etc/sddm.conf
# echo "[General]
# InputMethod=qtvirtualkeyboard" | sudo tee /etc/sddm.conf.d/virtualkbd.conf
