local root={
    gen={
        glibc={
            repo=Repo.AOR,
            multi_user_config={
                "/etc/locale.gen",
                {"locale-gen"}
            },
        }
    },

    set={
        systemd={
            repo=Repo.AOR,
            multi_user_config={"/etc/locale.conf"},
            installation={
                {"localectl", "set-locale", "LANG=en_US.UTF-8"}
            }
        }
    }
}

return {
    root.gen.glibc,
    root.set.systemd
}

