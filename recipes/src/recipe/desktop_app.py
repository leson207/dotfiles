from box import Box

from src.recipe.schema import EXTRA, USER, Recipe

opener=Box(
    pkgs=[
        ["handlr-regex", EXTRA]
    ],
    configs=[
        "~/.config/handlr",
        ["~/.local/bin/xdg-open"],
        ["chmod", "+x", "~/.local/bin/xdg-open"],

        # ["type", "-a", "xdg-open"],
        # ["which", "-a", "xdg-open"],

        ["handlr", "set", "text/*", "nvim.desktop"],
        ["handlr", "set", "image/*", "swayimg.desktop"],
        # TODO: application/pdf or pdf/*?
        ["handlr", "set", "application/pdf", "org.pwmt.zathura.desktop"],
    ],
    env=[
        ["TERM", "foot"],
        ["PAGER", "bat"],
        ["MANPAGER", "nvim +Man!"],
        ["MANPAGER", "vi -M +MANPAGER -"],

        ["VISUAL", "nvim"],
        ["EDITOR", "nvim"],
        ["BROWSER", "firefox"],
    ]
)

terminal_emulator=Recipe(
    pkg=[
        ["foot", EXTRA],
    ],
    config=[
        "~/.config/foot"
    ],
    auto_start=[["foot", "--server"]]
)

terminal_multiplexer=Recipe(
    pkg=[
        ["tmux", EXTRA],
    ],
    config=[
        "~/.tmux.conf"
    ]
)

text=Recipe(
    pkg=[
        ["vim", EXTRA],
        # ["gvim", EXTRA],

        ["neovim", EXTRA],
        ["featherpad", EXTRA],
        ["emacs-wayland", USER],
    ],
    config=[
        "~/.vimrc",
        "~/.config/lazyvim",
        "~/.config/doom"
    ]
)

opener=Recipe(
    pkg=[
        ["chafa", EXTRA],
        ["swayimg", EXTRA],

        ["mpv", EXTRA],

        ["zathura", EXTRA],
        ["zathura-pdf-mupdf", EXTRA],

        ["libreoffice-fresh", EXTRA],

        ["7zip", EXTRA],
        ["xarchive", EXTRA],
    ],
    config=[
        "~/.config/mpv",
        "~/.config/swayimg"
    ]
)

file=Box(
    pkgs=[
        ["gvfs", EXTRA],

        ["yazi", EXTRA],

        ["thunar", EXTRA],
        ["thunar-archive-plugin", EXTRA],

        ["xdg-user-dirs", EXTRA],

        ["tumbler", EXTRA],
        # ["libgsf", EXTRA],
        # ["poppler-glib", EXTRA],
        ["ffmpegthumbnailer", EXTRA],
    ],
    configs=[
        ["systemctl", "--user", "enable", "tumblerd"],
        ["systemctl", "--user", "enable", "xdg-user-dirs"],
    ],
    auto_start=[["thunar", "--daemon"]],
)

browser=Box(
    pkgs=[
        ["firefox", EXTRA],
        ["brave-bin", USER],
        ["brave-origin-bin", USER],
        ["zen-browser-bin", USER],
        ["helium-browser-bin", USER],
    ],
    configs=[
        "~/.config/brave-flags.conf"
    ]
)

social=Recipe(
    pkg=[
        ["telegram-desktop", EXTRA]
    ]
)

utils=Box(
    pkgs=[
        ["stow", EXTRA],
        ["megasync", USER],
        # ["timeshift", EXTRA],
        ["syncthing", EXTRA],
        ["krokiet", USER],
    ],
    config=[
        ["systemctl", "--user", "enable", "syncthing"],
    ]
)
