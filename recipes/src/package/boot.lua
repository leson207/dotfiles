local root={
    loader={
        grub={repo=Repo.AOR},
        limine={repo=Repo.AOR},
        refind={repo=Repo.AOR},
        systemd={
            repo=Repo.AOR,
            multi_user_config={"/boot/loader/entries"}
        },
    },

    microcode={
        intel_ucode={repo=Repo.AOR}
    },

    initramfs_image={
        mkinitcpio={
            repo=Repo.AOR,
            multi_user_config={
                "/etc/mkinitcpio.conf",
                "/etc/mkinitcpio.conf.d"
            }
        },
        dracut={repo=Repo.AOR},
        booster={repo=Repo.AOR},
    },

    manager={
        efibootmgr={repo=Repo.AOR}
    },
}

return {
    root.loader.systemd,
    root.ucode.intel_ucode,
    root.initramfs_image.mkinitcpio,
    root.manager.efibootmgr,
}
