from re import Pattern
from src.schema.enumeration import Repo, Scope
from src.schema.atomic import Unit, PackageRecipe, TopicRecipe


map = {}

TopicRecipe(
    name="version-control",
    recipes=[
        PackageRecipe(
            name="git",
            repo=Repo.OFFICIAL,
            supporters=[
                PackageRecipe("less", Repo.OFFICIAL),
                PackageRecipe("git-delta", Repo.OFFICIAL),
            ]
        ),
        PackageRecipe("jujutsu", Repo.OFFICIAL),
        PackageRecipe("cvs", Repo.OFFICIAL),
        PackageRecipe("mercurial", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="c++",
    recipes=[
        PackageRecipe("xmake", Repo.OFFICIAL),
        PackageRecipe("meson", Repo.OFFICIAL),
        PackageRecipe("bazel", Repo.OFFICIAL),
        PackageRecipe("buck2-bin", Repo.AUR),
        PackageRecipe("cmake", Repo.OFFICIAL),

        PackageRecipe("ninja", Repo.OFFICIAL),

        PackageRecipe("ccache", Repo.OFFICIAL),
        PackageRecipe("sccache", Repo.OFFICIAL),
        PackageRecipe("conan-bin", Repo.AUR),

        PackageRecipe("gcc", Repo.OFFICIAL),
        PackageRecipe("clang", Repo.OFFICIAL),

        PackageRecipe("gdb", Repo.OFFICIAL),
        PackageRecipe("lldb", Repo.OFFICIAL),

        PackageRecipe("clangd", Repo.OFFICIAL),

        PackageRecipe("ld", Repo.OFFICIAL),
        PackageRecipe("lld", Repo.OFFICIAL),
        PackageRecipe("mold", Repo.OFFICIAL),

        PackageRecipe("libstdc++", Repo.OFFICIAL),
        PackageRecipe("libstdc++abi", Repo.OFFICIAL),
        PackageRecipe("libc++", Repo.OFFICIAL),
        PackageRecipe("libc++abi", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="go",
    recipes=[PackageRecipe("go", Repo.OFFICIAL)]
)

TopicRecipe(
    name="python",
    recipes=[PackageRecipe("uv", Repo.OFFICIAL)]
)
TopicRecipe(
    name="rust",
    recipes=[PackageRecipe("rustup", Repo.OFFICIAL)]
)

TopicRecipe(
    name="keyboard-driven editor",
    recipes=[
        PackageRecipe("neovim", Repo.OFFICIAL, supporters=[PackageRecipe("luarocks", Repo.OFFICIAL)]),
        PackageRecipe("vim", Repo.OFFICIAL),
        PackageRecipe("helix", Repo.OFFICIAL),
        PackageRecipe("kakoune", Repo.OFFICIAL),
        PackageRecipe("emacs", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="gui editor",
    recipes=[
        PackageRecipe("zed", Repo.OFFICIAL),
        PackageRecipe("code", Repo.OFFICIAL),
        PackageRecipe("typst", Repo.OFFICIAL),
        PackageRecipe("lapce", Repo.OFFICIAL),
        PackageRecipe("xi-editor", Repo.OFFICIAL),
        PackageRecipe("fresh-editor-bin", Repo.AUR),
        PackageRecipe("micro", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="note-taking",
    recipes=[
        PackageRecipe("memos", Repo.AUR),
        PackageRecipe("zettlr ", Repo.AUR),
        PackageRecipe("obsidian", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="office",
    recipes=[
        PackageRecipe("onlyoffice", Repo.AUR),
        PackageRecipe("libreoffice-fresh", Repo.OFFICIAL),
        PackageRecipe("openoffice", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="container",
    recipes=[
        PackageRecipe(
            name="podman",
            repo=Repo.OFFICIAL,
            supporters=[
                PackageRecipe("podman-tui", Repo.OFFICIAL),
                PackageRecipe("podman-desktop", Repo.OFFICIAL),
            ]
        )
    ]
)

TopicRecipe(
    name="virtual-machine-misc",
    recipes=[
        PackageRecipe("dnsmasq", Repo.OFFICIAL),
        PackageRecipe("libvirt", Repo.OFFICIAL, units=[Unit("libvirtd.service", scope=Scope.MULTI_USER)]),
        PackageRecipe("qemu-full", Repo.OFFICIAL),
        PackageRecipe("virt-viewer", Repo.OFFICIAL),
        PackageRecipe("virt-manager", Repo.OFFICIAL),
        PackageRecipe("bridge-utils", Repo.OFFICIAL),
    ]
)
