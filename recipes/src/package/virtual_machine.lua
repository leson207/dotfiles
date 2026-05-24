local root={
        qemu_desktop={repo=Repo.AOR},
        dnsmasq={repo=Repo.AOR},
        virt_manager={repo=Repo.AOR},
        virt_viewer={repo=Repo.AOR},
        libvirt={repo=Repo.AOR, units={"libvirtd.service", scope=Scope.MULTI_USER}}
}

return {
    root.qemu_desktop,
    root.libvirt,
    root.dnsmasq,
    root.virt_manager,
    root.virt_viewer
}
