local root={
    python={
        uv={repo=Repo.AOR}
    },

    rust={
        rustup={repo=Repo.AOR}
    },

    go={
        go={repo=Repo.AOR}
    }
}

return {
    root.python.uv,
    root.rust.rustup,
    root.rust.go
}
