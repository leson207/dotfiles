return {
    keyring={
        gnome_keyring={repo=Repo.AOR, units={"gnome-keyring-daemon.service", scope=Scope.SINGLE_USER}}
    },

    manager={
        seahorse={repo=Repo.AOR},
        bitwardern={repo=Repo.AOR},
    }
}

