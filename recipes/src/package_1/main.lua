local db=require("recipes_1.src.catalog")

-----------------------------------------------------------
local assumption={
    pkgs={
        {db.glibc},
        {db.pacman},
        {db.systemd},
    }
}

-----------------------------------------------------------

local recipes={
    authenticator={
        pkgs={
            { db.sudo }
        }
    },

    init_system={
        pkgs={
            {db.systemd}
        }
    },

    boot={
        pkgs={
            {db.systemd},
            {db.linux},
            {db.linux_cachyos_bore},
            {db.linux_headers},
            {db.linux_cachyos_bore_headers},
        },
        configs={
            "/boot/loader/entries",
            "/boot/loader/loader.conf",
        }
    },

    boot_manager={
        pkgs={
            {db.efibootmgr}
        }
    },

    system_package_manager={
        pacman={
            pkgs={
                {db.pacman}
            }
        },
        yay={
            pkgs={
                {db.pacman},
                {db.git},
            },
            installation={
                "cd ~/.cache",
                "git clone https://aur.archlinux.org/yay.git",
                "cd yay",
                "makepkg -si"
            }
        },
        paru={
            pkgs={
                {db.pacman},
                {db.git},
            },
            installation={
                "cd ~/.cache",
                "git clone https://aur.archlinux.org/paru.git",
                "cd yay",
                "makepkg -si"
            }
        },
    },

    mirror_filter={
            -- TODO: This is python
        pkgs={
            {db.reflector}
        }
    },

    time={
        pkgs={
            { pkg=db.glibc },
            {
                pkg=db.systemd,
                unit={db.systemd.units.systemd_timesyncd_service}
            }
        },
        installation={
            {"sudo", "timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"},
            {"sudo", "timedatectl", "set-ntp", "true"},
            {"sudo", "timedatectl", "set-local-rtc", "0"},
            {"timedatectl", "status"},
            {"hwclock", "--systohc"},
        }
    },

    locale={
        pkgs={
            { pkg=db.glibc },
            { pkg=db.systemd, }
        },
        installation={
            {"sudo", "locale-gen", "en_US.UTF-8"},
            {"localectl", "set-locale", "LANG=en_US.UTF-8"}
        }
    }
}



print("Hello world!")
