dofile("utils.lua")

-- local category={
--     recipes_option=[
--         sub_recipes=[
--             package_recies={
--                 package={}
--             }
--         ],
--         config_something={}
--     ]
-- }
-- category->recipe_option->recipes_package

local FunctionSettingRecipes={
    locale={
        {
            sub_recipes={
                {
                    package={"glibc", Repo.AOR},
                    multi_user_config={
                        "/etc/locale.gen",
                        {"locale-gen"}
                    }
                },
                {
                    package={"systemd", Repo.AOR},
                    multi_user_config={
                        "/etc/locale.conf",
                        -- { "localectl", "set-locale", "LANG=en_US.UTF-8" }
                    },
                },
            },
        }
    },

    time={
        {
            sub_recipes={
                {
                    package={"systemd", Repo.AOR},
                    units={"systemd-timesyncd", Scope.MULTI_USER},
                    multi_user_config={
                        {"sudo", "timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"},
                        {"sudo", "timedatectl", "set-ntp", "true"},
                        {"sudo", "timedatectl", "set-local-rtc", "0"},
                        {"timedatectl", "status"},
                        {"hwclock", "--systohc"},
                    }
                }
            }
        }
    },

    boot={
        loader={
            {
                sub_recipes={
                    {
                        package={"linux", Repo.AOR},
                    },
                    {
                        package={"systemd", Repo.AOR},
                    },
                    {
                        package={"intel-ucode", Repo.AOR},
                    },
                },
                multi_user_config={
                    "/boot/loader/entries/linux.conf",
                },
            },
            {
                sub_recipes={
                    {
                        package={"linux-zen", Repo.AOR},
                    },
                    {
                        package={"systemd", Repo.AOR},
                    },
                    {
                        package={"intel-ucode", Repo.AOR},
                    },
                },
                multi_user_config={
                    "/boot/loader/entries/linux-zen.conf",
                },
            }
        },
    },

    shell={
        {
            sub_recipes={
                {
                    package={"nushell", Repo.AOR},
                    single_user_config={
                        "~/.config/nushell/env.nu",
                        "~/.config/nushell/config.nu",
                    },
                    personalized_data={
                        "~/.config/nushell/history.txt",
                        "~/.config/nushell/history.sqlite3"
                    }
                },
                {
                    package={"atuin", Repo.AOR},
                },
                {
                    package={"starship", Repo.AOR},
                    single_user_config={"~/.config/starship.toml"},
                },
            },
            single_user_config={
                {"mkdir", "~/.local/share/atuin/"},
                {"atuin", "init", "nu", "|", "save", "~/.local/share/atuin/init.nu"},

                {"mkdir", "($nu.data-dir | path join \"vendor/autoload\")"},
                {"starship", "init", "nu", "|", "save", "-f", "($nu.data-dir | path join \"vendor/autoload/starship.nu\")"}
            }
        },
    }
}

local RoleRecipes={
    kernel={
        {
            sub_recipes={
                {
                    package={"linux", Repo.AOR}
                },
                {
                    package={"linux-headers", Repo.AOR}
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"linux-zen", Repo.AOR}
                },
                {
                    package={"linux-zen-headers", Repo.AOR}
                }
            }
        }
    },

    c_library={
        {
            sub_recipes={
                {
                    package={"glibc", Repo.AOR}
                }
            }
        }
    },

    core_tools={
        {
            sub_recipes={
                {
                    package={"coreutils", Repo.AOR}
                }
            }
        }
    },

    init_system={
        {
            sub_recipes={
                {
                    package={"systemd", Repo.AOR},

                    single_user_config={"~/.config/systemd"},
                },
                multi_user_config={
                    -- is this really systemd config or just general thing use by systemd
                    -- "/etc/hostname",
                    -- "/etc/vconsole.conf",
                    -- "/etc/systemd/journald.conf"
                    -- #MaxRetentionSec=7day
                },
        }
        }
    },

    userland={
        {
            sub_recipes={
                {
                    package={"base", Repo.AOR}
                },
                {
                    package={"base-devel", Repo.AOR}
                }
            }
        }
    },

    boot={
        loader={
            {
                sub_recipes={
                    {
                        package={"systemd", Repo.AOR},
                    }
                },
                multi_user_config={"/boot/loader/entries"},
            }
        },
        manager={
            {
                sub_recipes={
                    {
                        package={"efibootmgr", Repo.AOR}
                    }
                }
            }
        }
    },

    microcode={
        {
            sub_recipes={
                {
                    package={"intel-ucode", Repo.AOR}
                }
            }
        }
    },

    permission={
        {
            sub_recipes={
                {
                    package={"sudo", Repo.AOR}
                }
            }
        }
    },

    firmware={
        {
            sub_recipes={
                {
                    package={"linux-firmware", Repo.AOR}
                }
            }
        }
    },

    display_server_protocol={
        {
            sub_recipes={
                {
                    package={"wayland", Repo.AOR}
                }
            }
        }
    },

    graphic={
        common={
            {
                sub_recipes={
                    {
                        package={"mesa", Repo.AOR}
                    },
                    {
                        package={"mesa-utils", Repo.AOR}
                    },
                    {
                        package={"vulkan-mesa-implicit-layers", Repo.AOR}
                    },
                    {
                        package={"libva", Repo.AOR}
                    },
                    {
                        package={"libva-utils", Repo.AOR}
                    }
                }
            }
        },
        intel={
            {
                sub_recipes={
                    {
                        package={"vulkan-intel", Repo.AOR}
                    },
                    {
                        package={"libva-intel-driver", Repo.AOR},
                    },
                    {
                        package={"intel-media-driver", Repo.AOR},
                    }
                }
            }
        },
        amd={
            {
                sub_recipes={
                    {
                        package={
                            {"vulkan-radeon", Repo.AOR},
                        }
                    }
                }
            }
        }
    },

    disk={
        driver={
            {
                sub_recipes={
                    {
                        package={"ntfs-3g", Repo.AOR},
                    }
                }
            }
        },
        mount={
            {
                sub_recipes={
                    {
                        package={"udisks2", Repo.AOR},
                        units={name="udisks2.service", scope=Scope.MULTI_USER},
                        -- auto start here? udiskie &
                    },
                    {
                        package={"udiskie", Repo.AOR}
                    }
                }
            }
        },
        virtual_file_system={
            {
                sub_recipes={
                    {
                        package={"gvfs", Repo.AOR},
                    },
                    {
                        package={"gvfs-mtp", Repo.AOR},
                    },
                    -- {
                    --     package={"gvfs-smb", Repo.AOR},
                    -- }
                }
            }
        },
        trim={
            {
                sub_recipes={
                    {
                        package={"util-linux", Repo.AOR},
                        units={"fstrim.service", Scope.MULTI_USER}
                    }
                }
            }
        }
    },

    audio={
        processor={
            {
                sub_recipes={
                    {
                        package={"pipewire", Repo.AOR},
                        units={"pipewire.service", scope=Scope.SINGLE_USER},
                    },
                    {
                        package={"wireplumber", Repo.AOR},
                        units={"wireplumber.service", scope=Scope.SINGLE_USER},
                    },
                    {
                        package={"pipewire-pulse", Repo.AOR},
                        units={"pipewire-pulse.service", scope=Scope.SINGLE_USER},
                    },
                    {
                        package={"pipewire-audio", Repo.AOR},
                    },
                    {
                        package={"pipewire-alsa", Repo.AOR},
                    }
                }
            }
        }
    },

    network={
        internet={
            {
                sub_recipes={
                    {
                        package={"networkmanager", Repo.AOR},
                        units={"NetworkManager.service", Scope.MULTI_USER},
                    },
                    {
                        package={"iwd", Repo.AOR},
                        units={"iwd.service", Scope.MULTI_USER},
                    },
                    {
                        package={"dnsmasq", Repo.AOR},
                        units={"dnsmasq.service", Scope.MULTI_USER},
                    }
                }
            }
        },
        ssh={
            {
                sub_recipes={
                    {
                        package={"openssh", Repo.AOR},
                        units={"sshd.service", Scope.MULTI_USER}
                    }
                }
            }
        }
    },

    power_and_performance={
        {
            sub_recipes={
                {
                    package={"tlp", Repo.AOR},
                    units={"tlp.service", Scope.MULTI_USER},
                    multi_user_config={
                        "/etc/tlp.conf"
                        -- CPU_ENERGY_PERF_POLICY_ON_BAT=power
                    }
                },
                {
                    package={"tlp-rdw", Repo.AOR}
                },
                {
                    package={"tlp-pd", Repo.AOR},
                    units={"tlp-pd.service", Scope.MULTI_USER}
                }
            }
        },
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
        {
            sub_recipes={
                {
                    package={"cpupower", Repo.AUR},
                    units={"cpupower.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"preload", Repo.AUR},
                    units={"preload.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"thermald", Repo.AUR},
                    units={"thermald.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"irqbalance", Repo.AUR},
                    units={"irqbalance.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"batsignal", Repo.AUR},
                    units={"batsignal.service", Scope.MULTI_USER},
                }
            }
        },
    },

    package_manager={
        -- {
        --     sub_recipes={
        --         {
        --             package={"guix", Repo.AUR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"nix", Repo.AUR},
        --         }
        --     }
        -- },
        {
            sub_recipes={
                {
                    package={"pacman", Repo.AUR},
                    multi_user_config={"/etc/pacman.conf"}
                },
                {
                    package={"refector", Repo.AUR},
                    units={"refector.timer", Scope.MULTI_USER},
                }
            }
        }
    }
}

return RoleRecipes, FunctionSettingRecipes
