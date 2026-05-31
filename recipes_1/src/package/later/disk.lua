local root={
    udisks2={repo=Repo.AOR, units={name="udisks2.service", scope=Scope.MULTI_USER}},

    e2fsprogs={repo=Repo.AOR},
    exfatprogs={repo=Repo.AOR},
    ntfs_3g={repo=Repo.AOR},

    udiskie={repo=Repo.AOR, auto_start={{"udiskie", "&"}}},
    gvfs={repo=Repo.AOR},
    gvfs_mtp={repo=Repo.AOR},
    gvfs_smb={repo=Repo.AOR},

    util_linux={repo=Repo.AOR, units={"fstrim.timer", Scope.MULTI_USER}},
    sshfs={repo=Repo.AOR}
}

return {
    root.udisks2,

    root.e2fsprogs,
    root.exfatprogs,
    root.ntfs_3g,

    root.udiskie,
    root.gvfs,
    root.gvfs_mtp,

    root.util_linux
}
