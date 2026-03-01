dofile("utils.lua")

local m={}


m.version_control.git={
    Repo.AOR,
    single_user_config={"~/.gitconfig"},
    supporters={
        less=aor,
        git_delta=aor,
    }
}
m.version_control.jujutsu=aor

m.cpp.build_generator={
    xmake=aor,
    meson=aor,
    bazel=aor,
    buck2_bin=aur,
    cmake=aor,
}
m.cpp.build_system={ninja=aor}
m.cpp.compiler_cache={
    ccache=aor,
    sccache=aor
}
m.cpp.package_manager={conan_bin={Repo.AUR}}
m.cpp.language_server={clangd_bin={Repo.AUR}}
m.cpp.compiler={
    gcc=aor,
    clang=aor
}
m.cpp.debugger={
    gdb=aor,
    lldb=aor
}
m.cpp.linker={
    ld=aor,
    lld=aor,
    mold=aor
}
m.cpp.std_lib={
    ["libc++"]={
        Repo.AOR,
        supporters={["libc++abi"]=aor}
    },
    ["libstdc++"]={
         Repo.AOR,
        supporters={["libstdc++abi"]=aor}
    }
}

m.python.uv=aor
-- m.go.go=aor
-- m.rust.rustup=aor

m.editor.terminal={
    vim=aor,
    neovim={Repo.AOR, supporters={luarocks=aor}},
    helix=aor,
    kakoune=aor,
    emacs=aor,
}

m.editor.gui={
    zed=aor,
    code=aor,
    -- typst=aor,
    -- lapce=aor,
    -- micro=aor,
    -- xi_editor={Repo.GITHUB},
    -- fresh_editor_bin=aur,
}

m.monitor={
    -- atop=aor,
    btop=aor,
    -- htop=aor,
    -- nvtop=aor,
    -- glances=aor,
    -- bottom=aor,
    -- hyperfine=aor,
}

m.container.podman={
    Repo.AOR,
    single_user_config={"~/.config/containers"},
    supporters={
        podman_tui=aur,
        podman_desktop=aor,
        podman_compose=aor,
    }
}

m.virtualization.relationship=Relationship.ASSOCIATED
m.virtualization={
    libvirt={
        Repo.AOR,
        units={"libvirtd.service", scope=Scope.MULTI_USER},
        supporters={
            -- hyprvisor
            qemu_desktop=aor,
            -- NET DHCP
            dnsmasq=aor,
        }
    },
    -- GUI config?
    virt_manager=aor,
    -- GUI display VM?
    virt_viewer=aor,
}

m.misc={
    -- broot=aor,
    tree=aor,

    aria2=aor,

    -- dust=aor,
    -- dua_cli=aor,
    -- progress=aor,

    fastfetch=aor,

    fd=aor,
    fzf=aor,
    bat=aor,
    eza=aor,
    zoxide=aor,
    ripgrep=aor,
    rsync=aor,
    ["7zip"]=aur
}
