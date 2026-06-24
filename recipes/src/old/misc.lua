return {
    xgd_user_dirs={repo=Repo.AOR, units={"xdg-user-dirs.service", Scope.SINGLE_USER}},
    xdg_utils={repo=Repo.AOR},
    krokiet_bin={repo=Repo.AOR},
    anki={repo=Repo.AOR},
    mediawriter={repo=Repo.AOR},
    electron={
        repo=Repo.AOR,
        single_user_config={"~/.config/electron-flags.conf"},
        env={ELECTRON_OZONE_PLATFORM_HINT="auto"}
    },

    tree={repo=Repo.AOR},

    aspell={repo=Repo.AOR},
    aspell_en={repo=Repo.AOR},
    doom_emacs={},
}

