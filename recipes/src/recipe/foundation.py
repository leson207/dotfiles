from box import Box

from src.recipe.schema import CORE, EXTRA, Recipe

x=Box()

x.fs=Recipe(
    manual=True,
    config=[
        "/etc/fstab",
        ["sudo", "systemctl", "daemon-reload"],
        ["sudo", "mount", "-a"],
    ]
)

x.base=Recipe(
    pkg=[
        # ["base", CORE],
        # ["glibc", CORE],
        # ["pacman", CORE],
        # ["systemd", CORE],
        # ["lz4", CORE],
        # ["zstd", CORE],
        ["pacman-contrib", EXTRA],
    ],
    config=[
        ["sudo", "sed", "-i", "s/^#Color$/Color/", "/etc/pacman.conf"]
    ]
)

x.build=Recipe(
    pkg=[
        ["git", EXTRA],
        ["mold", EXTRA],
        ["ccache", EXTRA],

        ["axel", EXTRA],
        ["base-devel", CORE],
        # ["sudo", EXTRA],
        # ["gcc", EXTRA],
    ],
    config=[
        "~/.makepkg.conf",
        "/etc/sudoers.d/10-foo",

        ["cd", "~/.cache"],
        ["rm", "-rf", "paru"],
        ["git", "clone", "https://aur.archlinux.org/paru.git"],
        ["cd", "paru"],
        ["makepkg", "-si"],
    ]
)

x.core_utils= Recipe(
    pkg=[
        ["fd", EXTRA],
        ["fzf", EXTRA],
        ["ripgrep", EXTRA],

        ["bat", EXTRA],
        ["eza", EXTRA],
        ["zoxide", EXTRA],

        ["jq", EXTRA],
    ]
)
