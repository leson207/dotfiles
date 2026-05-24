dofile("utils.lua")

local usecase={
    build_generator={

        {"cmake", Repo.AOR},
        {"meson", Repo.AOR},
    },
    build_system={
        {"make", Repo.AOR},
        {"ninja", Repo.AOR},
        {"xmake", Repo.AOR},
        {"bazel", Repo.AOR},
        {"buck2-bin", Repo.AUR},
    },
    compiler_cache={
        {"ccache", Repo.AOR},
        {"scache", Repo.AOR}
    },
    package_manager={
        {"vcpkg", Repo.AOR},
        {"conan-bin", Repo.AUR}
    },
    language_server={
        {"clangd-bin", Repo.AUR},
    },
    compilation_database_generator={
        {"bear", Repo.AOR},
    },
    compiler={
        {"gcc", Repo.AOR},
        {"clang", Repo.AOR}
    },
    linker={
        {"ld", Repo.AOR},
        {"lld", Repo.AOR},
        {"mold", Repo.AOR}
    },
    std_lib={
        {"libc++", Repo.AOR},
        {"libstdc++", Repo.AOR},
    },
    std_lib_abi={
        {"libc++abi", Repo.AOR},
        {"libstdc++abi", Repo.AOR},
    },
}

local vendor={
    gnu={
        {"gcc", Repo.AOR},
        {"ld", Repo.AOR},
        {"libc++", Repo.AOR},
        {"libc++abi", Repo.AOR},
    },
    llvm={
        {"clang", Repo.AOR},
        {"lld", Repo.AOR},
        {"libcstd++", Repo.AOR},
        {"libcstd++abi", Repo.AOR},
    }
}

local picked={
    {"make", Repo.AOR},
    {"ccache", Repo.AOR},
    {"clangd-bin", Repo.AOR},
    {"bear", Repo.AOR},
    {"gcc", Repo.AOR},
    {"ld", Repo.AOR},
    {"libc++", Repo.AOR},
    {"libc++abi", Repo.AOR},
}

return picked
