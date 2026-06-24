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
    system={
        nm_applet={repo=Repo.AOR},
        blueman={repo=Repo.AOR}
    },
    shell={
        product={
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

    brightness_control={
        brightnessctl={repo=Repo.AOR},
        ddcutil={repo=Repo.AOR}
    },

    audio_control={
        pavu_control={repo=Repo.AOR},
        pamixer={repo=Repo.AOR}
    },

}
