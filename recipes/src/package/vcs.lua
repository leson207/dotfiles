local root={
    backend={
        git={
            git={repo=Repo.AOR, single_user_config={"~/.gitconfig"}},
            less={repo=Repo.AOR},
            git_delta={repo=Repo.AOR},
        },
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

local picked={
    root.backend.git.git,
    root.backend.git.less,
    root.backend.git.git_delta,
}

return picked
