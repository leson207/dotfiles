from src.schema.enumeration import Relationship, Repo, Scope
from src.schema.atomic import Unit, Package, Topic


map = {}

Topic(
    name="version-control",
    recipes=[
        Package(
            name="git",
            repo=Repo.AOR,
            single_user_config=["~/.gitconfig"],
            supporters=[
                Package("less", Repo.AOR),
                Package("git-delta", Repo.AOR),
            ]
        ),
        # Package("jujutsu", Repo.AOR),
    ]
)

Topic(
    name="c++",
    recipes=[
        Topic(
            name="build-generator",
            recipes=[
                # Package("xmake", Repo.AOR),
                # Package("meson", Repo.AOR),
                # Package("bazel", Repo.AOR),
                # Package("buck2-bin", Repo.AUR),
                Package("cmake", Repo.AOR),
            ]
        ),
        Topic(
            name="build system",
            recipes=[Package("ninja", Repo.AOR)]
        ),
        Topic(
            name="compiler cache",
            recipes=[
                Package("ccache", Repo.AOR),
                # Package("sccache", Repo.AOR),
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
                Package("gcc", Repo.AOR),
                Package("clang", Repo.AOR),
            ]
        ),
        Topic(
            name="debugger",
            recipes=[
                Package("gdb", Repo.AOR),
                Package("lldb", Repo.AOR),
            ]
        ),
        Topic(
            name="linker",
            recipes=[
                Package("ld", Repo.AOR),
                Package("lld", Repo.AOR),
                Package("mold", Repo.AOR),
            ]
        ),
        Topic(
            name="standard library",
            recipes=[
                Package("libc++", Repo.AOR, supporters=[Package("libc++abi", Repo.AOR)]),
                Package("libstdc++", Repo.AOR, supporters=[Package("libstdc++abi", Repo.AOR)]),
            ]
        )
    ]
)

Topic(
    name="python",
    recipes=[Package("uv", Repo.AOR)]
)

# Topic(
#     name="go",
#     recipes=[Package("go", Repo.AOR)]
# )

# Topic(
#     name="rust",
#     recipes=[Package("rustup", Repo.AOR)]
# )

Topic(
    name="editor",
    recipes=[
        Topic(
            name="keyboard-driven editor",
            recipes=[
                # Package("vim", Repo.AOR),
                Package("neovim", Repo.AOR, supporters=[Package("luarocks", Repo.AOR)]),
                # Package("helix", Repo.AOR),
                # Package("kakoune", Repo.AOR),
                # Package("emacs", Repo.AOR),
            ]
        ),
        Topic(
            name="gui editor",
            recipes=[
                Package("zed", Repo.AOR),
                Package("code", Repo.AOR, single_user_config=["~/.config/code-flags.conf"]),
                # Package("typst", Repo.AOR),
                # Package("lapce", Repo.AOR),
                # Package("xi-editor", Repo.GITHUB),
                # Package("fresh-editor-bin", Repo.AUR),
                # Package("micro", Repo.AOR),
            ]
        )
    ]
)

Topic(
    name="monitor",
    recipes=[
        # Package("atop", Repo.AOR),
        Package("btop", Repo.AOR, single_user_config=["~/.config/btop"]),
        # Package("htop", Repo.AOR),
        # Package("nvtop", Repo.AOR),
        # Package("glances", Repo.AOR),
        # Package("bottom", Repo.AOR),
        # Package("hyperfine", Repo.AOR),
    ]
)

# Topic(
#     name="container",
#     recipes=[
#         Package(
#             name="podman",
#             repo=Repo.AOR,
#             single_user_config=["~/.config/containers"],
#             supporters=[
#                 Package("podman-tui", Repo.AUR),
#                 Package("podman-desktop", Repo.AOR),
#                 Package("podman-compose", Repo.AOR),
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
            repo=Repo.AOR,
            units=[Unit("libvirtd.service", scope=Scope.MULTI_USER)],
            supporters=[
                # hyprvisor
                Package("qemu-desktop", Repo.AOR),
                # NET DHCP
                Package("dnsmasq", Repo.AOR),
            ]
        ),
        # GUI config?
        Package("virt-manager", Repo.AOR),
        # GUI display VM?
        Package("virt-viewer", Repo.AOR),
    ]
)

Topic(
    name="misc",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        # Package("broot", Repo.AOR),
        Package("tree", Repo.AOR),
        # Package("aria2", Repo.AOR),
        # Package("dust", Repo.AOR),
        # Package("dua-cli", Repo.AOR),
        # Package("progress", Repo.AOR),
        Package("fastfetch", Repo.AOR),

        Package("fd", Repo.AOR),
        Package("fzf", Repo.AOR),
        Package("bat", Repo.AOR),
        Package("eza", Repo.AOR),
        Package("zoxide", Repo.AOR),
        Package("ripgrep", Repo.AOR),
        Package("rsync", Repo.AOR),
        Package("7zip", Repo.AOR),
    ]

)
