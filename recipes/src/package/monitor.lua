local root={
    atop={repo=Repo.AOR},
    btop={
        repo=Repo.AOR,
        single_user_config={".config/btop"}
    },
    htop={repo=Repo.AOR},
    nvtop={repo=Repo.AOR},
    glances={repo=Repo.AOR},
    bottom={repo=Repo.AOR},
    hyperfind={repo=Repo.AOR},
}

return {
    root.btop
}
