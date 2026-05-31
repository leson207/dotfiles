local root={
    misc={
        evolution_data_server={repo=Repo.AOR},
        upower={repo=Repo.AOR},
        bluez={repo=Repo.AOR}
        -- https://github.com/end-4/dots-hyprland/blob/main/sdata/deps-info.md
        -- https://github.com/caelestia-dots/shell#manual-installation
        -- https://docs.noctalia.dev/v4/getting-started/installation/#manual-install
        -- https://danklinux.com/docs/dankmaterialshell/installation/
        -- https://github.com/Darkkal44/qylock#-dependencies
        -- https://axeni.de/ax-shell/
        -- https://github.com/snowarch/iNiR/wiki/INSTALL#the-hard-way-manual
        -- github tag: dotifles, quickshell, ricing, unixporn, niri, hyprland, desktop-shell, wayland
    },
    aesthetic={

    },
    dock={

    },
    system={
        nm_applet={repo=Repo.AOR},
        blueman={repo=Repo.AOR}
    },
    shell={
        framework={
            quickshell={repo=Repo.AUR},
        },
        product={
            ashell={repo=Repo.AUR},
            ewww={repo=Repo.AUR},
            ags={repo=Repo.AUR},
            noctalia_shell={repo=Repo.AUR},
            dms={
                dms_shell_niri={
                    repo=Repo.AOR,
                    units={"dms.service", Scope.SINGLE_USER},
                },
                kimageformats={repo=Repo.AOR},
                cava={repo=Repo.AOR},
                dgop={repo=Repo.AOR},
                dsearch_bin={
                    repo=Repo.AUR,
                    units={"dsearch.service", Scope.SINGLE_USER},
                },
                matugen={repo=Repo.AUR},
                qt6_multimedia={repo=Repo.AUR},
                papirus_icon_theme={
                    repo=Repo.AOR,
                    env={
                        "QS_ICON_THEME=Papirus"
                    }
                }
            }
        }
    },

    bar={
        waybar={
            repo=Repo.AOR,
            units={"waybar.service", Scope.SINGLE_USER},
            single_user_config={"~/.config/waybar"}
        },
        hyprpanel={repo=Repo.AUR},
    },

    polkit_agent={
        hyprpolkitagent={
            repo=Repo.AOR,
            units={"hyprpolkitagent.service", Scope.SINGLE_USER},
        },
        polkit={repo=Repo.AOR}
    },

    backlight={
        hyprsunset={
            repo=Repo.AOR,
            units={"hyprsunset.service", Scope.SINGLE_USER},
            single_user_config={"~/.config/hypr/hyprsunset.conf"}
        },
        wlsunset={repo=Repo.AOR},
        gammastep={repo=Repo.AOR},
    },

    screen_lock={
        hyprlock={
            repo=Repo.AOR,
            single_user_config={"~/.config/hypr/hyprlock.conf"}
        },
        swaylock={repo=Repo.AOR},
        gtklock={repo=Repo.AOR},
    },

    idle_management={
        hypridle={
            repo=Repo.AOR,
            units={"hypridle.service", Scope.SINGLE_USER},
            single_user_config={"~/.config/hypr/hypridle.conf"}
        },
        swayidle={
            repo=Repo.AOR,
            units={"hypridle.service", Scope.SINGLE_USER},
            single_user_config={"~/.config/systemd/user/swayidle.service"}
        }
    },

    notificaton={
        mako={
            repo=Repo.AOR,
            units={"mako.service", Scope.SINGLE_USER},
            single_user_config={"~/.config/dunst"}
        },
        swaync={
            repo=Repo.AOR,
            units={"swaync.service", Scope.SINGLE_USER},
            single_user_config={"~/.config/swaync"},
        },
        dunst={repo=Repo.AOR, single_user_config={"~/.config/dunst"}},
        fnott={repo=Repo.AOR},
    },

    osd={
        swayosd={
            repo=Repo.AOR,
            units={"swayosd-libinput-backend.service", Scope.SINGLE_USER},
            auto_start={{"swayosd-server"}}
        }
    },

    brightness_control={
        brightnessctl={repo=Repo.AOR},
        ddcutil={repo=Repo.AOR}
    },

    audio_control={
        pavu_control={repo=Repo.AOR},
        pamixer={repo=Repo.AOR}
    },

    wallpaper={
        setter={
            awww={
                repo=Repo.AOR,
                single_user_config={
                    "~/.config/systemd/user/awww.service"
                },
                auto_start={{"awww-daemon"}}
            },
            swaybg={repo=Repo.AOR},
            mpvpaper={repo=Repo.AUR},
            wpaperd={repo=Repo.AOR},
            hyprpaper={
                repo=Repo.AOR,
                units={"hyprpaper.service", Scope.SINGLE_USER},
                single_user_config={"~/.config/hypr/hyprpaper.conf"}
            }
        },

        picker={
            waypaper={repo=Repo.AUR},
            wallrizz={repo=Repo.GITHUB},
            waytrogen_bin={repo=Repo.AUR},
            rofi={
                repo=Repo.AOR,
                single_user_config={"~/.config/rofi"},
            }
        },

        color_extractor={
            wallust={repo=Repo.AUR},
            hellwal={repo=Repo.AUR},
            python_pywall={repo=Repo.AOR},
            kde_material_you_colors={repo=Repo.AUR},
            matugen={
                repo=Repo.AOR,
                single_user_config={"~/.config/matugen"},
            }
        },
    },

    display_manager={
        greetd={repo=Repo.AOR},
        gdm={repo=Repo.AOR},
        lightdm={repo=Repo.AOR},
        sddm={
            sddm={
                repo=Repo.AOR,
                units={"sddm.service", Scope.MULTI_USER},
                multiple_user_config={
                    "/etc/sddm.conf",
                    "/etc/sddm.conf.d/virtualkbd.conf",
                }
            },
            qt6_svg={repo=Repo.AOR},
            qt6_wayland={repo=Repo.AOR},
            qt6_virtualkeyboard={repo=Repo.AOR},
            qt6_multimedia_ffmpeg={repo=Repo.AOR},

            installation={
                {"sudo", "git", "clone", "-b", "master", "--depth", "1", "https://github.com/keyitdev/sddm-astronaut-theme.git", "/usr/share/sddm/themes/sddm-astronaut-theme"},
                {"sudo", "cp", "-r", "/usr/share/sddm/themes/sddm-astronaut-theme/Fonts/*", "/usr/share/fonts/"},
                "/usr/share/sddm/themes/sddm-astronaut-theme/metadata.desktop"
            }
        }
    },

    clipboard={
        copy_paste={
            wl_clipboard={repo=Repo.AOR}
        },

        persist={
            wl_clip_persist={
                repo=Repo.AOR,
                auto_start={{"wl-clip-persist", "--clipboard regular"}}
            },
        },

        history={
            cliphist={
                repo=Repo.AOR,
                units={"cliphist.service", Scope.SINGLE_USER},
                auto_start={
                    {"wl-paste", "--type", "text", "watch", "cliphist", "store"},
                    {"wl-paste", "--type", "image", "watch", "cliphist", "store"},
                },
            },
            copyq={repo=Repo.AOR},
            nwg_clipman={repo=Repo.AOR},
        },
    }
}

return {
    root.bar.waybar
}
