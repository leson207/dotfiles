return {
    backend={
        git={repo=Repo.AOR, single_user_config={"~/.gitconfig"}},
        jujutsu={repo=Repo.AOR},
        mercurial={repo=Repo.AOR},
        darcs={repo=Repo.AOR},
    },

    service={
        gitea={repo=Repo.AOR},
        gitlab={repo=Repo.AOR},
        forgejo={repo=Repo.AOR},
    }
}
