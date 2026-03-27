dofile("utils.lua")

local M={
    keylogger={
        {
            sub_recipes={
                {
                    package={"logkeys", Repo.AUR}
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"whatpulse", Repo.AUR}
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"osa", Repo.AUR}
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"keymouse-logger", Repo.AUR}
                }
            }
        },
    },

    misc={
        {
            sub_recipes={
                {
                    package={"broot", Repo.AOR},
                },
                {
                    package={"dust", Repo.AOR},
                },
                {
                    package={"dua-cli", Repo.AOR},
                },
                {
                    package={"progress", Repo.AOR},
                },
                {
                    package={"broot", Repo.AOR},
                },

                {
                    package={"hugo", Repo.AOR}
                },
                {
                    package={"cava", Repo.AOR},
                    single_user_config={"~/.config/cava"},
                },
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
    text_editor={
        tui={
            {
                sub_recipes={
                    {
                        package={"vim", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"helix", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"kakoune", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"emacs", Repo.AOR}
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
                        package={"xi-editor", Repo.GITHUB}
                    }
                }
            },
        }
    },

    terminal={
        emulator={
            {
                sub_recipes={
                    {
                        package={"kitty", Repo.AOR},
                        single_user_config={"~/.config/kitty"},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"aclacritty", Repo.AOR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"ghostty", Repo.AOR},
                        units={"app-com.mitchellh.ghostty.service", Scope.SINGLE_USER},
                    }
                }
            }
        }
    },

    notification={
        -- {
        --     sub_recipes={
        --         {
        --             package={"fnott", Repo.AOR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"dunst", Repo.AOR},
        --             single_user_config={"~/.config/dunst"},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"mako", Repo.AOR},
        --             units={"mako.service", Scope.SINGLE_USER},
        --             single_user_config={"~/.config/mako"},
        --         }
        --     }
        -- },
    },
    -- widget_system={
    --     {
    --         sub_recipes={
    --             {
    --                 package={"quickshell", Repo.AOR}
    --             }
    --         }
    --     },
    --     {
    --         sub_recipes={
    --             {
    --                 package={"eww", Repo.AOR}
    --             }
    --         }
    --     },
    --     {
    --         sub_recipes={
    --             {
    --                 package={"ags", Repo.AOR}
    --             }
    --         }
    --     },
    -- }
    window_compositor={
        -- {
        --     sub_recipes={
        --         {
        --             package={"niri", Repo.AOR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"river", Repo.AOR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"mangowc", Repo.AOR},
        --         }
        --     }
        -- },
    },

    color_extractor={
        -- {
        --     sub_recipes={
        --         {
        --             package={"python-pywal", Repo.AOR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"wallust", Repo.AUR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"hellwall", Repo.AUR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"kde-material-you-colors", Repo.AUR},
        --         }
        --     }
        -- },
    },
    wallpaper={
        setter={
            -- {
            --     sub_recipes={
            --         {
            --             package={"awww-bin", Repo.AUR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"swaybg", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"mpvpaper", Repo.AUR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"wpaperd", Repo.AOR}
            --         }
            --     }
            -- },
        },
        picker={
            -- {
            --     sub_recipes={
            --         {
            --             package={"waypaper", Repo.AUR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"wallrizz", Repo.GITHUB}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"waytrogen-bin", Repo.AUR}
            --         }
            --     }
            -- },
        }
    },
    power_and_performance={
        -- {
        --     sub_recipes={
        --         {
        --             package={"ananicy-cpp", Repo.AOR},
        --             units={"ananicy-cpp.service", Scope.MULTI_USER},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"tunned", Repo.AOR},
        --             units={"tunned.service", Scope.MULTI_USER},
        --         },
        --         {
        --             package={"tunned-ppd", Repo.AOR},
        --             units={"tunned-ppd.service", Scope.MULTI_USER},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"auto-cpufreq", Repo.AUR},
        --             units={"auto-cpufreq.service", Scope.MULTI_USER},
        --         }
        --     }
        -- },
    },
    screen={
        capture={
            -- {
            --     sub_recipes={
            --         {
            --             package={"grim", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"flameshot", Repo.AOR}
            --         }
            --     }
            -- },
        },
        crop={
            sub_recipes={
                {
                    package={"slurp", Repo.AOR}
                }
            }
        },
        annotate={
            {
                sub_recipes={
                    {
                        package={"swappy", Repo.AOR},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"satty", Repo.AOR},
                    }
                }
            }
        },
        record={
            -- {
            --     sub_recipes={
            --         {
            --             package={"wl-screenrec", Repo.AUR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"obs-studio", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"wf-recorder", Repo.AOR}
            --         }
            --     }
            -- },
        }
    },
    opener={
        image={
            -- {
            --     sub_recipes={
            --         {
            --             package={"imv", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"feh", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"gthumb", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"swayimg", Repo.AOR}
            --         }
            --     }
            -- },
        },
    },

    remapper={
        -- {
        --     sub_recipes={
        --         {
        --             package={"wlr-which-key", Repo.AUR}
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"xremap-hypr-bin", Repo.AUR}
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"xremap-wlroots-bin", Repo.AUR}
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"input-remapper-bin", Repo.AUR}
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"keyd", Repo.AOR}
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"kmonad", Repo.AOR}
        --         }
        --     }
        -- },
    }
}
