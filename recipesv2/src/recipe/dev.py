from src.schema.enumeration import Relationship, Repo, Scope
from src.schema.atomic import Unit, Package, Topic


map = {}

Topic(
    name="version-control",
    recipes=[
        Package(
            name="git",
            repo=Repo.OFFICIAL,
            single_user_config=["~/.gitconfig"],
            supporters=[
                Package("less", Repo.OFFICIAL),
                Package("git-delta", Repo.OFFICIAL),
            ]
        ),
        # Package("jujutsu", Repo.OFFICIAL),
    ]
)

Topic(
    name="c++",
    recipes=[
        Topic(
            name="build-generator",
            recipes=[
                # Package("xmake", Repo.OFFICIAL),
                # Package("meson", Repo.OFFICIAL),
                # Package("bazel", Repo.OFFICIAL),
                # Package("buck2-bin", Repo.AUR),
                Package("cmake", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="build system",
            recipes=[Package("ninja", Repo.OFFICIAL)]
        ),
        Topic(
            name="compiler cache",
            recipes=[
                Package("ccache", Repo.OFFICIAL),
                # Package("sccache", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="package manager",
            recipes=[Package("conan-bin", Repo.AUR)]
        ),
        # Topic(
        #     name="language-server",
        #     recipes=[Package("clangd-bin", Repo.AUR)]
        # ),
        Topic(
            name="compiler",
            recipes=[
                Package("gcc", Repo.OFFICIAL),
                Package("clang", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="debugger",
            recipes=[
                Package("gdb", Repo.OFFICIAL),
                Package("lldb", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="linker",
            recipes=[
                Package("ld", Repo.OFFICIAL),
                Package("lld", Repo.OFFICIAL),
                Package("mold", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="standard library",
            recipes=[
                Package("libc++", Repo.OFFICIAL, supporters=[Package("libc++abi", Repo.OFFICIAL)]),
                Package("libstdc++", Repo.OFFICIAL, supporters=[Package("libstdc++abi", Repo.OFFICIAL)]),
            ]
        )
    ]
)

Topic(
    name="python",
    recipes=[Package("uv", Repo.OFFICIAL)]
)

# Topic(
#     name="go",
#     recipes=[Package("go", Repo.OFFICIAL)]
# )

# Topic(
#     name="rust",
#     recipes=[Package("rustup", Repo.OFFICIAL)]
# )

Topic(
    name="editor",
    recipes=[
        Topic(
            name="keyboard-driven editor",
            recipes=[
                # Package("vim", Repo.OFFICIAL),
                Package("neovim", Repo.OFFICIAL, supporters=[Package("luarocks", Repo.OFFICIAL)]),
                # Package("helix", Repo.OFFICIAL),
                # Package("kakoune", Repo.OFFICIAL),
                # Package("emacs", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="gui editor",
            recipes=[
                Package("zed", Repo.OFFICIAL),
                Package("code", Repo.OFFICIAL, single_user_config=["~/.config/code-flags.conf"]),
                # Package("typst", Repo.OFFICIAL),
                # Package("lapce", Repo.OFFICIAL),
                # Package("xi-editor", Repo.GITHUB),
                # Package("fresh-editor-bin", Repo.AUR),
                # Package("micro", Repo.OFFICIAL),
            ]
        )
    ]
)

Topic(
    name="monitor",
    recipes=[
        # Package("atop", Repo.OFFICIAL),
        Package("btop", Repo.OFFICIAL, single_user_config=["~/.config/btop"]),
        # Package("htop", Repo.OFFICIAL),
        # Package("nvtop", Repo.OFFICIAL),
        # Package("glances", Repo.OFFICIAL),
        # Package("bottom", Repo.OFFICIAL),
        # Package("hyperfine", Repo.OFFICIAL),
    ]
)

# Topic(
#     name="container",
#     recipes=[
#         Package(
#             name="podman",
#             repo=Repo.OFFICIAL,
#             single_user_config=["~/.config/containers"],
#             supporters=[
#                 Package("podman-tui", Repo.AUR),
#                 Package("podman-desktop", Repo.OFFICIAL),
#                 Package("podman-compose", Repo.OFFICIAL),
#             ]
#         )
#     ]
# )

Topic(
    name="virtualization-misc",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package(
            name="libvirt",
            repo=Repo.OFFICIAL,
            units=[Unit("libvirtd.service", scope=Scope.MULTI_USER)],
            supporters=[
                # hyprvisor
                Package("qemu-desktop", Repo.OFFICIAL),
                # NET DHCP
                Package("dnsmasq", Repo.OFFICIAL),
            ]
        ),
        # GUI config?
        Package("virt-manager", Repo.OFFICIAL),
        # GUI display VM?
        Package("virt-viewer", Repo.OFFICIAL),
    ]
)

Topic(
    name="misc",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        # Package("broot", Repo.OFFICIAL),
        Package("tree", Repo.OFFICIAL),
        # Package("aria2", Repo.OFFICIAL),
        # Package("dust", Repo.OFFICIAL),
        # Package("dua-cli", Repo.OFFICIAL),
        # Package("progress", Repo.OFFICIAL),
        Package("fastfetch", Repo.OFFICIAL),

        Package("fd", Repo.OFFICIAL),
        Package("fzf", Repo.OFFICIAL),
        Package("bat", Repo.OFFICIAL),
        Package("eza", Repo.OFFICIAL),
        Package("zoxide", Repo.OFFICIAL),
        Package("ripgrep", Repo.OFFICIAL),
        Package("rsync", Repo.OFFICIAL),
        Package("7zip", Repo.OFFICIAL),
    ]

)
