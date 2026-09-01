from box import Box

from src.recipe.schema import Recipe

USER="user"
CORE="core"
EXTRA="extra"

limine_boot=Recipe(
    pkg=[
        ["limine", EXTRA],
        ["efibootmgr", CORE],

        ["linux-headers", CORE],
        ["linux-cachyos-bore-headers", USER],

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
        ["sudo", "efibootmgr", "--create", "--disk", "/dev/sda", "--part", "1", "--label", "Arch Linux Limine Boot Loader", "--loader", "\\EFI\arch-limine\\BOOTX64.EFI", "--unicode"],

        # /usr/share/libalpm/hooks
        ["sudo", "ln", "-sf", "/dev/null", "/etc/pacman.d/hooks/90-mkinitcpio-install.hook"],
        ["sudo", "ln", "-sf", "/dev/null", "/etc/pacman.d/hooks/60-mkinitcpio-remove.hook"],
        ["/usr/lib/booster/regenerate_images"],

        ["/usr/share/libalpm/scripts/mkinitcpio", "remove"]
    ],
)

core_utils=Recipe(
    pkg=[
        ["uutils-coreutils", EXTRA],
    ],
    config=[
        "~/.config/scripts/uutils-coreutils.sh",
        ["sh", "~/.config/scripts/uutils-coreutils.sh"],
    ]
)

virtual_machine=Recipe(
    pkg=[
        ["qemu-desktop", EXTRA],
        ["libvirt", EXTRA],
        ["dnsmasq", EXTRA],
        ["virt-manager", EXTRA],
    ],
    config=[
        # https://wiki.cachyos.org/virtualization/qemu_and_vmm_setup
        ["sudo", "systemctl", "enable", "--now", "libvirtd"],

        ["sudo", "virsh", "net-autostart", "default"],
        ["sudo", "virsh", "net-start", "default"],

        ["sudo", "usermod", "-aG", "libvirt", "$USER"],
    ]
)

grammar=Recipe(
    pkg=[
        ["harper", EXTRA],
    ],
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

zsh_shell=Recipe(
    pkg=[
        ["zsh", EXTRA],

        ["atuin", EXTRA],
        ["direnv", EXTRA],
        ["starship", EXTRA],
        ["fastfetch", EXTRA],
    ],
    config=[
        ".zshrc",
        ["git", "clone", "https://github.com/zdharma-continuum/zinit.git", "~/.local/share/zinit/zinit.git"],
        ["zcompile", "~/.local/share/zinit/zinit.git/zinit.zsh"]
    ],
    update=[
        ["zinit", "update", "--all"],
        ["zcompile", "~/.local/share/zinit/zinit.git/zinit.zsh"]
    ]
)

nushell=Recipe(
    pkg=[
        ["nushell", EXTRA],
        ["atuin", EXTRA],
        ["starship", EXTRA],
        ["fastfetch", EXTRA],
    ],
    config=[
        "~/.config/nushell",
        ["chsh", "-s", "/bin/fish"],

        "~/.config/starship.toml",
        ["mkdir", "($nu.data-dir | path join \"vendor/autoload\")"],
        ["starship", "init", "nu", "|", "save", "-f", "($nu.data-dir | path join \"vendor/autoload/starship.nu\")"],

        "~/.config/atuin",
        ["mkdir", "~/.local/share/atuin/"],
        ["atuin", "init", "nu", "|", "save", "~/.local/share/atuin/init.nu"],
    ],
    auto_start=[["atuin", "daemon", "start"]]
)

bash=Recipe(
    pkg=[
        ["bash", CORE],
        ["blesh", USER],
    ],
    config=[
        "~/.bashrc",
        "~/.bash_profile",
    ]
)

misc=Box(
    pkgs=[
        ["matugen", EXTRA],

        ["playctl", EXTRA],
        ["brightnessctl", EXTRA],
        ["ddcutil", EXTRA],
        ["libpulse", EXTRA],

        ["easyeffects", EXTRA],
        ["qpwgraph", EXTRA],
        ["pamixer", EXTRA],
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

        ["krokiet-bin", EXTRA],
        ["anki", EXTRA],
        ["mediawriter", EXTRA],
        ["aspell", EXTRA],
        ["aspell-en", EXTRA],

        ["electron", EXTRA],
        ["strace", EXTRA],
        ["perf", EXTRA],
        ["valgrind", EXTRA],

        # foot
        ["libnotify", EXTRA],
        ["xdg-utils", EXTRA],
        ["harper", EXTRA],
        ["hunspell-en_us", EXTRA],
    ],

    config=["~/.config/electron-flags.conf"],

    env=[
        ["ELECTRON_OZONE_PLATFORM_HINT","auto"]
    ]
)


