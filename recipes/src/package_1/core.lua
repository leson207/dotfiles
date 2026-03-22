dofile("utils.lua")

local m={}

------------------------------------------------------------------------
m.locale={
    systemd={
        Repo.AOR,
        multi_user_config={"/etc/locale.conf"},
    },
    glibc={
        Repo.AOR,
        multi_user_config={
            "/etc/locale.gen",
            {"locale-gen"}
        }
    }
}

m.time.systemd={
    Repo.AOR,
    units={"systemd-timesyncd", Scope.MULTI_USER},
    multi_user_config={
        {"sudo", "timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"},
        {"sudo", "timedatectl", "set-ntp", "true"},
        {"sudo", "timedatectl", "set-local-rtc", "0"},
        {"timedatectl", "status"},
        {"hwclock", "--systohc"},
    }
}

m.init_system.systemd={
    Repo.AOR,
    multi_user_config={
        "/etc/hostname",
        "/etc/vconsole.conf",
        -- "/etc/systemd/journald.conf"
        -- #MaxRetentionSec=7day
    },
    single_user_config={"~/.config/systemd"},
}

-------------------------------------------------------------

m.boot.loader.systemd={
    Repo.AOR,
    multi_user_config={
        "/boot/loader/entries/linux.conf",
        "/boot/loader/entries/linux-zen.conf",
    },
    supporters={
        kernel={
            linux={Repo.AOR, supporters={linux_headers=aor}},
            linux_zen={Repo.AOR, supporters={linux_zen_headers=aor}}
        },
        microcode={intel_ucode=aor}
    }
}
m.boot.manager.efibootmgr=aor

m.privilege.sudo={
    Repo.AOR,
    multi_user_config={"/etc/sudoers"}
}

m.firmware.linux_firmware=aor
m.display_server_protocol.wayland=aor

m.base.rel=Relationship.ASSOCIATED
m.base.base=aor
m.base.base_devel=aor

m.graphic.opengl.rel=Relationship.ASSOCIATED
m.graphic.opengl.mesa={Repo.AOR, supporters={mesa_utils=aor}}

m.graphic.rel=Relationship.ASSOCIATED
m.graphic.vulkan.vulkan_intel=aor
m.graphic.vulkan.vulkan_radeon=aor
m.graphic.vulkan.vulkan_mesa_implicit_layers=aor

m.graphic.video.rel=Relationship.ASSOCIATED
m.graphic.vaapi.libva={Repo.AOR, supporters={libva_utils=aor}}
m.graphic.vaapi.libva_intel_driver=aor
m.graphic.vaapi.intel_media_driver=aor

m.disk.driver.ntfs_3g=aor
m.disk.mount.udisks2={
    Repo.AOR,
    units={name="udisks2.service", scope=Scope.MULTI_USER},
    supporters={udiskie=aor}
}

m.disk.virtual_file_system.gvfs={
    Repo.AOR,
    supporters={
        gvfs_mtp=aor,
        -- gvfs_smb=aor
    }
}

m.disk.strim.util_linux={Repo.AOR, units={"fstrim.service", Scope.MULTI_USER}}

m.audio.processor.pipewire={
    Repo.AOR,
    units={"pipewire.service", scope=Scope.SINGLE_USER},
    supporter={
        wireplumber={Repo.AOR, units={"wireplumber.service", Scope.SINGLE_USER}},
        pipewire_pulse={Repo.AOR, units={"pipewire-pulse.service", Scope.SINGLE_USER}},
        pipewire_audio=aor,
        pipewire_alsa=aor,
    }
}

m.network.internet.networkmanager={
    Repo.AOR,
    units={"NetworkManager.service", Scope.MULTI_USER},
    supporters={
        iwd={Repo.AOR, units={"iwd.service", Scope.MULTI_USER}},
        dnsmasq={Repo.AOR, units={"dnsmasq.service", Scope.MULTI_USER}},
    }
}

m.network.ssh.openssh={Repo.AOR, units={"sshd.service", Scope.MULTI_USER}}

m.power_and_performance={
    -- ananicy_cpp={Repo.AOR, units={"ananicy-cpp.service", Scope.MULTI_USER}},
    tlp={
        Repo.AOR,
        units={"tlp.service", Scope.MULTI_USER},
        multi_user_config={
            "/etc/tlp.conf"
            -- CPU_ENERGY_PERF_POLICY_ON_BAT=power
        },
        supporters={
            tlp_rdw=aor,
            tlp_pd={Repo.AOR, units={"tlp-pd.service", Scope.MULTI_USER}},
        }
    },
    -- tunned_ppd={
    --     Repo.AOR,
    --     units={"tunned-ppd.service", Scope.MULTI_USER},
    --     supporters={tuned={Repo.AOR, units={"tuned.service", Scope.MULTI_USER}}}
    -- },
    -- power_profiles_daemon={Repo.AOR},
    -- auto_cpufreq={Repo.AOR, units={"auto-cpufreq.service", Scope.MULTI_USER}},
    cpupower={Repo.AOR, units={"cpupower.service", Scope.MULTI_USER}},
    preload={Repo.AOR, units={"preload.service", Scope.MULTI_USER}},
    thermald={Repo.AOR, units={"thermald.service", Scope.MULTI_USER}},
    irqbalance={Repo.AOR, units={"irqbalance.service", Scope.MULTI_USER}},
    batsignal={Repo.AOR, units={"batsignal.service", Scope.MULTI_USER}},
}

m.package_manager={
    guix=aur,
    nix=aor,
    pacman={Repo.AOR, multi_user_config={"/etc/pacman.conf"}},
}
