from box import Box
from src.v5.schema import Recipe


USER="user"
CORE="core"
EXTRA="extra"

limine_boot=Recipe(
    pkg=[
        ["limine", EXTRA],
        ["efibootmgr", CORE],

        ["linux-headers", CORE],
        ["linux-cachyos-bore-headers", USER],

        # ["zstd", EXTRA],
        ["booster", EXTRA],
        ["intel-ucode", EXTRA],
        ["linux-firmware", CORE],
    ],
    config=[
        "/etc/booster.yaml",
        "/etc/pacman.d/hooks/90-booster.hook",

        "/boot/limine/limine.conf",
        "/etc/pacman.d/hooks/90-limine.hook",

        ["sudo", "mkdir", "-p", "/boot/EFI/arch-limine"],
        ["sudo", "cp", "/usr/share/limine/BOOTX64.EFI", "/boot/EFI/arch-limine/"],
        ["sudo", "efibootmgr", "--create", "--disk", "/dev/sda", "--part", "1", "--label", "Arch Linux Limine Boot Loader", "--loader", "\EFI\arch-limine\BOOTX64.EFI", "--unicode"],

        # /usr/share/libalpm/hooks
        ["sudo" "ln" "-sf" "/dev/null" "/etc/pacman.d/hooks/90-mkinitcpio-install.hook"],
        ["sudo" "ln" "-sf" "/dev/null" "/etc/pacman.d/hooks/60-mkinitcpio-remove.hook"],
        ["/usr/lib/booster/regenerate_images"],

        ["/usr/share/libalpm/scripts/mkinitcpio" "remove"]
    ],
)

virtual_machine=Recipe(
    pkg=[
        ["qemu-desktop", EXTRA],
        ["libvirt", EXTRA],
        ["dnsmasq", EXTRA],
        ["virt-manager", EXTRA],
        ["edk2-ovmf", EXTRA],
    ],
    config=[
        ["sudo", "systemctl", "enable", "--now", "libvirtd"],

        ["sudo", "virsh", "net-define", "/usr/share/libvirt/networks/default.xml"],
        ["sudo", "virsh", "net-autostart", "default"],
        ["sudo", "virsh", "net-start", "default"],

        ["sudo", "usermod", "-aG", "libvirt", "$USER"],
    ]
)

clipboard=Recipe(
    pkg=[
        ["cliphist", EXTRA],
        ["wl-clip-persist", EXTRA]
    ],
    auto_start=[
        ["wl-paste", "--type", "text", "watch", "cliphist", "store"],
        ["wl-paste", "--type", "image", "watch", "cliphist", "store"],
        # "cliphist list | fuzzel --dmenu --with-nth 2 | cliphist decode | wl-copy"
        #
        ["wl-clip-persist", "--clipboard", "regular"]
    ],
)

input_remap=Box(
    pkgs=[
        ["kanata-bin", USER]
    ],
    configs=[
        "/etc/udev/rules.d/99-uinput.rules",
        # KERNEL=="uinput", MODE="0660", GROUP="uinput", OPTIONS+="static_node=uinput"
        ["sudo", "udevadm", "control", "--reload"],
        ["sudo", "udevadm", "trigger", "--verbose", "--sysname-match=uinput"],
        ["sudo", "modprobe", "-r", "uinput"],
        ["sudo", "modprobe", "uinput"]
    ],
    groups={
        # sudo groupadd uinput
        # sudo usermod -aG input $USER
        # sudo usermod -aG uinput $USER
        "input",
        "uinput",
    },
    reference=[
        "https://shom.dev/start/using-kanata-to-remap-any-keyboard/"
    ]
)

screen_record=Box(
    pkgs=[
        ["gpu-screen-recorder", EXTRA],
        ["gpu-screen-recorder-ui", EXTRA]
    ],
)

opener=Box(
    pkgs=[
        ["handlr-regex", EXTRA]
    ],
    configs=[
        "~/.config/handlr",
        "~/.config/mimeapps.list",
        "~/.local/bin/xdg-open",
        ["chmod", "+x", "~/.local/bin/xdg-open"]
        # ["type", "-a", "xdg-open"]
    ],
)

misc=Box(
    pkgs=[
        ["dms-shell", EXTRA],
        ["dgop", EXTRA],
        ["dsearch-bin", USER],

        ["cava", EXTRA],
        ["matugen", EXTRA],
        ["fastfetch", EXTRA],
        ["papirus-icon-theme", EXTRA],
        ["qt6-multimedia", EXTRA],

        ["pamixer", EXTRA],
        ["playctl", EXTRA],
        ["brightnessctl", EXTRA],
        ["ddcutil", EXTRA],
        ["libpulse", EXTRA],

        ["pavucontrol", EXTRA],
        ["blueman", EXTRA],
        ["nm-applet", EXTRA],

        ["aria2", EXTRA],
        ["yt-dlp", EXTRA],
        ["qbitorrent", EXTRA],
        ["hugo", EXTRA],
        ["skim", EXTRA],
        ["git-delta", EXTRA],
        ["duf", EXTRA],
        ["dust", EXTRA],
        ["dua-cli", EXTRA],
        ["progress", EXTRA],
        ["broot", EXTRA],
        ["gping", EXTRA],
        ["rustscan", EXTRA],
        ["yq", EXTRA],
        ["hyperfine", EXTRA],
        ["navi", EXTRA],
        ["direnv", EXTRA],

        ["bluez", EXTRA],
        ["upower", EXTRA],
        ["evolution_data_server", EXTRA],

        ["xsg-user-dirs", EXTRA],
        ["xsg-utils", EXTRA],
        ["krokiet-bin", EXTRA],
        ["anki", EXTRA],
        ["mediawriter", EXTRA],
        ["aspell", EXTRA],
        ["aspell-en", EXTRA],

        ["electron", EXTRA],

        ["orchis-theme", EXTRA],
        ["vimix-curors", EXTRA],
        ["tela-circle-icon-theme", EXTRA],
    ],
    env=[
        ["ELECTRON_OZONE_PLATFORM_HINT","auto"]
    ]
)


