from box import Box
from src.v5.schema import Recipe, EXTRA, USER


shell=Box(
    pkgs=[
        ["nushell", EXTRA],
        ["atuin", EXTRA],
        ["starship", EXTRA]
    ],
    configs=[
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

terminal_emulator=Box(
    pkgs=[
        ["foot", EXTRA]
    ],
    configs=[
        "~/.config/foot"
    ],
    auto_start=[["foot", "--server"]]
)

terminal_multiplexer=Box(
    pkgs=[
        ["tmux", EXTRA]
    ],
    configs=[
        "~/.tmux.conf"
    ]
)

text=Box(
    pkgs=[
        ["git", EXTRA],
        ["neovim", EXTRA],
        ["emacs-wayland", USER],
    ],
    configs=[
        "~/.config/lazyvim",
        "~/.config/doom"
    ]
)

pdf=Box(
    pkgs=[
        ["zathura", EXTRA],
        ["zathura-pdf-mupdf", EXTRA]
    ],
)

image=Box(
    pkgs=[
        ["imv", EXTRA]
    ],
)

video=Box(
    pkgs=[
        ["mpv", EXTRA]
    ],
    configs=[
        "~/.config/mpv"
    ]
)

office=Box(
    pkgs=[
        ["libreoffice-fresh", EXTRA],
    ],
)

file=Box(
    pkgs=[
        ["gvfs", EXTRA],

        ["yazi", EXTRA],
        # ["chafa", EXTRA],
        # ["poppler", EXTRA],
        # ["ueberzugpp", EXTRA],
        # ["imagemagick", EXTRA],

        ["thunar", EXTRA],
        ["thunar-archive-plugin", EXTRA],

        ["tumbler", EXTRA],
        # ["libgsf", EXTRA],
        # ["poppler-glib", EXTRA],
        # ["ffmpegthumbnailer", EXTRA],

        ["fd", EXTRA],
        ["fzf", EXTRA],
        ["ripgrep", EXTRA],
        ["zoxide", EXTRA],
        ["eza", EXTRA],
        ["bat", EXTRA],
        ["jq", EXTRA],

        # ["7zip", EXTRA],
        ["xarchive", EXTRA],
    ],
    configs=[
        ["sudo", "systemctl", "--user", "enable", "tumblerd"],
    ],
    auto_start=[["thunar", "--daemon"]],
)

browser=Box(
    pkgs=[
        ["firefox", EXTRA],
        ["brave-bin", USER],
        ["zen-browser-bin", USER],
        ["helium-browser-bin", USER],
    ],
    configs=[
        "~/.config/brave-flags.conf"
    ]
)

cloud_drive=Box(
    pkgs=[
        ["megasync", USER],
    ],
)

utils=Box(
    pkgs=[
        ["stow", EXTRA],
        ["timeshift", EXTRA]
    ],
)
