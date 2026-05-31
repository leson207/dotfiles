return {
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
    niri={repo=Repo.AOR},
    river={repo=Repo.AOR},
    mangowm={repo=Repo.AUR},
}

