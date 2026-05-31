return {
    login_manager={
        greetd={
            repo=Repo.AOR,
            units={"greetd", Scope.MULTI_USER}
        },
        sddm={
            repo=Repo.AOR,
            units={"sddm", Scope.MULTI_USER},
            multi_user_config={
                "/etc/sddm.conf",
                "/etc/sddm.conf.d"
            }
        },
    },
    greeter={
        cosmic_greeter={repo=Repo.AOR},
        greetd_regreet={repo=Repo.AOR},
        greetd_agreety={repo=Repo.AOR},
        greetd_gtkgreet={repo=Repo.AOR},
        greetd_tuigreet={repo=Repo.AOR},

        greetd_qtgreet={repo=Repo.AUR},
        greetd_syscgreet={repo=Repo.AUR},
    },
    sddm_astronaut_theme={repo=Repo.AUR}
}
