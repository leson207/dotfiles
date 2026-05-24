local root={
    c_library={
        glibc={repo=Repo.AOR}
    },

    firmware={
        linux_firmware={repo=Repo.AOR},
    },

    display_server_protocol={
        wayland={repo=Repo.AOR},
    },

    init_system={
        systemd={
            repo=Repo.AOR,
            single_user_config={"~/.config/systemd"},
        }
    },

    message_bus={
        dbus={
            repo=Repo.AOR,
            auto_start={
                {"dbus-update-activation-environment", "--systemd", "WAYLAND_DISPLAY", "XDG_CURRENT_DESKTOP"}
            }
        }
    },

    xgd_user_dirs={repo=Repo.AOR, units={"xdg-user-dirs.service", Scope.SINGLE_USER}},
    xdg_utils={repo=Repo.AOR},
    krokiet_bin={repo=Repo.AOR},
    anki={repo=Repo.AOR},
    mediawriter={repo=Repo.AOR},
    electron={
        repo=Repo.AOR,
        single_user_config={"~/.config/electron-flags.conf"},
        env={ELECTRON_OZONE_PLATFORM_HINT="auto"}
    },

    tree={repo=Repo.AOR},
    fastfetch={repo=Repo.AOR},
    fd={repo=Repo.AOR},
    fzf={repo=Repo.AOR},
    ripgrep={repo=Repo.AOR},
    bat={repo=Repo.AOR},
    eza={repo=Repo.AOR},
    zoxide={repo=Repo.AOR},

    xorg_xlsclients={repo=Repo.AOR},
    xorg_xrdb={repo=Repo.AOR},
    xorg_xeyes={repo=Repo.AOR},
    xorg_xclock={repo=Repo.AOR},
}

local env={
    XCURSOR_SIZE=24,
    _JAVA_AWT_WM_NONREPARENTING=1,

    QT_QPA_PLATFORM="wayland;xcb",
    QT_ENABLE_HIGHDPI_SCALING=1,
    QT_AUTO_SCREEN_SCALE_FACTOR=1,
    QT_WAYLAND_DISABLE_WINDOWDECORATION=1,

    GDK_SCALE=1,
    GDK_DPI_SCALE=1,
    GDK_BACKEND="wayland,x11",

    SDL_VIDEODRIVER="wayland",
    CLUTTER_BACKEND="wayland",
}

return {
    root.c_library.glibc,
}
