from box import Box
from src.v2.schema import PkgVar, PkgRecipe
from src.v2.catalog import db, db2, db3


base=Box(
    boot_linux=Box(
        recipes=[
            PkgRecipe(
            PkgVar(
                db.systemd,
                    configs=[
                        "/boot/loader/loader.conf",
                        "/boot/loader/entries/linux.conf"
                    ]
                ),
            ),
            PkgRecipe(
                PkgVar(db.linux),
                [
                    PkgRecipe(PkgVar(db.linux_headers)),
                    PkgRecipe(PkgVar(db.linux_firmware))
                ],
            ),
            PkgRecipe(PkgVar(db.intel_ucode)),
        ],
    ),

    boot_linux_cahcyos_bore=Box(
        recipes=[
            PkgRecipe(
            PkgVar(
                db.systemd,
                    configs=[
                        "/boot/loader/loader.conf",
                        "/boot/loader/entries/linux-cachyos-bore.conf"
                    ]
                ),
            ),
            PkgRecipe(
                PkgVar(db.linux_cachyos_bore),
                [
                    PkgRecipe(PkgVar(db.linux_cachyos_bore_headers)),
                    PkgRecipe(PkgVar(db.linux_firmware))
                ],
            ),
            PkgRecipe(PkgVar(db.intel_ucode)),
        ],
    ),

    authenticator=Box(
        recipes=[
            PkgRecipe(PkgVar(db.sudo))
        ]
    ),

    time=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.sudo)),
            PkgRecipe(PkgVar(db.glibc)),
            PkgRecipe(PkgVar(db.systemd, units=[db.systemd.units.systemd_timesyncd_service]))
        ],
        installation=[
            ["timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"],
            ["sudo", "timedatectl", "set-ntp", "true"],
            ["timedatectl", "set-local-rtc", "0"],
            ["timedatectl", "status"],
            ["sudo", "hwclock", "--systohc"],
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

    sdk=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.base_devel)),
            PkgRecipe(PkgVar(db.make)),
            PkgRecipe(PkgVar(db.ninja)),
            PkgRecipe(PkgVar(db.gcc)),
            PkgRecipe(PkgVar(db.ccache)),
            PkgRecipe(PkgVar(db.mold)),
            PkgRecipe(PkgVar(db.gdb)),

            PkgRecipe(PkgVar(db.uv)),

            PkgRecipe(
                PkgVar(db.git),
                [
                    PkgRecipe(PkgVar(db.less)),
                    PkgRecipe(PkgVar(db.git_delta)),
                ]
            ),
        ]
    ),

    arch_official_repo=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.pacman)),
            PkgRecipe(PkgVar(db.reflector)),
        ]
    ),

    yay=Box(
        pkgs=[
            PkgVar(db.yay),
            PkgRecipe(PkgVar(db.git)),
            PkgRecipe(PkgVar(db.pacman)),
        ],
        installation=[
            ["cd", "~/.cache"],
            ["rm", "-rf", "yay"],
            ["git", "clone", "https://aur.archlinux.org/yay.git"],
            ["cd", "yay"],
            ["makepkg", "-si"]
        ]
    ),

    paru=Box(
        pkgs=[
            PkgVar(db.paru),
            PkgRecipe(PkgVar(db.git)),
            PkgRecipe(PkgVar(db.pacman)),
        ],
        installation=[
            ["cd", "~/.cache"],
            ["rm", "-rf", "yay"],
            ["git", "clone", "https://aur.archlinux.org/paru.git"],
            ["cd", "yay"],
            ["makepkg", "-si"]
        ]
    ),

    graphic=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.mesa)),
            PkgRecipe(PkgVar(db.intel_media_driver)),
            PkgRecipe(PkgVar(db.vulkan_intel)),
        ]
    ),

    audio=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.pipewire)),
            PkgRecipe(PkgVar(db.wireplumber)),
            PkgRecipe(PkgVar(db.pipewire_pulse)),
            PkgRecipe(PkgVar(db.pipewire_alsa)),
        ]
    ),

    internet=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.iwd)),
            PkgRecipe(PkgVar(db.openssh)),
            PkgRecipe(PkgVar(db.networkmanager)),
        ]
    ),

    disk=Box(
        pkgs=[
            PkgRecipe(
                PkgVar(db.udisks2),
                [
                    PkgRecipe(PkgVar(db.e2fsprogs)),
                    PkgRecipe(PkgVar(db.exfatprogs)),
                    PkgRecipe(PkgVar(db.ntfsprogs)),
                ]
            ),
            PkgRecipe(PkgVar(db.udiskie)),
            PkgRecipe(
                PkgVar(db.gvfs),
                [
                    PkgRecipe(PkgVar(db.gvfs_mtp)),
                ]
            ),
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

    thumbnail=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.tumbler)),
            PkgRecipe(PkgVar(db.ffmpegthumbnailer)),
            PkgRecipe(PkgVar(db.libgsf)),
            PkgRecipe(PkgVar(db.poppler_glib)),
        ]
    ),

    archive=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.seven_zip)),
            PkgRecipe(PkgVar(db.unzip)),
            PkgRecipe(PkgVar(db.zip)),
            PkgRecipe(PkgVar(db.unrar)),
            PkgRecipe(PkgVar(db.libarchive)),
        ]
    ),

    qt=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.qt6_wayland)),
        ]
    ),

    input_method=Box(
        pkgs=[
            PkgRecipe(PkgVar(db.fcitx5)),
            PkgRecipe(PkgVar(db.fcitx5_qt)),
            PkgRecipe(PkgVar(db.fcitx5_gtk)),
            PkgRecipe(PkgVar(db.fcitx5_configtool)),
            PkgRecipe(PkgVar(db.fcitx5_unikey)),
        ]
    )
)

application=Box(
    text_editor=Box(
        pkgs=[
            PkgRecipe(PkgVar(db2.neovim)),
            PkgRecipe(PkgVar(db2.emacs_wayland)),
        ]
    ),
    browser=Box(
        pkgs=[
            PkgRecipe(PkgVar(db2.firefox)),
            PkgRecipe(PkgVar(db2.zen_browser_bin)),
            PkgRecipe(PkgVar(db2.brave_bin)),
            PkgRecipe(PkgVar(db2.helium_browser_bin)),
        ]
    ),
    screen_record=Box(
        pkgs=[
            PkgRecipe(PkgVar(db2.gpu_screen_recorder)),
            PkgRecipe(PkgVar(db2.gpu_screen_recorder_ui)),
        ]
    ),

    opener=Box(
        pkgs=[
            PkgRecipe(PkgVar(db2.mpv)),
            PkgRecipe(PkgVar(db2.imv)),
            PkgRecipe(PkgVar(db2.featherpad)),
            PkgRecipe(
                PkgVar(db2.zathura),
                [
                    PkgRecipe(PkgVar(db2.zathura_pdf_mupdf))
                ]
            ),
            PkgRecipe(PkgVar(db2.xarchive)),
            PkgRecipe(
                PkgVar(db2.libreoffice_fresh),
                [
                    PkgRecipe(PkgVar(db2.libreoffice_fresh_vi)),
                    PkgRecipe(PkgVar(db2.libreoffice_fresh_en_gb))
                ]
            ),
        ]
    ),

    emulator=Box(
        pkgs=[
            PkgRecipe(PkgVar(db2.foot))
        ],
    ),

    mutiplexer=Box(
        pkgs=[
            PkgRecipe(PkgVar(db2.tmux))
        ],
    ),

    file_manager=Box(
        pkgs=[
            PkgRecipe(
                PkgVar(db2.thunar),
                [
                    PkgRecipe(PkgVar(db2.thunar_volman)),
                    PkgRecipe(PkgVar(db2.thunar_archive_plugin))
                ]
            )
        ]
    )

)

desktop_shell=Box(
    clipboard=Box(
        pkgs=[
            PkgRecipe(PkgVar(db3.cliphist)),
            PkgRecipe(PkgVar(db3.wl_clip_persist)),
        ],
    ),
    launcher=Box(
        pkgs=[
            PkgRecipe(PkgVar(db3.fuzzel)),
            PkgRecipe(PkgVar(db3.app2unit)),
        ],
    ),

    moniro=Box(
        pkgs=[
            PkgRecipe(PkgVar(db3.btop)),
        ],
    ),
)
