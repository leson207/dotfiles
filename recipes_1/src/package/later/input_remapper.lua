local root={
    mapper={
        kanata_bin={
            repo=Repo.AOR,
            multiple_user_config={
                "/etc/udev/rules.d/99-uinput.rules",
                -- KERNEL=="uinput", MODE="0660", GROUP="uinput", OPTIONS+="static_node=uinput"
                {"sudo", "udevadm", "control", "--reload"},
                {"sudo", "udevadm", "trigger", "--verbose", "--sysname-match=uinput"},
                {"sudo", "modprobe", "-r", "uinput"},
                {"sudo", "modprobe", "uinput"}
            },
            -- sudo groupadd uinput
            -- sudo usermod -aG input $USER
            -- sudo usermod -aG uinput $USER
            groups={
                "input",
                "uinput",
            },
            reference={
                "https://shom.dev/start/using-kanata-to-remap-any-keyboard/"
            }
        },

        keyd={repo=Repo.AOR},
        kmonad={repo=Repo.AOR},
        input_remapper_bin={repo=Repo.AUR},
        xremap_hypr_bin={repo=Repo.AUR},
        xremap_niri_bin={repo=Repo.AUR},
        xremap_wlroots_bin={repo=Repo.AUR},
    },

    manager={
        wlr_which_key={repo=Repo.AUR}
    }
}

local picked={
    root.mapper.kanata_bin
}

return picked

