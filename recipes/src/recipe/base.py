from box import Box
from src.recipe.schema import Recipe, CORE, EXTRA, USER

x=Box()

x.sytemd_boot=Recipe(
    pkg=[
        ["linux-headers", CORE],
        # ["linux-cachyos-bore-headers", USER],

        ["linux-firmware", CORE],
        ["intel-ucode", EXTRA],

        ["booster", EXTRA],
    ],
    config=[
        "/etc/booster.yaml",
        "/etc/pacman.d/hooks/90-booster.hook",

        "/boot/loader/loader.conf",
        "/boot/loader/entries/linux.conf",
        "/boot/loader/entries/linux-cachyos-bore.conf",

        ["sudo", "bootctl", "install"],

        # /usr/share/libalpm/hooks
        ["sudo" "ln" "-sf" "/dev/null" "/etc/pacman.d/hooks/90-mkinitcpio-install.hook"],
        ["sudo" "ln" "-sf" "/dev/null" "/etc/pacman.d/hooks/60-mkinitcpio-remove.hook"],
        ["/usr/share/libalpm/scripts/mkinitcpio" "remove"],
        ["/usr/lib/booster/regenerate_images"],
    ]
)

x.time=Recipe(
    pkg=[
        # ["glibc", CORE],
        # ["systemd", CORE],
    ],
    config=[
        ["sudo", "systemctl", "enable", "systemd-timesyncd"],
        ["timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"],
        ["sudo", "timedatectl", "set-ntp", "true"],
        ["timedatectl", "set-local-rtc", "0"],
        ["sudo", "hwclock", "--systohc"],
        ["timedatectl", "status"],
    ],
)

x.locale=Recipe(
    pkg=[
        # ["glibc", CORE],
        # ["systemd", CORE],
    ],
    config=[
        ["sudo", "locale-gen", "en_US.UTF-8"],
        ["localectl", "set-locale", "LANG=en_US.UTF-8"]
    ],
)

x.official_mirror=Recipe(
    pkg=[
        ["rate-mirrors", EXTRA]
    ],
    config=[
        "/etc/pacman.d/hooks/rate-mirrors.hook",
        ["sudo", "rate-mirrors", "--entry-country", "VN", "--allow-root", "--protocol", "https", "--save", "/etc/pacman.d/mirrorlist", "arch"],
        ["sudo", "pacman", "-Syy"]
    ]
)

x.graphic=Recipe(
    pkg=[
        ["mesa", EXTRA],
        ["vulkan-intel", EXTRA],
        ["intel-media-driver", EXTRA],
    ],
    env=[
        ["LIBVA_DRIVER_NAME", "iHD"],
    ]
)

x.audio=Recipe(
    pkg=[
        ["pipewire", EXTRA],
        ["wireplumber", EXTRA],
        ["pipewire-pulse", EXTRA],
        ["pipewire-alsa", EXTRA],
    ],
    config=[
        ["sudo", "systemctl", "--user", "enable", "pipewire"],
        ["sudo", "systemctl", "--user", "enable", "wireplumber"],
        ["sudo", "systemctl", "--user", "enable", "pipewire-pulse"],
    ]
)

x.ssh=Recipe(
    pkg=[
        ["openssh", EXTRA],
    ],
)

x.firewall=Recipe(
    pkg=[
        ["ufw", EXTRA],
    ],
    config=[
        ["sudo", "systemctl", "enable", "ufw"],
        ["sudo", "ufw", "default", "deny", "incoming"],
        ["sudo", "ufw", "default", "allow", "outgoing"],
        ["sudo", "ufw", "allow", "51820/udp"],
        ["sudo", "ufw", "allow", "192.168.1.0/24"],
        ["sudo", "ufw", "enable"],
        # ["sudo", "ufw", "status", "verbose"]
    ]
)

x.network=Recipe(
    pkg=[
        # ["systemd", CORE],
        ["iwd", EXTRA],
        ["networkmanager", EXTRA],
        # ["networkmanager-iwd", USER],
    ],
    config=[
        "/etc/systemd/resolved.conf",
        "/etc/NetworkManager/conf.d/dns.conf",
        "/etc/NetworkManager/conf.d/wifi_backend.conf",

        ["ln", "-sf", "/run/systemd/resolve/stub-resolv.conf", "/etc/resolv.conf"],

        ["sudo", "systemctl", "enable", "systemd-resolved"],
        ["sudo", "systemctl", "enable", "NetworkManager"],

        # ["nmcli", "connection", "modify", "Co Phuong", "ipv4.dns", "1.1.1.1 8.8.8.8"],
        # ["nmcli", "connection", "modify", "Co Phuong", "ipv4.ignore-auto-dns", "yes"],
        # ["nmcli", "connection", "modify", "Co Phuong", "ipv6.ignore-auto-dns", "yes"],

        # ["sudo", "systemctl", "restart", "systemd-resolved"],
        # ["sudo", "systemctl", "restart", "NetworkManager"],

        # ["resolvectl", "status"],
        # ["resolvectl", "query", "google.com"],
        # ["curl", "-sL", "https://test.nextdns.io", "|", "jq"]
    ]
)

x.secret=Recipe(
    pkg=[
        # ["oo7", EXTRA],
        # ["libsecret", EXTRA],
        ["gnome-keyring", EXTRA],
    ],
    config=[
        "busctl --user list | grep Secret"
        "busctl --user status org.freedesktop.secrets"
    ]
)

x.disk=Recipe(
    pkg=[
        ["util-linux", CORE]
    ],
    config=[
        ["sudo", "systemctl", "enable", "fstrim.timer"],
    ]
)

x.p2p=Recipe(
    pkg=[
        ["tlp", EXTRA],
        ["tlp-pd", EXTRA],
        ["thermal", EXTRA],
        # TODO: Uppower?
        # ls /etc/systemd/system/multi-user.target.wants/
        ["batsignal", EXTRA],
        ["irqbalance", EXTRA],
        ["ananicy-cpp", EXTRA],
        ["cachyos-ananicy-rules-git", USER]
    ],

    config=[
        ["sudo", "systemctl", "enable", "tlp"],
        ["sudo", "systemctl", "enable", "tlp-pd"],
        ["sudo", "systemctl", "enable", "thermal"],
        ["sudo", "systemctl", "enable", "batsignal"],
        ["sudo", "systemctl", "enable", "irqbalance"],
        ["sudo", "systemctl", "enable", "ananicy-cpp"],
    ]
)

x.input=Recipe(
    pkg=[
        ["fcitx5", EXTRA],
        ["fcitx5-gtk", EXTRA],
        ["fcitx5-unikey", EXTRA],
        ["fcitx5-configtool", EXTRA],
    ],
    config=[
        "~/.config/fcitx5",
        # "~/.config/fcitx5/config",
        # "~/.config/fcitx5/profile"
    ],
    env=[
        ["QT_IM_MODULE", "fcitx"],
        # ["GTK_IM_MODULE", "fcitx"],
        ["XMODIFIERS", "@im=fcitx"],
        ["SDL_IM_MODULE", "fcitx",],
        ["GLFW_IM_MODULE", "ibus"],
    ],
    auto_start=[["fcitx5", "-d"]]
)

x.font=Recipe(
    pkg=[
        ["noto-fonts", EXTRA],
        ["noto-fonts-cjk", EXTRA],
        ["noto-fonts-emoji", EXTRA],

        ["ttf-fira-code", EXTRA],
        ["ttf-fira-code-nerd", EXTRA],

        ["ttf-jetbrains-mono", EXTRA],
        ["ttf-jetbrains-mono-nerd", EXTRA],
    ],
)
