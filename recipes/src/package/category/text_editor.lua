return {
    tui={
        vim={repo=Repo.AOR},
        neovim={
            repo=Repo.AOR,
            single_user_config={
                "~/.config/nvim",
                "~/.config/lazyvim"
            }
        },
        helix={repo=Repo.AOR, single_user_config={"~/.config/helix"}},
        kakoune={repo=Repo.AOR},
    },

    gui={
        zed={repo=Repo.AOR},
        code={repo=Repo.AOR},
        typst={repo=Repo.AOR},
        emacs={
            emacs={repo=Repo.AOR},
            emacs_nox={repo=Repo.AOR},
            emacs_wayland={
                repo=Repo.AOR,
                auto_start={{"emacs", "--daemon"}},
                service={"emacs.service", Scope.SINGLE_USER}
            },
        },
    },
}

