dofile("utils.lua")

local root={
    build_generator={
        cmake={repo=Repo.AOR},
        meson={repo=Repo.AOR},
    },

    build_system={
        make={repo=Repo.AOR},
        ninja={repo=Repo.AOR},
        xmake={repo=Repo.AOR},
        bazel={repo=Repo.AOR},
        buck2_bin={repo=Repo.AUR},
    },

    compiler_cache={
        ccache={repo=Repo.AOR},
        sccache={repo=Repo.AOR},
    },

    package_manager={
        vcpkg={repo=Repo.AOR},
        conan_bin={repo=Repo.AUR},
    },

    language_server={
        clangd={
            clangd_bin={repo=Repo.AUR},
            bear={rep=Repo.AOR}
        }
    },

    compiler={
        gcc={repo=Repo.AOR},
        clang={repo=Repo.AOR},
    },

    linker={
        ld={repo=Repo.AOR},
        lld={repo=Repo.AOR},
        mold={repo=Repo.AOR},
    },

    std_lib={
        libcpp={repo=Repo.AOR},
        libstdcpp={repo=Repo.AOR},
    },

    std_lib_abi={
        libcppabi={repo=Repo.AOR},
        libstdcppabi={repo=Repo.AOR},
    },
}

local vendor={
    gnu={
        root.compiler.gcc,
        root.linker.ld,
        root.std_lib.libcpp,
        root.std_lib.libcppabi,
    },
    llvm={
        root.compiler.clang,
        root.linker.lld,
        root.std_lib.libstdcpp,
        root.std_lib.libstdcppabi,
    }
}

return {
    root.build_system.make,
    root.compiler_cache.ccache,
    root.language_server.clangd,
    root.compiler.gcc,
    root.linker.ld,
    root.std_lib.libcpp,
    root.std_lib.libcppabi,
}
