return {
    gen={
        glibc={
            repo=Repo.AOR,
            installation={
                {"sudo", "locale-gen", "en_US.UTF-8"}
            },
        }
    },

    set={
        systemd={
            repo=Repo.AOR,
            installation={
                {"localectl", "set-locale", "LANG=en_US.UTF-8"}
            }
        }
    }
}


