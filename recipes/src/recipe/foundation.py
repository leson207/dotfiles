from box import Box
from src.v5.schema import Recipe, CORE, EXTRA

base=Box()

base.preinstalled=Recipe(
    pkg=[
        ["base", CORE],
        # ["pacman", CORE],
        # ["glibc", CORE],
        # ["systemd", CORE],
    ],
    config=[
        # TODO: should we use cmd to modify config file? If yes write the function func(file, desire_content)
        "/etc/pacman.conf"
    ]
)

base.build_package=Recipe(
    pkg=[
        ["git", EXTRA],
        ["mold", EXTRA],
        ["ccache", EXTRA],
        ["base-devel", EXTRA],
        # ["gcc", EXTRA],
        # ["zstd", EXTRA],
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
