local root={
    kernel={
        linux={repo=Repo.AOR},
        linux_zen={repo=Repo.AOR},
        linux_cachyos={repo=Repo.AOR},
        linux_cachyos_bore={repo=Repo.AOR},
    },
    header={
        linux_headers={repo=Repo.AOR},
        linux_zen_headers={repo=Repo.AOR},
        linux_cachyos_headers={repo=Repo.AOR},
        linux_cachyos_bore_headers={repo=Repo.AOR},
    },
}

local vendor={
    vanilla={
        root.kernel.linux,
        root.header.linux_headers
    },
    zen={
        root.kernel.linux_zen,
        root.header.linux_zen_headers
    },
    cachyos={
        root.kernel.linux_cachyos,
        root.header.linux_cachyos_headers
    },
    cachyos_bore={
        root.kernel.linux_cachyos_bore,
        root.header.linux_cachyos_bore_headers
    },
}

return {
    root.kernel.linux,
    root.header.linux_headers,

    root.kernel.linux_zen,
    root.header.linux_zen_headers,

    root.kernel.linux_cachyos_bore,
    root.header.linux_cachyos_bore_headers
}
