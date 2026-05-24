local root={
    tui={
        vim={repo=Repo.AOR},
        neovim={
            neovim={repo=Repo.AOR},
            luarocks={repo=Repo.AOR}
        },
        helix={repo=Repo.AOR},
        kakoune={repo=Repo.AOR},
        emacs={repo=Repo.AOR},
    },
    gui={
        zed={repo=Repo.AOR},
        code={repo=Repo.AOR},
        typst={repo=Repo.AOR},
        emacs={repo=Repo.AOR},
    },
}

return {
    root.tui.neovim,
    root.gui.zed
}
