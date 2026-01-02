# Execute command
# Undo command
# idempotent

# ln -sf /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime
# hwclock --systohc

# LOCALE="en_US.UTF-8"
# KEYMAP="de-latin1"
# sed -i "s/# $LOCALE/$LOCALE/" /etc/locale.gen
# locale-gen
# echo "LANG=$LOCALE" > /etc/locale.conf
# echo "KEYMAP=$KEYMAP" > /etc/vconsole.conf

# echo "victor" > /etc/hostname

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

# sudo sed -i 's/^#Color/Color/' /etc/pacman.conf
# sudo sed -i 's/^#ILoveCandy/ILoveCandy/' /etc/pacman.conf
# sudo sed -i 's/^#ParallelDownloads = 5/ParallelDownloads = 5/' /etc/pacman.conf
# sudo sed -i 's/^#DownloadUser = alpm/DownloadUser = alpm/' /etc/pacman.conf
# VerbosePkgLists

# systemctl --user unset-environment GTK_IM_MODULE
# systemctl --user show-environment | grep GTK_IM_MODULE

# sudo systemctl disable systemd-timesyncd
# sudo systemctl mask systemd-rfkill.service systemd-rfkill.socket
# sudo journalctl --vacuum-time=7d

# /etc/sysctl.d/99-desktop.conf
# vm.swappiness=10
# kernel.sched_autogroup_enabled=1
# fs.inotify.max_user_watches=524288


# sudo ln -s /usr/lib/systemd/system/cpupower.service /etc/systemd/system/multi-user.target.wants/
# sudo nano /etc/default/cpupower
# governor="performance" or "schedutil"

sudo pacman -Rns $(pacman -Qtdq)

~/.config/systemd/user/idle-cleanup.service
[Service]
Type=oneshot
ExecStart=/usr/bin/pkill -f chromium
systemctl --user enable idle-cleanup.timer


sudo nano /etc/systemd/logind.conf
HandleLidSwitch=suspend
HandleLidSwitchDocked=ignore


sudo pacman -S tlp
sudo systemctl enable tlp
CPU_ENERGY_PERF_POLICY_ON_BAT=power



systemd-analyze blame
systemctl status <service>
journalctl -xe

/boot/loader/entries/arch.conf
options mitigations=auto,nosmt
