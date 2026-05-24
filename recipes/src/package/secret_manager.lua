local root={
    keyring={
        gnome_keyring={repo=Repo.AOR, units={"gnome-keyring-daemon.service", scope=Scope.SINGLE_USER}}
    },

    manager={
        seahorse={repo=Repo.AOR},
        bitwardern={repo=Repo.AOR},
    }
}

return {
    root.keyring.gnome_keyring,
    root.manager.bitwardern
}
