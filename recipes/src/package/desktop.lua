dofile("utils.lua")

local M={
    dotfile_manager={
        {
            sub_recipes={
                {
                    package={"stow", Repo.AOR},
                }
            }
        },
        -- {
        --     sub_recipes={
        --         {
        --             package={"chemzmoi", Repo.AOR},
        --         }
        --     }
        -- }
    },

    xdg={
        {
            sub_recipes={
                {
                    package={"xdg-desktop-portal-gtk", Repo.AOR},
                },
                {
                    package={"xdg-desktop-portal-hyprland", Repo.AOR},
                    env={
                        -- XDG_CURRENT_DESKTOP="Hyprland",
                        -- XDG_SESSION_TYPE="wayland"
                    }
                },
                {
                    package={"xdg-user-dirs", Repo.AOR},
                    units={"xdg-user-dirs.service", Scope.SINGLE_USER},
                },
                {
                    package={"xdg-utils", Repo.AOR},
                },
            }
        }
    },

    window_compositor={
        {
            sub_recipes={
                {
                    package={"hyprland", Repo.AOR},
                    single_user_config={
                        "~/.config/hypr/hyprland",
                        "~/.config/hypr/hyprland.conf",
                        "~/.config/uwsm/env-hyprland",
                        {"sh", "~/.config/hypr/hyprland/scripts/first_intel_gpu.sh"},
                        {"sh", "~/.config/hypr/hyprland/scripts/first_amd_gpu.sh"},
                    },
                    env={
                        HYPRCURSOR_SIZE="24",
                        AQ_DRM_DEVICES="/dev/dri/first-intel-gpu:/dev/dri/first-amd-gpu"
                    }
                }
            }
        },
    },

    session_manager={
        {
            sub_recipes={
                {
                    package={"uwsm", Repo.AUR},
                    single_user_config={"~./config/uwsm"},
                },
                {
                    package={"libnewt", Repo.AOR},
                },
                {
                    package={"app2unit", Repo.AUR},
                    env={
                        APP2UNIT_SLICES="a=app-graphical.slice b=background-graphical.slice s=session-graphical.slice"
                    }
                },
            }
        }
    },

    display_manager={
        {
            sub_recipes={
                {
                    package={"sddm", Repo.AOR},
                    units={"sddm.service", Scope.MULTI_USER},
                    multiple_user_setting={
                        "/etc/sddm.conf",
                        "/etc/sddm.conf.d/virtualkbd.conf",
                    }
                },
                {
                    package={"qt6-svg", Repo.AOR}
                },
                {
                    package={"qt6-wayland", Repo.AOR}
                },
                {
                    package={"qt6-virtualkeyboard", Repo.AOR}
                },
                {
                    package={"qt6-multimedia-ffmpeg", Repo.AOR}
                },
            },
            multiple_user_setting={
                {"sudo", "git", "clone", "-b", "master", "--depth", "1", "https://github.com/keyitdev/sddm-astronaut-theme.git", "/usr/share/sddm/themes/sddm-astronaut-theme"},
                {"sudo", "cp", "-r", "/usr/share/sddm/themes/sddm-astronaut-theme/Fonts/*", "/usr/share/fonts/"},
                "/usr/share/sddm/themes/sddm-astronaut-theme/metadata.desktop"
            }
        }
    },

    screen_sharing={
        {
            sub_recipes={
                {
                    package={"xdg-desktop-portal-gtk", Repo.AOR}
                },
                {
                    package={"xdg-desktop-portal-hyprland", Repo.AOR}
                },
                {
                    package={"grim", Repo.AOR}
                },
                {
                    package={"slurp", Repo.AOR}
                },
            }
        }
    },

    bar={
        {
            sub_recipes={
                {
                    package={"waybar", Repo.AOR},
                    units={"waybar.service", Scope.SINGLE_USER},
                    single_user_config={"~/.config/waybar"}
                }
            }
        },
        -- {
        --     sub_recipes={
        --         {
        --             package={"ashell", Repo.AUR},
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"hyprpanel", Repo.AUR},
        --         }
        --     }
        -- },
    },

    color_extractor={
        {
            sub_recipes={
                {
                    package={"matugen", Repo.AOR},
                    single_user_config={"~/.config/matugen"},
                }
            }
        },
    },

    qt={
        misc={
            {
                env={
                    QT_QPA_PLATFORM="wayland;xcb",
                    QT_ENABLE_HIGHDPI_SCALING=1,
                    QT_AUTO_SCREEN_SCALE_FACTOR=1,
                    QT_WAYLAND_DISABLE_WINDOWDECORATION=1,
                }
            }
        },
        theme_config={
            {
                sub_recipes={
                    {
                        package={"qt5ct", Repo.AOR},
                        single_user_config={"~/.config/qt5ct"},
                    },
                    {
                        package={"qt6ct", Repo.AOR},
                        single_user_config={"~/.config/qt6ct"},
                        env={
                            QT_QPA_PLATFORMTHEME="qt6ct"
                        }
                    },
                    -- {
                    --     package={"hyprqt6engine", Repo.AUR},
                    -- },
                    {
                        package={"kvantum", Repo.AOR},
                        single_user_config={"~/.config/Kvantum"},
                        env={
                            QT_STYLE_OVERRIDE="kvantum"
                        }
                    }
                }
            }
        },
    },

    gtk={
        misc={
            {
                env={
                    GDK_SCALE=1,
                    GDK_DPI_SCALE=1,
                    GDK_BACKEND="wayland,x11",
                }
            }
        },
        theme_config={
            {
                sub_recipes={
                    {
                        single_user_config={
                            "~/.config/gtk-3.0",
                            "~/.config/gtk-4.0"
                        }
                    },
                    {
                        package={"nwg-look", Repo.AOR},
                        single_user_config={"~/.config/nwg-look"},
                    },
                }
            }
        },
        theme={
            {
                sub_recipes={
                    {
                        package={"orchis-theme", Repo.AOR}
                    },
                    {
                        package={"vimix-cursors", Repo.AOR}
                    },
                    {
                        package={"tela-circle-icon-theme", Repo.AOR}
                    }
                }
            }
        }
    },

    wallpaper={
        setter={
            {
                sub_recipes={
                    {
                        package={"hyprpaper", Repo.AOR},
                        units={"hyprpaper.service", Scope.SINGLE_USER},
                        single_user_config={"~/.config/hypr/hyprpaper.conf"}
                    }
                } }
        },
        picker={
            {
                sub_recipes={
                    {
                        package={"rofi", Repo.AOR},
                        single_user_config={"~/.config/rofi"},
                    }
                }
            },
        }
    },

    screen_lock={
        {
            sub_recipes={
                {
                    package={"hyprlock", Repo.AOR},
                    single_user_config={"~/.config/hypr/hyprlock.conf"}
                }
            }
        }
    },

    polkit_agent={
        {
            sub_recipes={
                {
                    package={"hyprpolkitagent", Repo.AOR},
                    units={"hypridle.service", Scope.SINGLE_USER},
                    single_user_config={"~/.config/hypr/hypridle.conf"}
                }
            }
        }
    },

    backlight={
        {
            sub_recipes={
                {
                    package={"hyprsunset", Repo.AOR},
                    units={"hyprsunset.service", Scope.SINGLE_USER},
                    single_user_config={"~/.config/hypr/hyprsunset.conf"}
                }
            }
        }
    },

    launcher={
        {
            sub_recipes={
                package={"fuzzel", Repo.AOR},
                single_user_config={"~/.config/fuzzel"},
            }
        },
        {
            sub_recipes={
                package={"hyprpicker", Repo.AOR},
                single_user_config={"~/.config/hypr/hyprlauncher.conf"},
            }
        }
    },

    notification={
        {
            sub_recipes={
                {
                    package={"swaync", Repo.AOR},
                    units={"swaync.service", Scope.SINGLE_USER},
                    single_user_config={"~/.config/swaync"},
                }
            }
        },
    },

    clipboard={
        copy_paste={
            {
                sub_recipes={
                    {
                        package={"wl-clipboard", Repo.AOR}
                    },
                    {
                        package={"wl-clip-persist", Repo.AOR},
                        auto_start={{"wl-clip-persist", "--clipboard regular"}}
                    }
                }
            }
        },
        history={
            {
                sub_recipes={
                    {
                        -- TODO: how and should i declate it config in hyprland?
                        package={"cliphist", Repo.AOR},
                        units={"cliphist.service", Scope.SINGLE_USER},
                        auto_start={
                            {"wl-paste", "--type", "text", "watch", "cliphist", "store"},
                            {"wl-paste", "--type", "image", "watch", "cliphist", "store"},
                        }
                    }
                }
            },
            -- {
            --     sub_recipes={
            --         {
            --             package={"copyq", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"nwg-clipman", Repo.AOR}
            --         }
            --     }
            -- },
        },
    },

    input={
        method={
            {
                sub_recipes={
                    {
                        package={"fcitx5", Repo.AOR},
                        single_user_config={
                            "~/.config/fcitx5/config",
                            "~/.config/fcitx5/profile"
                        },
                    },
                    {
                        package={"fcitx5-gtk", Repo.AOR}
                    },
                    {
                        package={"fcitx5-qt", Repo.AOR}
                    },
                    {
                        package={"fcitx5-configtool", Repo.AOR}
                    },
                    {
                        package={"fcitx5-unikey", Repo.AOR}
                    },
                    -- {
                    --     package={"fcitx5-bamboo", Repo.AOR}
                    -- },
                    -- {
                    --     package={"fcitx5-lotus", Repo.AUR}
                    -- },
                },
                env={
                    QT_IM_MODULE="fcitx",
                    -- GTK_IM_MODULE="fcitx",
                    XMODIFIERS="@im=fcitx"
                }
            }
        }
    },

    remapper={
        {
            sub_recipes={
                {
                    package={"kanata-bin", Repo.AUR},
                    multiple_user_config={
                        "/etc/udev/rules.d/99-uinput.rules",
                        -- KERNEL=="uinput", MODE="0660", GROUP="uinput", OPTIONS+="static_node=uinput"
                        {"sudo", "udevadm", "control", "--reload"},
                        {"sudo", "udevadm", "trigger", "--verbose", "--sysname-match=uinput"},
                        {"sudo", "modprobe", "-r", "uinput"},
                        {"sudo", "modprobe", "uinput"}
                    },
                    -- sudo groupadd uinput
                    -- sudo usermod -aG input $USER
                    -- sudo usermod -aG uinput $USER
                    groups={
                        "input",
                        "uinput",
                    },
                    resource={
                        "https://shom.dev/start/using-kanata-to-remap-any-keyboard/"
                    }
                }
            }
        },
    },

    fonts={
        {
            sub_recipes={
                {
                    package={"noto-fonts", Repo.AOR}
                },
                {
                    package={"noto-fonts-cjk", Repo.AOR}
                },
                {
                    package={"noto-fonts-emoji", Repo.AOR}
                },
            }
        },
        {
            sub_recipes={
                {
                    package={"ttf-opensans", Repo.AOR}
                },
                {
                    package={"ttf-fira-code", Repo.AOR}
                },
                {
                    package={"ttf-cascadia-code-nerd", Repo.AOR}
                },
                {
                    package={"ttf-jetbrains-mono-nerd", Repo.AOR}
                },
            }
        },
        {
            sub_recipes={
                {
                    package={"tex-gyre-fonts", Repo.AOR}
                }
            }
        }
    },

    shell={
        -- {
        --     sub_recipes={
        --         {
        --             package={"zsh", Repo.AOR}
        --         }
        --     }
        -- },
        -- {
        --     sub_recipes={
        --         {
        --             package={"fish", Repo.AOR}
        --         }
        --     }
        -- },
        {
            sub_recipes={
                {
                    package={"bash", Repo.AOR},
                    single_user_config={"~/.bashrc", "~/.bash_profile"},
                }
            }
        },
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
                    single_user_config={
                        "~/.config/atuin",
                        {"mkdir", "~/.local/share/atuin/"},
                        {"atuin", "init", "nu", "|", "save", "~/.local/share/atuin/init.nu"}
                    }
                },
                {
                    package={"starship", Repo.AOR},
                    single_user_config={
                        "~/.config/starship.toml",
                        {"mkdir", "($nu.data-dir | path join \"vendor/autoload\")"},
                        {"starship", "init", "nu", "|", "save", "-f", "($nu.data-dir | path join \"vendor/autoload/starship.nu\")"}
                    },
                }
            }
        },
    },

    teminal={
        emulator={
            {
                sub_recipes={
                    {
                        package={"foot", Repo.AOR},
                        units={"foot-server.socket", Scope.SINGLE_USER},
                        single_user_config={"~/.config/foot"},
                        auto_start={{"foot", "--server"}}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"wezterm-git", Repo.AUR},
                        single_user_config={"~/.config/wezterm"}
                    }
                }
            },
        },
        multiplexer={
            {
                sub_recipes={
                    {
                        package={"tmux", Repo.AOR},
                        single_user_config={"~/.tmux.conf"},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"zellij", Repo.AOR}
                    }
                }
            }
        }
    },

    file={
        manager={
            {
                sub_recipes={
                    {
                        package={"thunar", Repo.AOR},
                    },
                    {
                        package={"thunar-volman", Repo.AOR},
                    },
                    {
                        package={"thunar-archive-plugin", Repo.AOR},
                    },
                    {
                        package={"thunar-media-tags-plugin", Repo.AOR},
                    },

                    -- {
                    --     package={"catfish", Repo.AOR},
                    -- },
                    -- {
                    --     package={"plocate", Repo.AOR},
                    -- },
                    -- {
                    --     package={"zeitgeist", Repo.AOR},
                    -- },
                    -- {
                    --     package={"clamav", Repo.AOR},
                    -- },
                    -- {
                    --     package={"clamtk", Repo.AOR},
                    -- },
                },
                auto_start={{"thunar", "--daemon"}}
            },
            {
                sub_recipes={
                    {
                        package={"yazi", Repo.AOR}
                    },
                    {
                        package={"7zip", Repo.AOR}
                    },
                    {
                        package={"chafa", Repo.AOR}
                    },
                    {
                        package={"jq", Repo.AOR}
                    },
                    {
                        package={"poppler", Repo.AOR}
                    },
                    {
                        package={"resvg", Repo.AOR}
                    },
                    {
                        package={"imagemagick", Repo.AOR}
                    },
                }
            },
            -- {
            --     sub_recipes={
            --         {
            --             package={"superfile", Repo.AOR}
            --         }
            --     }
            -- }
        },
        misc={
            {
                sub_recipes={
                    {
                        package={"xdg_user_dirs", Repo.AOR},
                        units={"xdg-user-dirs-update.service", Scope.SINGLE_USER},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"krokiet-bin", Repo.AUR}
                    }
                }
            }
        },

        thumnail={
            {
                sub_recipes={
                    {
                        {
                            package={"tumbler", Repo.AOR},
                            units={"tumblerd.service", Scope.SINGLE_USER},
                        },
                        {
                            package={"ffmpegthumbnailer", Repo.AOR},
                        },
                        {
                            package={"freetype2", Repo.AOR},
                        },
                        {
                            package={"libgepub", Repo.AOR},
                        },
                        {
                            package={"libgsf", Repo.AOR},
                        },
                        {
                            package={"libopenraw", Repo.AOR},
                        },
                        {
                            package={"poppler-glib", Repo.AOR},
                        },
                    }
                }
            }
        }
    },

    opener={
        video={
            {
                sub_recipes={
                    {
                        package={"mpv", Repo.AOR},
                        single_user_config={"~/.config/mpv"},
                    }
                }
            },
            -- {
            --     sub_recipes={
            --         {
            --             package={"vlc", Repo.AOR}
            --         }
            --     }
            -- },
            -- {
            --     sub_recipes={
            --         {
            --             package={"clapper", Repo.AOR}
            --         }
            --     }
            -- },
        },

        image={
            {
                sub_recipes={
                    {
                        -- gui
                        package={"mpv", Repo.AOR},
                        single_user_config={"~/.config/mpv"},
                    },
                    {
                        -- tui
                        package={"ueberzugpp", Repo.AOR},
                    },
                }
            },
        },

        office={
            {
                sub_recipes={
                    {
                        package={"libreoffice-fresh", Repo.AOR},
                    },
                    {
                        package={"libreoffice-fresh-en-gb", Repo.AOR},
                    },
                    {
                        package={"libreoffice-fresh-vi", Repo.AOR},
                    },
                }
            },
            {
                sub_recipes={
                    {
                        package={"onlyoffice-bin", Repo.AUR}
                    }
                }
            }
        },

        text={
            {
                sub_recipes={
                    {
                        package={"featherpad", Repo.AOR}
                    },
                }
            }
        },

        pdf={
            {
                sub_recipes={
                    {
                        package={"zathura", Repo.AOR}
                    },
                    {
                        package={"zathura-pdf-poppler", Repo.AOR}
                    },
                }
            }
        },

        archive={
            compress={
                {
                    sub_recipes={
                        {
                            package={"tar", Repo.AOR}
                        },
                        {
                            package={"gzip", Repo.AOR}
                        },
                        {
                            package={"bzip2", Repo.AOR}
                        },
                        {
                            package={"xz", Repo.AOR}
                        },
                        {
                            package={"zstd", Repo.AOR}
                        },
                    }
                }
            },
            package_compress={
                {
                    sub_recipes={
                        {
                            package={"libarchive", Repo.AOR}
                        },
                        {
                            package={"unrar", Repo.AOR}
                        },
                        {
                            package={"unzip", Repo.AOR}
                        },
                        {
                            package={"7zip", Repo.AOR}
                        },
                        {
                            package={"zip", Repo.AOR}
                        },
                    }
                }
            },
            gui={
                sub_recipes={
                    {
                        package={"xarchiver", Repo.AOR}
                    },
                }
            }
        }
    },

    screen={
        capture={
            {
                sub_recipes={
                    {
                        package={"hyprshot", Repo.AOR}
                    }
                }
            }
        },
        record={
            {
                sub_recipes={
                    {
                        package={"gpu-screen-recorder", Repo.AOR},
                        -- units={"gpu-screen-recorder.service", Scope.SINGLE_USER}
                    },
                    {
                        package={"gpu-screen-recorder-ui", Repo.AOR},
                        -- units={"gpu-screen-recorder-ui.service", Scope.SINGLE_USER}
                    }
                }
            },
        }
    },

    browser={
        gui={
            {
                sub_recipes={
                    {
                        package={"firefox", Repo.AOR},
                        single_user_config={"~/.config/firefox"}
                    },
                    {
                        package={"speech-dispatcher", Repo.AOR}
                    },
                    {
                        --TODO: this recipes need extension too, how to write
                        package={"python-pywalfox", Repo.AUR}
                    },
                }
            },
            {
                sub_recipes={
                    {
                        package={"zen-browser-bin", Repo.AUR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"brave-vin", Repo.AUR}
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"google-chrome-bin", Repo.AUR},
                        single_user_config={"~/.config/chrome-flags.conf"},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"helium-browser-bin", Repo.AUR},
                        single_user_config={"~/.config/helium-flags.conf"},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"thorium-browser-bin", Repo.AUR},
                        single_user_config={"~/.config/thorium-flags.conf"},
                    }
                }
            },
            {
                sub_recipes={
                    {
                        package={"microsoft-edge-stable-bin", Repo.AUR}
                    }
                }
            },
        }
    },

    misc={
        {
            sub_recipes={

                {
                    package={"anki", Repo.AOR}
                },
                {
                    package={"mediawriter", Repo.AOR}
                },
                {
                    package={"electron", Repo.AOR},
                    single_user_config={"~/.config/electron-flags.conf"},
                    env={
                        ELECTRON_OZONE_PLATFORM_HINT="auto"
                    }
                },
            }
        }
    }
}

return M
