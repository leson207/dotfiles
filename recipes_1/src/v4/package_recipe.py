from box import Box

from src.v4.schema import Install, PkgRecipe, PackageManager, UsageRecipe, Unit
from src.v4.enumeration import Scope


Ins=Box(
    AUR=Install("aur", PackageManager("paru", ("paru", "-S"))),
    ACR=Install("core", PackageManager("pacman", ("sudo", "pacman", "-S"))),
    AER=Install("extra", PackageManager("pacman", ("sudo", "pacman", "-S"))),
)


x=Box()

x.systemd=PkgRecipe(
    "systemd",
    Ins.ACR,
    configs=["~/.config/systemd"],
    units=[Unit(name="systemd-oomd.service", scope=Scope.MULTI_USER)],
)

x.time=UsageRecipe(
    [
        PkgRecipe("glibc", Ins.ACR),
        PkgRecipe("systemd", Ins.ACR, units=[Unit(name="systemd-timesyncd.service", scope=Scope.MULTI_USER)])
    ],
    [
        ["timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"],
        ["sudo", "timedatectl", "set-ntp", "true"],
        ["timedatectl", "set-local-rtc", "0"],
        ["sudo", "hwclock", "--systohc"],
        ["timedatectl", "status"],
    ]
)

x.locale=UsageRecipe(
    [
        PkgRecipe("glibc", Ins.ACR),
        PkgRecipe("systemd", Ins.ACR)
    ],
    [
        ["sudo", "locale-gen", "en_US.UTF-8"],
        ["localectl", "set-locale", "LANG=en_US.UTF-8"]
    ]
)

x.sudo=PkgRecipe("sudo", Ins.ACR, configs=["/etc/sudoers.d/10-foo"])

x.pacman=PkgRecipe(
    "pacman",
    Install("https://gitlab.archlinux.org/pacman/pacman"),
    [
        PkgRecipe("mold", Ins.AER),
        PkgRecipe("ccache", Ins.AER),
        PkgRecipe(
            "rate-mirrors",
            Ins.AER,
            configs=["/etc/pacman.d/hooks/rate-mirrors.hook"],
            bootstrap=[
                ["sudo", "rate-mirrors", "--entry-country", "VN", "--allow-root", "--protocol", "https", "--save", "/etc/pacman.d/mirrorlist", "arch"],
                ["sudo", "pacman", "-Syy"]
            ]
        ),
    ],
    configs=["~/.makepkg.conf"]
)

x.paru=PkgRecipe(
    "paru",
    Install(
        source="Morganamilo/paru",
        bootstrap=[
            ["cd", "~/.cache"],
            ["rm", "-rf", "paru"],
            ["git", "clone", "https://aur.archlinux.org/paru.git"],
            ["cd", "paru"],
            ["makepkg", "-si"],
        ],
    ),
    [
        PkgRecipe("git", Ins.AER),
        PkgRecipe("base_devel", Ins.ACR),
    ],
)

x.systemd_boot_linux=PkgRecipe(
    "systemd",
    Ins.ACR,
    [
        PkgRecipe(
            "linux",
            Ins.ACR,
            [
                PkgRecipe("linux-headers", Ins.ACR),
                PkgRecipe("linux-firmware", Ins.ACR)
            ]
        ),
        PkgRecipe("intel-ucode", Ins.AER)
    ],
    configs=["/boot/loader/loader.conf", "/boot/loader/entries/linux-cachyos-bore.conf"],
    bootstrap=[["sudo", "bootctl", "install"]]
)

x.systemd_boot_linux_cachyos_bore=PkgRecipe(
    "systemd",
    Ins.ACR,
    [
        PkgRecipe(
            "linux-cachyos-bore",
            Ins.AUR,
            [
                PkgRecipe("linux-cachyos-bore-headers", Ins.AUR),
                PkgRecipe("linux-firmware", Ins.ACR)
            ]
        ),
        PkgRecipe("intel-ucode", Ins.AER)
    ],
    configs=["/boot/loader/loader.conf", "/boot/loader/entries/linux-cachyos-bore.conf"],
    bootstrap=[["sudo", "bootctl", "install"]]
)

x.graphic=UsageRecipe(
    [
        PkgRecipe("vulkan-intel", Ins.AER),
        PkgRecipe("intel-media-driver", Ins.AER)
    ]
)

x.audio=UsageRecipe(
    [
        PkgRecipe("pipewire", Ins.AER, units=[Unit(name="pipewire.service", scope=Scope.SINGLE_USER)]),
        PkgRecipe("wireplumber", Ins.AER, units=[Unit(name="wireplumber.service", scope=Scope.SINGLE_USER)]),
        PkgRecipe("pipewire-pulse", Ins.AER, units=[Unit(name="pipewire-pulse.service", scope=Scope.SINGLE_USER)]),
        PkgRecipe("pipewire-alsa", Ins.AER),
    ]
)

x.network=UsageRecipe(
    [
        PkgRecipe("networkmanager", Ins.AER, units=[Unit(name="NetworkManager.service", scope=Scope.MULTI_USER)]),
        PkgRecipe("openssh", Ins.AER, units=[Unit(name="sshd.service", scope=Scope.MULTI_USER)]),

        PkgRecipe(
            "ufw",
            Ins.AER,
            units=[Unit(name="ufw.service", scope=Scope.MULTI_USER)],
            bootstrap=[
                ["sudo", "ufw", "default", "deny", "incoming"],
                ["sudo", "ufw", "default", "allow", "outgoing"],
                # ["sudo","ufw", "allow", "51820/udp"],
                # ["sudo","ufw", "allow", "192.168.1.0/24"],
                ["sudo", "ufw", "enable"],
                ["sudo", "ufw", "status", "verbose"]
            ]
        ),
    ]
)

x.dns=UsageRecipe(
    [
        PkgRecipe(
            "systemd",
            Ins.ACR,
            configs=["/etc/systemd/resolved.conf"],
            units=[Unit(name="systemd-resolved.service", scope=Scope.MULTI_USER)]
        ),
        PkgRecipe(
            "networkmanager",
            Ins.AER,
            configs=["/etc/NetworkManager/conf.d/dns.conf"],
            units=[Unit(name="NetworkManager.service", scope=Scope.MULTI_USER)]
        ),
    ],
    [
        ["ln", "-sf", "/run/systemd/resolve/stub-resolv.conf", "/etc/resolv.conf"],

        ["nmcli", "connection", "modify", "Co Phuong", "ipv4.dns"],
        ["nmcli", "connection", "modify", "Co Phuong", "ipv4.ignore-auto-dns", "yes"],
        ["nmcli", "connection", "modify", "Co Phuong", "ipv6.ignore-auto-dns", "yes"],

        ["systemctl", "restart", "systemd-resolved"],
        ["systemctl", "restart", "NetworkManager"],

        ["resolvectl", "status"],
        ["resolvectl", "query", "google.com"],
        ["curl", "-sL", "https://test.nextdns.io", "|", "jq"]
    ]
)

x.p2p=UsageRecipe(
    [
        PkgRecipe("tlp", Ins.AER, units=[Unit("tlp.service", Scope.MULTI_USER)]),
        PkgRecipe("tlp-pd", Ins.AER, units=[Unit("tlp-pd.service", Scope.MULTI_USER)]),
        PkgRecipe("thermal", Ins.AER, units=[Unit("thermald.service", Scope.MULTI_USER)]),
        PkgRecipe("irqbalance", Ins.AER, units=[Unit("irqbalance.service", Scope.MULTI_USER)]),
        PkgRecipe("batsignal", Ins.AER, units=[Unit("batsignal.service", Scope.MULTI_USER)]),
        PkgRecipe(
            "ananicy-cpp",
            Ins.AER,
            [PkgRecipe("cachyos-ananicy-rules-git", Ins.AUR)],
            units=[Unit("ananicy-cpp.service", Scope.MULTI_USER)]
        ),
    ]
),

x.font=UsageRecipe(
    [
        PkgRecipe(
            "noto-fonts",
            Ins.AER,
            [
                PkgRecipe("noto-fonts-cjk", Ins.AER),
                PkgRecipe("noto-fonts-emoji", Ins.AER),
            ]
        ),
        PkgRecipe("ttf-fira-code", Ins.AER),
        PkgRecipe("ttf-fira-code-nerd", Ins.AER),
        PkgRecipe("ttf-jetbrains-mono", Ins.AER),
        PkgRecipe("ttf-jetbrains-mono-nerd", Ins.AER),
    ]
)

x.input_method=UsageRecipe(
    [
        PkgRecipe(
            "fcitx5",
            Ins.AER,
            [
                PkgRecipe("fcitx5-gtk", Ins.AER),
                PkgRecipe("fcitx5-unikey", Ins.AER),
                PkgRecipe("fcitx5-configtool", Ins.AER),
            ],
            configs=[
                "~/.config/fcitx5/config",
                "~/.config/fcitx5/profile"
            ],
            env_vars=[
                ["QT_IM_MODULE", "fcitx"],
                ["GTK_IM_MODULE", "fcitx"],
                ["XMODIFIERS", "@im=fcitx"],
                ["SDL_IM_MODULE", "fcitx",],
                ["GLFW_IM_MODULE", "fcitx"],
            ],
            auto_start=[["fcitx5", "-d"]]
        ),
    ]
)

x.terminal_multiplexer=UsageRecipe(
    [
        PkgRecipe(
            "tmux",
            Ins.AER,
            configs=["~/.tmux.conf"],
        )
    ]
)

x.util_linux=PkgRecipe("util-linux", Ins.ACR, units=[Unit("fstrim.timer", Scope.MULTI_USER)])

x.browser=UsageRecipe(
    [
        PkgRecipe("firefox", Ins.AER),
        PkgRecipe("zen-browser-bin", Ins.AUR),
        PkgRecipe("brave-bin", Ins.AUR,configs=["~/.config/brave-flags.conf"]),
        PkgRecipe("helium-browser-bin", Ins.AUR),
    ]
)

x.text_editor=UsageRecipe(
    [
        PkgRecipe("neovim", Ins.AER, configs=["~/.config/lazyvim"]),
        PkgRecipe(
            "emacs-wayland",
            Ins.AER,
            configs=["~/.config/doom"],
            units=[Unit("emacs.service", Scope.SINGLE_USER)]
        )
    ]
)

x.drive=UsageRecipe(
    [
        PkgRecipe("megasync", Ins.AUR)
    ]
)

x.dotfile_manager=UsageRecipe(
    [
        PkgRecipe("stow", Ins.AER)
    ]
)

x.sdk=UsageRecipe(
    [
        PkgRecipe("make", Ins.ACR),
        PkgRecipe("gcc", Ins.ACR),
        PkgRecipe("gdb", Ins.ACR),
        PkgRecipe("uv", Ins.ACR),
        PkgRecipe("git", Ins.ACR),
    ]
)

x.monitor=UsageRecipe(
    [
        PkgRecipe("btop", Ins.ACR, configs=["~/.config/btop"]),
    ]
)

x.office=UsageRecipe(
    [
        PkgRecipe(
            "libreoffice-fresh",
            Ins.AER,
            [
                PkgRecipe("libreoffice-fresh-vi", Ins.AER),
                PkgRecipe("libreoffice-fresh-en-gb", Ins.AER)
            ]
        )
    ]
)

x.rollback=UsageRecipe(
    [
        PkgRecipe("timeshift", Ins.AER)
    ]
)

