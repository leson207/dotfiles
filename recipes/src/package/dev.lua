dofile("utils.lua")

local M={
    version_control={
        {
            sub_recipes={
                {
                    package={"git", Repo.AOR},
                    single_user_config={"~/.gitconfig"},
                },
                {
                    package={"less", Repo.AOR}
                },
                {
                    package={"delta", Repo.AOR}
                },
            }
        },
        {
            sub_recipes={
                {
                    package={"jujutsu", Repo.AOR}
                }
            }
        }
    },

    cpp={
        build_system={
            {
                sub_recipes={
                    {
                        package={"cmake", Repo.AOR},
                    },
                    {
                        package={"ninja", Repo.AOR}
                    }

                }
            },
            -- {
            --     sub_recipes={
            --         {
            --             package={"meson", Repo.AOR},
            --         },
            --         {
            --             package={"ninja", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"xmake", Repo.AOR},
            --         },
            --         {
            --             package={"ninja", Repo.AOR}
            --         }
            --
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"bazel", Repo.AOR},
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         package={"buck2-bin", Repo.AUR},
            --     }
            -- }
        },
        compiler_cache={
            {
                sub_recipes={
                    {
                        package={"ccache", Repo.AOR}
                    }
                }
            },
            -- {
            --     sub_recipes={
            --         {
            --             package={"scache", Repo.AOR}
            --         }
            --     }
            -- },
        },
        package_manager={
            {
                sub_recipes={
                    {
                        package={"conan-bin", Repo.AUR}
                    }
                }
            },
            -- {
            --     sub_recipes={
            --         {
            --             package={"vcpkg", Repo.AOR}
            --         }
            --     }
            -- },
        },
        language_server={
            {
                sub_recipes={
                    {
                        package={"clangb-bin", Repo.AUR},
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

    -- python={
    --     {
    --         sub_recipes={
    --             {
    --                 package={"uv", Repo.AOR}
    --             }
    --         }
    --     }
    -- },
    --
    -- rust={
    --     {
    --         sub_recipes={
    --             {
    --                 package={"rustup", Repo.AOR}
    --             }
    --         }
    --     }
    -- },
    --
    -- go={
    --     {
    --         sub_recipes={
    --             {
    --                 package={"go", Repo.AOR}
    --             }
    --         }
    --     }
    -- },
    editor={
        tui={
            -- {
            --     sub_recipes={
            --         {
            --             package={"vim", Repo.AOR}
            --         }
            --     }
            -- },
            {
                sub_recipes={
                    {
                        package={"neovim", Repo.AOR}
                    },
                    {
                        package={"luarocks", Repo.AOR}
                    }
                }
            },
            -- {
            --     sub_recipes={
            --         {
            --             package={"helix", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"kakoune", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"emacs", Repo.AOR}
            --         }
            --     }
            -- },

        },
        gui={
            {
                sub_recipes={
                    {
                        package={"zed", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"code", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"typst", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"micro", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"xi-editor", Repo.GITHUB}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"fresh-editor-bin", Repo.AUR}
                    }
                }
            },
        }
    },

    monitor={
        {
            sub_recipes={
                {
                    package={"atop", Repo.AOR},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"btop", Repo.AOR},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"htop", Repo.AOR},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"nvtop", Repo.AOR},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"glances", Repo.AOR},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"bottom", Repo.AOR},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"hyperfine", Repo.AOR},
                }
            }
        },
    },

    container={
        {
            sub_recipes={
                {
                    package={"podmand", Repo.AOR},
                    single_user_config={"~/.config/containers"},
                },
                {
                    package={"podman-compose", Repo.AOR}
                },
                {
                    package={"podman-tui", Repo.AUR}
                },
                {
                    package={"podman-desktop", Repo.AOR}
                },
            }
        }
    },

    virtual_machine={
        {
            sub_recipes={
                {
                    package={"libvirt", Repo.AOR},
                    units={"libvirtd.service", scope=Scope.MULTI_USER},
                },
                {
                    package={"qemu-desktop", Repo.AOR}
                },
                {
                    package={"dnsmasq", Repo.AOR}
                },
                {
                    package={"virt-manager", Repo.AOR}
                },
                {
                    package={"virt-viewer", Repo.AOR}
                },
            }
        }
    },

    download={
        {
            sub_recipes={
                {
                    package={"aria2", Repo.AOR},
                    single_user_config={"~/.config/aria2"}
                },
                {
                    package={"yt-dlp", Repo.AOR},
                    single_user_config={"~/.config/yt-dlp"}
                }
            }
        }
    },

    common={
        {
            sub_recipes={
                {
                    package={"tree", Repo.AOR},
                },
                {
                    package={"rsync", Repo.AOR},
                },
                {
                    package={"fastfetch", Repo.AOR},
                },
                {
                    package={"fd", Repo.AOR},
                },
                {
                    package={"fzf", Repo.AOR},
                },
                {
                    package={"ripgrep", Repo.AOR},
                },
                {
                    package={"bat", Repo.AOR},
                },
                -- {
                --     package={"eza", Repo.AOR},
                -- },
                -- {
                --     package={"zoxide", Repo.AOR},
                -- },
            }
        }
    },
}

return M
