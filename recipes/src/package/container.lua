local root={
    podman={
        podman={repo=Repo.AOR, single_user_config={"~/.config/containers"}},
        podman_compose={repo=Repo.AOR},
        podman_tui={repo=Repo.AUR},
        podman_desktop={repo=Repo.AOR},
    }
}

return {
    root.podman.podman,
    root.podman.podman_compose,
    root.podman.podman_tui,
    root.podman.podman_desktop,
}
