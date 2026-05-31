return {
    grub={repo=Repo.AOR},
    limine={repo=Repo.AOR},
    refind={repo=Repo.AOR},
    systemd={
        repo=Repo.AOR,
        multi_user_config={"/boot/loader/entries"}
    },
}
