return {
    dbus={
        repo=Repo.AOR,
        auto_start={
            {"dbus-update-activation-environment", "--systemd", "WAYLAND_DISPLAY", "XDG_CURRENT_DESKTOP"}
        }
    }
}
