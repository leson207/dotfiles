local root={
    hyprland={
        repo=Repo.AOR,
        single_user_config={
            "~/.config/hypr/hyprland",
            "~/.config/hypr/hyprland.conf",
            "~/.config/uwsm/env-hyprland",
        },
        installation={
            {"sh", "~/.config/hypr/hyprland/scripts/first_amd_gpu.sh"},
            {"sh", "~/.config/hypr/hyprland/scripts/first_intel_gpu.sh"},
        },
        env={
            HYPRCURSOR_SIZE="32",
            AQ_DRM_DEVICES="/dev/dri/first-intel-gpu:/dev/dri/first-amd-gpu"
        }
    },
    niri={
        niri={repo=Repo.AOR},
        xwayland_satellite={repo=Repo.AOR},
        xdg_desktop_portal_gtk={repo=Repo.AOR},
        xdg_desktop_portal_gnome={repo=Repo.AOR},
    },
    river={repo=Repo.AOR},
    mangowm={repo=Repo.AUR},
}

local screen_share={
    xdg_desktop_portal_gtk={repo=Repo.AOR},
    xdg_desktop_portal_hyprland={
        repo=Repo.AOR,
        env={
            -- XDG_CURRENT_DESKTOP="Hyprland",
            -- XDG_SESSION_TYPE="wayland"
        }
    },
    grim={repo=Repo.AOR},
    slurp={repo=Repo.AOR},
}

return {
    root.hyprland,
    screen_share.xdg_desktop_portal_gtk,
    screen_share.xdg_desktop_portal_hyprland
}
