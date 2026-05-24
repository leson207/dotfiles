dofile("utils.lua")

local usecase={
    cpp={
        build_generator={
            {
                sub_recipes={
                    {
                        package={"cmake", Repo.AOR},
                    },
                }
            },
            {
                sub_recipes={
                    {
                        package={"meson", Repo.AOR},
                    },
                }
            },
        },
        build_system={
            {
                sub_recipes={
                    {
                        package={"make", Repo.AOR},
                    },
                }
            },
            {
                sub_recipes={
                    {
                        package={"ninja", Repo.AOR},
                    },
                }
            },
            {
                sub_recipes={
                    {
                        package={"xmake", Repo.AOR},
                    },
                }
            },
            {
                sub_recipes={
                    {
                        package={"bazel", Repo.AOR},
                    }
                }
            },
            {
                sub_recipes={
                    package={"buck2-bin", Repo.AUR},
                }
            }
        },
        compiler_cache={
            {
                sub_recipes={
                    {
                        package={"ccache", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"scache", Repo.AOR}
                    }
                }
            },
        },
        package_manager={
            {
                sub_recipes={
                    {
                        package={"conan-bin", Repo.AUR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"vcpkg", Repo.AOR}
                    }
                }
            },
        },
        language_server={
            {
                sub_recipes={
                    {
                        package={"clangd-bin", Repo.AUR},
                    },
                    {
                        package={"bear", Repo.AOR},
                    }
                }
            }
        },
        compiler={
            {
                sub_recipes={
                    {
                        package={"gcc", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"clang", Repo.AOR}
                    }
                }
            }
        },
        linker={
            {
                sub_recipes={
                    {
                        package={"ld", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"lld", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"mold", Repo.AOR}
                    }
                }
            },
        },
        std_lib={
            {
                sub_recipes={
                    {
                        package={"libc++", Repo.AOR},
                    },
                    {
                        package={"libc++abi", Repo.AOR},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"libstdc++", Repo.AOR},
                    },
                    {
                        package={"libstdc++abi", Repo.AOR},
                    }
                }
            }
        }
    },
}

local vendor={
    gnu={
        sub_recipes={
            {
                package={"gcc", Repo.AOR}
            },
            {
                package={"ld", Repo.AOR}
            },
            {
                package={"libc++", Repo.AOR},
            },
            {
                package={"libc++abi", Repo.AOR},
            }
        }
    },
    llvm={
        sub_recipes={
            {
                package={"clang", Repo.AOR}
            },
            {
                package={"lld", Repo.AOR}
            },
            {
                package={"libcstd++", Repo.AOR},
            },
            {
                package={"libcstd++abi", Repo.AOR},
            }
        }
    }
}

local picked={
    sub_recipes={
        {
            package={"make", Repo.AOR}
        },
        {
            package={"ccache", Repo.AOR}
        },
        {
            package={"clangd-bin", Repo.AOR}
        },
        {
            package={"bear", Repo.AOR}
        },
        {
            package={"gcc", Repo.AOR}
        },
        {
            package={"ld", Repo.AOR}
        },
        {
            package={"libc++", Repo.AOR},
        },
        {
            package={"libc++abi", Repo.AOR},
        }
    }
}

return picked
