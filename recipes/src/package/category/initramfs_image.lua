return {
    mkinitcpio={
        repo=Repo.AOR,
        multi_user_config={
            "/etc/mkinitcpio.conf",
            "/etc/mkinitcpio.conf.d"
        }
    },
    dracut={repo=Repo.AOR},
    booster={repo=Repo.AOR},
}
