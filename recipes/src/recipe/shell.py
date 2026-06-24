from src.v5.schema import Recipe, EXTRA, USER


display_manager=Recipe(
    pkg=[
        ["sddm", EXTRA],
        ["sddm-astronaut-theme", USER]
    ],
    config=[
        "/etc/sddm.conf",
        "/etc/sddm.conf.d"
    ]
)

window_compositor=Recipe(
    pkg=[
        ["niri", EXTRA],
        ["xwayland-satelite", EXTRA],
        ["xdg-desktop-portal-gtk", EXTRA],
        # TODO: do we need this?
        ["qt6-wayland", EXTRA],
        ["dms-shell-niri", EXTRA],

        ["fuzzel", EXTRA],
        ["app2unit", USER]
    ],
    config=[
        "~/.config/niri",
        "~/.config/DankMaterialShell",
        ["systemctl", "--user", "add-wants", "niri.service", "dms"],

        "~/.config/fuzzel"
    ],
    env=[
        ["APP2UNIT_SLICES", "a=app-graphical.slice b=background-graphical.slice s=session-graphical.slice"]
    ]
)

shell=Recipe(
    pkg=[
        ["git", "EXTRA"],

        ["zsh", "EXTRA"],

        ["fd", "EXTRA"],
        ["fzf", "EXTRA"],
        ["ripgrep", "EXTRA"],

        ["bat", "EXTRA"],
        ["eza", "EXTRA"],
        ["zoxide", "EXTRA"],

        ["direnv", EXTRA],
        ["atuin", "EXTRA"],
        ["starship", "EXTRA"],
    ],
    config=[
        ".zshrc",
        ["git", "clone", "https://github.com/zdharma-continuum/zinit.git", "~/.local/share/zinit"]
    ]
)
