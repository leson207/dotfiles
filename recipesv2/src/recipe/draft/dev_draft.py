from src.schema.enumeration import Relationship, Repo, Scope
from src.schema.atomic import Unit
from box import Box

m=Box()

m.version_control.git=Box(
    repo=Repo.AOR,
    single_user_config=["~/.gitconfig"],
    supporters=Box(
        less=Box(repo=Repo.AOR),
        git_delta=Box(repo=Repo.AOR),
    )
)
m.version_control.jujutsu=Box(repo=Repo.AOR)

m.cpp.build_generator=Box(
    xmake=Box(repo=Repo.AOR),
    meson=Box(repo=Repo.AOR),
    bazel=Box(repo=Repo.AOR),
    buck2_bin=Box(repo=Repo.AUR),
    cmake=Box(repo=Repo.AOR),
)
m.cpp.build_system=Box(ninja=Box(repo=Repo.AOR))
m.cpp.compiler_cache=Box(
    ccache=Box(repo=Repo.AOR),
    sccache=Box(repo=Repo.AOR)
)
m.cpp.package_manager=Box(conan_bin=Box(repo=Repo.AUR))
m.cpp.language_server=Box(clangd_bin=Box(repo=Repo.AUR))
m.cpp.compiler=Box(
    gcc=Box(repo=Repo.AOR),
    clang=Box(repo=Repo.AOR)
)
m.cpp.debugger=Box(
    gdb=Box(repo=Repo.AOR),
    lldb=Box(repo=Repo.AOR)
)
m.cpp.linker=Box(
    ld=Box(repo=Repo.AOR),
    lld=Box(repo=Repo.AOR),
    mold=Box(repo=Repo.AOR)
)
m.cpp.std_lib={
    "libc++": Box(
        repo=Repo.AOR,
        supporters={"libc++abi" : {"repo": Repo.AOR}}
    ),
    "libstdc++": Box(
        repo= Repo.AOR,
        supporters={"libstdc++abi" : {"repo": Repo.AOR}}
    )
}

m.python.uv=Box(repo=Repo.AOR)
# m.go.go=Box(repo=Repo.AOR)
# m.rust.rustup=Box(repo=Repo.AOR)

m.editor.terminal=Box(
    vim=Box(repo=Repo.AOR),
    neovim=Box(repo=Repo.AOR, supporters=Box(luarocks=Box(repo=Repo.AOR))),
    helix=Box(repo=Repo.AOR),
    kakoune=Box(repo=Repo.AOR),
    emacs=Box(repo=Repo.AOR),
)

m.editor.gui=Box(
    zed=Box(repo=Repo.AOR),
    code=Box(repo=Repo.AOR),
    # typst=Box(repo=Repo.AOR),
    # lapce=Box(repo=Repo.AOR),
    # micro=Box(repo=Repo.AOR),
    # xi_editor=Box(repo=Repo.GITHUB),
    # fresh_editor_bin=Box(repo=Repo.AUR),
)

m.monitor=Box(
    atop=Box(repo=Repo.AOR),
    btop=Box(repo=Repo.AOR),
    htop=Box(repo=Repo.AOR),
    nvtop=Box(repo=Repo.AOR),
    glances=Box(repo=Repo.AOR),
    bottom=Box(repo=Repo.AOR),
    hyperfine=Box(repo=Repo.AOR),
)

m.container.podman=Box(
    repo=Repo.AOR,
    single_user_config=["~/.config/containers"],
    supporters=Box(
        podman_tui=Box(repo=Repo.AUR),
        podman_desktop=Box(repo=Repo.AOR),
        podman_compose=Box(repo=Repo.AOR),
    )
)

m.virtualization.relationship=Relationship.ASSOCIATED
m.virtualization=Box(
    libvirt=Box(
        repo=Repo.AOR,
        units=[Unit("libvirtd.service", scope=Scope.MULTI_USER)],
        supporters=Box(
            # hyprvisor
            qemu_desktop=Box(repo=Repo.AOR),
            # NET DHCP
            dnsmasq=Box(repo=Repo.AOR),
        )
    ),
    # GUI config?
    virt_manager=Box(repo=Repo.AOR),
    # GUI display VM?
    virt_viewer=Box(repo=Repo.AOR),
)

m.misc=Box(
    broot=Box(repo=Repo.AOR),
    tree=Box(repo=Repo.AOR),

    aria2=Box(repo=Repo.AOR),

    dust=Box(repo=Repo.AOR),
    dua_cli=Box(repo=Repo.AOR),
    progress=Box(repo=Repo.AOR),

    fastfetch=Box(repo=Repo.AOR),

    fd=Box(repo=Repo.AOR),
    fzf=Box(repo=Repo.AOR),
    bat=Box(repo=Repo.AOR),
    eza=Box(repo=Repo.AOR),
    zoxide=Box(repo=Repo.AOR),
    ripgrep=Box(repo=Repo.AOR),
    rsync=Box(repo=Repo.AOR),
)

m.misc["7zip"]=Box(repo=Repo.AOR)
