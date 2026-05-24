local root={
    nix={repo=Repo.AOR},
    guix={repo=Repo.AOR},
    pacman={
        pacman={repo=Repo.AOR, multi_user_config={"/etc/pacman.conf"}},
        reflector={repo=Repo.AOR, units={"reflector.timer", Scope.MULTI_USER}}
    }
}

return {
    root.pacman
}
