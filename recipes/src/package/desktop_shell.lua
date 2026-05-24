local root={
    shell={
        framework={
            quickshell={repo=Repo.AUR},
        },
        product={
            ashell={repo=Repo.AUR},
            ewww={repo=Repo.AUR},
            ags={repo=Repo.AUR},
            noctalia_shell={repo=Repo.AUR},
            dms_shell_niri={
                repo=Repo.AOR,
                units={"dms.service", Scope.SINGLE_USER},
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
        swaylock={repo=Repo.AOR}
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
}

return {
    root.bar.waybar
}
