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
    -- user={
    --     {
    --         name="victor",
    --         groups={"wheel"}
    --     }
    -- },

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
                    {
                        package={"mkinitcpio", Repo.AOR},
                        multi_user_config={
                            "/etc/mkinitcpio.conf"
                        }
                    }
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
                    {
                        package={"mkinitcpio", Repo.AOR},
                        multi_user_config={
                            "/etc/mkinitcpio.conf"
                        }
                    }
                },
                multi_user_config={
                    "/boot/loader/entries/linux-zen.conf",
                },
            },
            {
                sub_recipes={
                    {
                        package={"linux-cachyos-bore", Repo.AUR},
                    },
                    {
                        package={"systemd", Repo.AOR},
                    },
                    {
                        package={"intel-ucode", Repo.AOR},
                    },
                    {
                        package={"mkinitcpio", Repo.AOR},
                        multi_user_config={
                            "/etc/mkinitcpio.conf"
                        }
                    }
                },
                multi_user_config={
                    "/boot/loader/entries/linux-cachyos-bore.conf",
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
                },
                {
                    package={"atuin", Repo.AOR},
                    single_user_config={"~/.config/atuin"},
                    auto_start={{"atuin", "daemon", "start"}}
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
    -- misc={
    --     {
    --         env={
    --             XCURSOR_SIZE=24,
    --             _JAVA_AWT_WM_NONREPARENTING=1,
    --         }
    --     }
    -- },

    bus={
        {
            sub_recipes={
                {
                    package={"dbus", Repo.AOR},
                    auto_start={
                        {"dbus-update-activation-environment", "--systemd", "WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"}
                    }
                }
            }
        }
    },

    disk={
        device_management={
            {
                sub_recipes={
                    {
                        package={"udisks2", Repo.AOR},
                        units={name="udisks2.service", scope=Scope.MULTI_USER},
                    },
                }
            }
        },
        fs_utility={
            {
                sub_recipes={
                    {
                        package={"e2fsprogs", Repo.AOR}
                    },
                    {
                        package={"exfatprogs", Repo.AOR}
                    },
                    {
                        package={"ntfs-3g", Repo.AOR}
                    }
                }
            }
        },
        user_integration={
            {
                sub_recipes={
                    {
                        package={"udiskie", Repo.AOR},
                        auto_start={{"udiskie", "&"}}
                    },
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
        maintenance={
            {
                sub_recipes={
                    {
                        package={"util-linux", Repo.AOR},
                        units={"fstrim.timer", Scope.MULTI_USER}
                    }
                }
            }
        }
    },

    initramfs_image_creator={
        {
            sub_recipes={
                {
                    package={"mkinitcpio", Repo.AOR},
                    multi_user_config={
                        "/etc/mkinitcpio.conf",
                        "/etc/mkinitcpio.conf.d"
                    }
                }
            }
        },
        -- {
        --     sub_recipes={
        --         {
        --             package={"dracut", Repo.AOR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"booster", Repo.AOR},
        --         }
        --     }
        -- },
    },

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
        },
        {
            sub_recipes={
                {
                    package={"linux-cachyos-bore", Repo.AUR}
                },
                {
                    package={"linux-cachyos-bore-headers", Repo.AUR}
                }
            }
        }
    },

    -- c_library={
    --     {
    --         sub_recipes={
    --             {
    --                 package={"glibc", Repo.AOR}
    --             }
    --         }
    --     }
    -- },

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
                    multi_user_config={
                        -- "/etc/hostname",
                        -- "/etc/vconsole.conf",
                        -- "/etc/systemd/journald.conf"
                        -- #MaxRetentionSec=7day
                    },
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
                    package={"wayland", Repo.AOR},
                    env={
                        SDL_VIDEODRIVER="wayland",
                        CLUTTER_BACKEND="wayland",
                    }
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
                        package={"vulkan-radeon", Repo.AOR}
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
            },
        },
        ssh={
            {
                sub_recipes={
                    {
                        package={"openssh", Repo.AOR},
                        units={"sshd.service", Scope.MULTI_USER},
                        -- units={"sshdgenkeys.service", Scope.MULTI_USER}
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
                    package={"reflector", Repo.AUR},
                    units={"reflector.timer", Scope.MULTI_USER},
                }
            }
        }
    }
}

return {FunctionSettingRecipes, RoleRecipes}
