from box import Box
from src.catalog import db
from src.schema import Unit, PkgSpec, PkgVar, PkgRecipe, UsageRecipe


recipes=Box(
    boot_linux=UsageRecipe(
        recipes=[
            PkgRecipe(PkgVar(
                db.systemd,
                configs=[
                    "/boot/loader/loader.conf",
                    "/boot/loader/entries/linux.conf"
                ]
            )),
            PkgRecipe(
                PkgVar(db.linux),
                [
                    PkgVar(db.linux_headers),
                    PkgVar(db.linux_firmware)
                ],
            ),
            PkgRecipe(PkgVar(db.microcode)),
            PkgRecipe(PkgVar(db.mkinitcpio))
        ],
    ),
    boot_linux_cachyos_bore=UsageRecipe(
        recipes=[
            PkgRecipe(PkgVar(
                db.systemd,
                configs=[
                    "/boot/loader/loader.conf",
                    "/boot/loader/entries/linux-cachyos-bore.conf"
                ]
            )),
            PkgRecipe(
                PkgVar(db.linux_cachyos_bore),
                [
                    PkgVar(db.linux_cachyos_bore_headers),
                    PkgVar(db.linux_firmware)
                ],
            ),
            PkgRecipe(PkgVar(db.microcode)),
            PkgRecipe(PkgVar(db.mkinitcpio))
        ],
    ),

    efibootmgr=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.efibootmgr)),
        ]
    ),

    time=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.sudo)),
            PkgRecipe(PkgVar(db.glibc)),
            PkgRecipe(PkgVar(db.systemd, units=[db.systemd.units.systemd_timesyncd_service]))
        ],
        installation=[
            ["sudo", "timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"],
            ["sudo", "timedatectl", "set-ntp", "true"],
            ["sudo", "timedatectl", "set-local-rtc", "0"],
            ["timedatectl", "status"],
            ["hwclock", "--systohc"],
        ]
    ),

    locale=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.sudo)),
            PkgRecipe(PkgVar(db.glibc)),
            PkgRecipe(PkgVar(db.systemd)),
        ],
        installation=[
            ["sudo", "locale-gen", "en_US.UTF-8"],
            ["localectl", "set-locale", "LANG=en_US.UTF-8"]
        ]
    ),

    userland=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.base)),
            PkgRecipe(PkgVar(db.base_devel)),
        ],
    ),

    vcs=Box(
        pkgs=[
            PkgRecipe(
                PkgVar(db.git),
                [
                    PkgVar(db.less),
                    PkgVar(db.delta),
                ]
            ),
        ]
    ),

    system_package_manager= Box(
        pkgs=[
            PkgRecipe(PkgVar(db.git)),
            PkgRecipe(PkgVar(db.pacman)),
            PkgRecipe(
                PkgVar(db.yay),
                installation=[
                    ["cd", "~/.cache"],
                    ["rm", "-rf", "yay"],
                    ["git", "clone", "https://aur.archlinux.org/yay.git"],
                    ["cd", "yay"],
                    ["makepkg", "-si"]
                ]
            ),
            PkgRecipe(
                PkgVar(db.paru),
                installation=[
                    ["cd", "~/.cache"],
                    ["rm", "-rf", "paru"],
                    ["git", "clone", "https://aur.archlinux.org/paru.git"],
                    ["cd", "yay"],
                    ["makepkg", "-si"]
                ]
            ),
            PkgRecipe(PkgVar(db.reflector))
        ]
    ),

    graphic=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.mesa)),
            PkgRecipe(PkgVar(db.mesa_utils)),
            PkgRecipe(PkgVar(db.libva_utils)),
            PkgRecipe(PkgVar(db.vulkan_intel)),
            PkgRecipe(PkgVar(db.intel_media_diriver)),
            PkgRecipe(PkgVar(db.vulkan_radeon_driver)),
        ]
    ),

    audio=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.pipewire)),
            PkgRecipe(PkgVar(db.wireplumber)),
            PkgRecipe(PkgVar(db.pipewire_pulse)),
            PkgRecipe(PkgVar(db.pipewire_audio)),
            PkgRecipe(PkgVar(db.pipewire_alsa)),
        ]
    ),

    network=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.iwd)),
            PkgRecipe(PkgVar(db.networkmanager)),
            PkgRecipe(PkgVar(db.openssh, units=[db.openssh.units.sshd])),
        ]
    ),

    font=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.noto_fonts)),
            PkgRecipe(PkgVar(db.noto_fonts_cjk)),
            PkgRecipe(PkgVar(db.noto_fonts_emoji)),
            PkgRecipe(PkgVar(db.ttf_fira_code)),
            PkgRecipe(PkgVar(db.ttf_fira_code_nerd)),
            PkgRecipe(PkgVar(db.ttf_jetbrains_mono)),
            PkgRecipe(PkgVar(db.ttf_jetbrains_mono_nerd)),
        ]
    ),

    window_compositor=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.niri)),
            PkgRecipe(PkgVar(db.xwayland_satelite)),
            PkgRecipe(PkgVar(db.xdg_desktop_portal_gtk)),
            PkgRecipe(PkgVar(db.app2unit))
        ]
    ),

    input_method=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.fcitx5)),
            PkgRecipe(PkgVar(db.fcitx5_qt)),
            PkgRecipe(PkgVar(db.fcitx5_gtk)),
            PkgRecipe(PkgVar(db.fcitx5_unikey)),
            PkgRecipe(PkgVar(db.fcitx5_configtool)),
        ]
    ),

    shell_history=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.nushell)),
            PkgRecipe(PkgVar(db.atuin)),
        ],
        installtion=[
            {"mkdir", "~/.local/share/atuin/"},
            {"atuin", "init", "nu", "|", "save", "~/.local/share/atuin/init.nu"},
        ]
    ),

    shell_prompt=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.nushell)),
            PkgRecipe(PkgVar(db.starship)),
        ],
        installtion=[
            {"mkdir", "($nu.data-dir | path join \"vendor/autoload\")"},
            {"starship", "init", "nu", "|", "save", "-f", "($nu.data-dir | path join \"vendor/autoload/starship.nu\")"}
        ]
    ),

    terminal=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.foot)),
            PkgRecipe(PkgVar(db.tmux)),
        ]
    ),

    browser=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.firefox)),
            PkgRecipe(PkgVar(db.zen_browser_bin)),
            PkgRecipe(PkgVar(db.brave_bin)),
            PkgRecipe(PkgVar(db.helium_browser_bin)),
        ]
    ),

    launcher=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.fuzzel)),
        ]
    ),

    cxx=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.make)),
            PkgRecipe(PkgVar(db.gcc)),
            PkgRecipe(PkgVar(db.ccache)),
            PkgRecipe(PkgVar(db.mold)),
            PkgRecipe(PkgVar(db.gdb)),
        ]
    ),
    python=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.uv)),
        ]
    ),

    text_editor=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.nvim)),
            PkgRecipe(PkgVar(db.emacs_wayland)),
        ]
    ),

    monitor=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.btop)),
        ]
    ),

    disk=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.udisks2)),
            PkgRecipe(PkgVar(db.udiskie)),

            PkgRecipe(PkgVar(db.e2fsprogs)),
            PkgRecipe(PkgVar(db.exfatprogs)),
            PkgRecipe(PkgVar(db.ntfsprogs)),

            PkgRecipe(PkgVar(db.gvfs)),
            PkgRecipe(PkgVar(db.gvfs_mtp)),
        ]
    ),

    power_n_performance=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.tlp)),
            PkgRecipe(PkgVar(db.tlp_rdw)),
            PkgRecipe(PkgVar(db.batsignal)),
            PkgRecipe(PkgVar(db.thermal)),
            PkgRecipe(PkgVar(db.irqbalance)),

        ]
    ),

    thumbnail=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.tumbler)),
            PkgRecipe(PkgVar(db.ffmpegthumbnailer)),
            PkgRecipe(PkgVar(db.freetype2)),
            PkgRecipe(PkgVar(db.libgepub)),
            PkgRecipe(PkgVar(db.libgsf)),
            PkgRecipe(PkgVar(db.libopenraw)),
            PkgRecipe(PkgVar(db.poppler_glib)),
        ]
    ),

    video_player=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.mpv)),
        ]
    ),

    image_viewer=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.mpv)),
            PkgRecipe(PkgVar(db.ueberzugpp)),
        ]
    ),

    office=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.libreoffice_fresh)),
            PkgRecipe(PkgVar(db.libreoffice_fresh_vi)),
            PkgRecipe(PkgVar(db.libreoffice_fresh_en_gb)),
        ]
    ),

    pdf_viewer=Box(
        pkgs=[
            PkgRecipe(
                PkgVar(db.zathura),
                [
                    PkgVar(db.zathura_pdf_mupdf),
                ]
            ),
        ]
    ),

    archive=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.xarchive)),
            PkgRecipe(PkgVar(db.seven_zip)),
            PkgRecipe(PkgVar(db.unzip)),
            PkgRecipe(PkgVar(db.zip)),
            PkgRecipe(PkgVar(db.unrar)),
            PkgRecipe(PkgVar(db.libarchive)),
        ]
    ),

    thunar=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.thunar)),
            PkgRecipe(PkgVar(db.thunar_volman)),
            PkgRecipe(PkgVar(db.thunar_archive_plugin)),
        ]
    ),

    # TODO: This package dependency is a lot
    yazi=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.yazi)),
            PkgRecipe(PkgVar(db.seven_zip)),
            PkgRecipe(PkgVar(db.chafa)),
            PkgRecipe(PkgVar(db.jq)),
            PkgRecipe(PkgVar(db.poppler)),
            PkgRecipe(PkgVar(db.resvg)),
            PkgRecipe(PkgVar(db.imagemagick)),
        ]
    ),

    qt6_wayland=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.qt6_wayland)),

        ]
    ),

    clipboard=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.wl_clipboard)),
            PkgRecipe(PkgVar(db.wl_clipboard_persist)),
            PkgRecipe(PkgVar(db.cliphist)),
        ]
    )
)












