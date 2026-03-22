dofile("utils.lua")

-- local category={
--     recipes_option=[
--         sub_recipes=[
--             package_recies={
--                 packages={}
--             }
--         ],
--         config_something={}
--     ]
-- }
-- category->recipe_option->recipes_package

local M={
    locale={
        {
            sub_recipes={
                {
                    packages={"glibc", Repo.AOR},
                    multi_user_config={
                        "/etc/locale.gen",
                        {"locale-gen"}
                    }
                },
                {
                    packages={"systemd", Repo.AOR},
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
                    packages={"systemd", Repo.AOR},
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

    init_system={
        {
            sub_recipes={
                {
                    packages={"systemd", Repo.AOR},
                    multi_user_config={
                        "/etc/hostname",
                        "/etc/vconsole.conf",
                        -- "/etc/systemd/journald.conf"
                        -- #MaxRetentionSec=7day
                    },
                    single_user_config={"~/.config/systemd"},
                }
            }
        }
    },

    boot={
        loader={
            {
                sub_recipes={
                    {
                        packages={"linux", Repo.AOR},
                    },
                    {
                        packages={"systemd", Repo.AOR},
                    },
                    {
                        packages={"intel-ucode", Repo.AOR},
                    },
                },
                multi_user_config={
                    "/boot/loader/entries/linux.conf",
                },
            },
            {
                sub_recipes={
                    {
                        packages={"linux-zen", Repo.AOR},
                    },
                    {
                        packages={"systemd", Repo.AOR},
                    },
                    {
                        packages={"intel-ucode", Repo.AOR},
                    },
                },
                multi_user_config={
                    "/boot/loader/entries/linux-zen.conf",
                },
            }
        },
        manager={
            {
                sub_recipes={
                    {
                        packages={"efibootmgr", Repo.AOR}
                    }
                }
            }
        }
    },

    permission={
        {
            sub_recipes={
                {
                    packages={"sudo", Repo.AOR}
                }
            }
        }
    },

    firmware={
        {
            sub_recipes={
                {
                    packages={"linux-firmware", Repo.AOR}
                }
            }
        }
    },

    display_server_protocol={
        {
            sub_recipes={
                {
                    packages={"wayland", Repo.AOR}
                }
            }
        }
    },

    userland={
        {
            sub_recipes={
                {
                    packages={"base", Repo.AOR}
                },
                {
                    packages={"base-devel", Repo.AOR}
                }
            }
        }
    },

    graphic={
        common={
            {
                sub_recipes={
                    {
                        packages={"mesa", Repo.AOR}
                    },
                    {
                        packages={"mesa-utils", Repo.AOR}
                    },
                    {
                        packages={"vulkan-mesa-implicit-layers", Repo.AOR}
                    },
                    {
                        packages={"libva", Repo.AOR}
                    },
                    {
                        packages={"libva-utils", Repo.AOR}
                    }
                }
            }
        },
        intel={
            {
                sub_recipes={
                    {
                        packages={"vulkan-intel", Repo.AOR}
                    },
                    {
                        packages={"libva-intel-driver", Repo.AOR},
                    },
                    {
                        packages={"intel-media-driver", Repo.AOR},
                    }
                }
            }
        },
        amd={
            {
                sub_recipes={
                    {
                        packages={
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
                        packages={"ntfs-3g", Repo.AOR},
                    }
                }
            }
        },
        mount={
            {
                sub_recipes={
                    {
                        packages={"udisks2", Repo.AOR},
                        units={name="udisks2.service", scope=Scope.MULTI_USER},
                        -- auto start here? udiskie &
                    },
                    {
                        packages={"udiskie", Repo.AOR}
                    }
                }
            }
        },
        virtual_file_system={
            {
                sub_recipes={
                    {
                        packages={"gvfs", Repo.AOR},
                    },
                    {
                        packages={"gvfs-mtp", Repo.AOR},
                    },
                    -- {
                    --     packages={"gvfs-smb", Repo.AOR},
                    -- }
                }
            }
        },
        trim={
            {
                sub_recipes={
                    {
                        packages={"util-linux", Repo.AOR},
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
                        packages={"pipewire", Repo.AOR},
                        units={"pipewire.service", scope=Scope.SINGLE_USER},
                    },
                    {
                        packages={"wireplumber", Repo.AOR},
                        units={"wireplumber.service", scope=Scope.SINGLE_USER},
                    },
                    {
                        packages={"pipewire-pulse", Repo.AOR},
                        units={"pipewire-pulse.service", scope=Scope.SINGLE_USER},
                    },
                    {
                        packages={"pipewire-audio", Repo.AOR},
                    },
                    {
                        packages={"pipewire-alsa", Repo.AOR},
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
                        packages={"networkmanager", Repo.AOR},
                        units={"NetworkManager.service", Scope.MULTI_USER},
                    },
                    {
                        packages={"iwd", Repo.AOR},
                        units={"iwd.service", Scope.MULTI_USER},
                    },
                    {
                        packages={"dnsmasq", Repo.AOR},
                        units={"dnsmasq.service", Scope.MULTI_USER},
                    }
                }
            }
        },
        ssh={
            {
                sub_recipes={
                    {
                        packages={"openssh", Repo.AOR},
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
                    packages={"tlp", Repo.AOR},
                    units={"tlp.service", Scope.MULTI_USER},
                    multi_user_config={
                        "/etc/tlp.conf"
                        -- CPU_ENERGY_PERF_POLICY_ON_BAT=power
                    }
                },
                {
                    packages={"tlp-rdw", Repo.AOR}
                },
                {
                    packages={"tlp-pd", Repo.AOR},
                    units={"tlp-pd.service", Scope.MULTI_USER}
                }
            }
        },
        -- {
        --     sub_recipes={
        --         {
        --             packages={"ananicy-cpp", Repo.AOR},
        --             units={"ananicy-cpp.service", Scope.MULTI_USER},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             packages={"tunned", Repo.AOR},
        --             units={"tunned.service", Scope.MULTI_USER},
        --         },
        --         {
        --             packages={"tunned-ppd", Repo.AOR},
        --             units={"tunned-ppd.service", Scope.MULTI_USER},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             packages={"auto-cpufreq", Repo.AUR},
        --             units={"auto-cpufreq.service", Scope.MULTI_USER},
        --         }
        --     }
        -- },
        {
            sub_recipes={
                {
                    packages={"cpupower", Repo.AUR},
                    units={"cpupower.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    packages={"preload", Repo.AUR},
                    units={"preload.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    packages={"thermald", Repo.AUR},
                    units={"thermald.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    packages={"irqbalance", Repo.AUR},
                    units={"irqbalance.service", Scope.MULTI_USER},
                }
            }
        },
        {
            sub_recipes={
                {
                    packages={"batsignal", Repo.AUR},
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

return M
