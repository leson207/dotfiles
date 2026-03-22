dofile("utils.lua")

local m={}


m.dotfile_manager={
    stow=aor,
    -- chemzmoi=aor,
}

m.window_compositor={
    -- niri=aor,
    -- river=aor,
    -- mangowc=aor,
    hyprland={
        Repo.AOR,
        single_user_config={
            "~/.config/hypr/hyprland",
            "~/.config/hypr/hyprland.conf",
            {"sh", "~/.config/hypr/hyprland/scripts/first_intel_gpu.sh"},
            {"sh", "~/.config/hypr/hyprland/scripts/first_amd_gpu.sh"},
        },
    }
}

m.session_manager.relationship=Relationship.ASSOCIATED
m.session_manager={
    app2unit=aor,
    uwsm={
        Repo.AOR,
        single_user_config={"~./config/uwsm"},
        supporters={libnewt=aor}
    }
}

m.display_manager.sddm={
    Repo.AOR,
    units={"sddm.service", Scope.MULTI_USER},
    supporters={
        qt6_svg=aor,
        qt6_wayland=aor,
        qt6_virtualkeyboard=aor,
        qt6_multimedia_ffmpeg=aor
    },
    multiple_user_setting={
        "/etc/sddm.conf",
        "/etc/sddm.conf.d/virtualkbd.conf",
        {"sudo", "git", "clone", "-b", "master", "--depth", "1", "https://github.com/keyitdev/sddm-astronaut-theme.git", "/usr/share/sddm/themes/sddm-astronaut-theme"},
        {"sudo", "cp", "-r", "/usr/share/sddm/themes/sddm-astronaut-theme/Fonts/*", "/usr/share/fonts/"},
        "/usr/share/sddm/themes/sddm-astronaut-theme/metadata.desktop"
    }
}

m.screen_share.relationship=Relationship.ASSOCIATED
m.screen_share={
    xdg_desktop_portal_gtk=aor,
    xdg_desktop_portal_hyprland=aor
}

m.bar={
    waybar={
        Repo.AOR,
        units={"waybar.service", Scope.SINGLE_USER},
        single_user_config={"~/.config/waybar"}
    },
    -- ashell=aur,
    -- hyprpanel=aor,
}

m.widget_system={
    -- quickshell=aor,
    -- eww=aor,
    -- ags=aor,
}

m.color_extractor={
    -- pywall=aor,
    -- wallust=aor,
    -- hellwal=aor,
    matugen={Repo.AOR, single_user_config={"~/.config/matugen"}},
    -- python_colorthief=aor,
    -- kde_material_you_colors=aor,
}
m.qt_theme.relationship=Relationship.ASSOCIATED
m.qt_theme={
    qt5ct={Repo.AOR, single_user_config={"~/.config/qt5ct"}},
    qt6ct={Repo.AOR, single_user_config={"~/.config/qt6ct"}},
    hyprqt6engine=aor,
    kvantum={Repo.AOR, single_user_config={"~/.config/Kvantum"}},
}

m.gtk_theme.relationship=Relationship.ASSOCIATED
m.gtk_theme={
    gtk={
        single_user_config={
            "~/.config/gtk-3.0",
            "~/.config/gtk-4.0"
        }
    },
    nwg_look={Repo.AOR, single_user_config={"~/.config/nwg-look"}},
    orchis_theme={
        Repo.AOR,
        supporters={
            vimix_cursors=aor,
            tela_circle_icon_theme=aor,
        },
    },
    gnome_themes_extra=aor,
}

m.wallpaper.resources={"https://wiki.hypr.land/Useful-Utilities/Wallpapers/"}
m.wallpaper.setter={
    -- swww=aor,
    -- swaybg=aor,
    -- awww_bin=aur,
    -- mpvpaper=aur,
    -- wpaperd=aur,
    hyprpaper={
        Repo.AOR,
        units={"hyprpaper.service", Scope.SINGLE_USER},
        single_user_config={"~/.config/hypr/hyprpaper.conf"}
    }
}

m.wallpaper.picker={
    rofi={Repo.AOR, single_user_config={"~/.config/rofi"}},
    -- waypaper=aur,
    -- wallrizz=aur,
    -- waytrogen_bin=aur,
}

m.screen_lock.hyprlock={Repo.AOR, single_user_config={"~/.config/hypr/hyprlock.conf"}}
m.polkit.hyprpolkitagent={Repo.AOR, units={"hyprpolkitagent.service", Scope.SINGLE_USER}}
m.idle.hypridle={
    Repo.AOR,
    units={"hypridle.service", Scope.SINGLE_USER},
    single_user_config={"~/.config/hypr/hypridle.conf"}
}
m.backlight.hyprsunset={
    Repo.AOR,
    units={"hyprsunset.service", Scope.SINGLE_USER},
    single_user_config={"~/.config/hypr/hyprsunset.conf"}
}

m.launcher={
    fuzzel={Repo.AOR, single_user_config={"~/.config/fuzzel"}},
    hyprlauncher={Repo.AOR, single_user_config={"~/.config/hypr/hyprlauncher.conf"}},
}

m.notification={
    -- fnott=aor,
    -- dunst={Repo.AOR, single_user_config={"~/.config/dunst"}},
    -- mako={Repo.AOR, units={"mako.service", Scope.SINGLE_USER}, single_user_config={"~/.config/mako"}},
    swaync={Repo.AOR, units={"swaync.service", Scope.SINGLE_USER}, single_user_config={"~/.config/swaync"}},
}

m.clipboard.copy_paste.wl_clipboard=aor
m.clipboard.history={
    -- copyq=aor,
    -- TODO: how and should i declate it config in hyprland?
    cliphist=aor,
    -- nwg_clipman=aor,
    -- wl_clllip_persist=aor,
}

m.input.method.fcitx5={
    Repo.AOR,
    single_user_config={
        "~/.config/fcitx5/config",
        "~/.config/fcitx5/profile"
    },
    supporters={
        fcitx5_unikey=aor,
        -- fcitx5_lotus_bin=aur, need quite more config here
        fcitx5_configtool=aor
    }
}
m.input.remapper={
    kanata_bin={
        Repo.AUR, single_user_config={"~/.config/kanata"},
        multiple_user_config={
            "/etc/udev/rules.d/90-uinput.rules",
            -- ACTION=="add", KERNEL=="uinput", RUN+="/usr/bin/setfacl -m u:victor:rw /dev/uinput"
        },
        scripts={
            "sudo udevadm control --reload-rules",
            "sudo udevadm trigger",
            "sudo modprobe -r uinput",
            "sudo modprobe uinput"
        },
        groups={
            "input",
            "uinput",
        }
    },
    -- kanata_bin={
    --     Repo.AUR, single_user_config={"~/.config/kanata"},
    --     multiple_user_config={
    --         "/etc/udev/rules.d/99-uinput.rules"
    --         -- KERNEL=="uinput", MODE="0660", GROUP="uinput", OPTIONS+="static_node=uinput"
    --     },
    --     scripts={
    --         "sudo udevadm control --reload",
    --         "sudo udevadm trigger --verbose --sysname-match=uinput",
    --
    --         "sudo modprobe uinput"
    --     },
    --     groups={
    --         "input",
    --         "uinput",
    --     }
    -- },
    -- wlr_which_key=aur,
    -- xremap_hypr_bin=aur,
    -- xremap_wlroots_bin=aur,
    -- input_remapper_bin=aur,
    -- keyd=aor,
    -- kmonad=aor,
}

m.keylogger={
    logkeys=aur,
    whatpulse=aur,
    osa=aur,
    keymouse_logger={repo=Repo.GTIHUB}
}

m.font.noto={
    noto_fonts=aor,
    noto_fonts_cjk=aor,
    noto_fonts_emoji=aor,
}
m.font.ttf={
    ttf_opensans=aor,
    ttf_fira_code=aor,
    ttf_cascadia_code_nerd=aor,
    ttf_jetbrains_mono_nerd=aor,
}
m.font.tex.tex_gyre_fonts=aor

m.shell={
    zsh=aor,
    fish=aor,
    bash={Repo.AOR, single_user_config={"~/.bashrc", "~/.bash_profile"}},
    nushell={
        Repo.AOR,
        single_user_config={
            "~/.config/nushell/env.nu",
            "~/.config/nushell/config.nu",
        },
        personalized_data={
            "~/.config/nushell/history.txt",
            "~/.config/nushell/history.sqlite3"
        }
    }
}

m.shell.history.atuin={
    Repo.AOR,
    supporters={
        nushell={
            Repo.AOR,
            single_user_config={
                "~/.config/nushell/config.nu",
            },
            personalized_data={
                "~/.config/nushell/history.txt",
                "~/.config/nushell/history.sqlite3"
            }
        }
    },
    scripts={
        "mkdir ~/.local/share/atuin/",
        "atuin init nu | save ~/.local/share/atuin/init.nu"
    }
}

m.shell.prompt.starship={
    Repo.AOR,
    single_user_config={"~/.config/starship.toml"},
    scripts={
        -- "mkdir ($nu.data-dir | path join "vendor/autoload")",
        -- "starship init nu | save -f ($nu.data-dir | path join "vendor/autoload/starship.nu")"
    },
    supporters={
        nushell={
            Repo.AOR,
            single_user_config={"~/.config/nushell/config.nu"},
        }
    },

}

m.terminal.emulator={
    foot={
        Repo.AOR,
        units={"foot-server.service", Scope.SINGLE_USER},
        single_user_config={"~/.config/foot"}
    },
    wezterm_git={
        Repo.AUR,
        single_user_config={"~/.config/wezterm"}
    },
    kitty={Repo.AOR, single_user_config={"~/.config/kitty"}},
    aclacritty=aor,
    ghostty={Repo.AOR, units={"app-com.mitchellh.ghostty.service", Scope.SINGLE_USER}},
}

m.terminal.multiplexer={
    tmux={Repo.AOR, single_user_config={"~/.tmux.conf"}},
    zellij=aor,
}

m.file.manager={
    thunar={
        Repo.AOR,
        supporters={
            thunar_volman=aor,
            thunar_archive_plugin=aor,
            thunar_media_tags_plugin=aor,
            -- catfish=aor,
            -- plocate=aor,
            -- zeitgeist=aor,
        }
    },
    yazi={
        Repo.AOR,
        single_user_config={"~/.config/yazi"},
        supporters={
            ["7zip"]=aor,
            chafa=aor,
            ffmpeg=aor ,
            jq=aor,
            poppler=aor,
            resvg=aor,
            imagemagick={Repo.AOR, supporters={libjpeg_turbo=aor}}
        }
    },
    superfile=aor
}
m.file.misc={
    xdg_user_dirs={Repo.AOR, units={"xdg-user-dirs-update.service", Scope.SINGLE_USER}},
    czkawka_gui_bin=aur,
}

m.file.thumnail.tumbler={
    Repo.AOR,
    units={"tumblerd.service", Scope.SINGLE_USER},
    supporters={
        ffmpegthumbnailer=aor,
        freetype2=aor,
        libgepub=aor,
        libgsf={Repo.AOR},
        libopenraw=aor,
        poppler_glib=aor,
        libarchive=aor,
        -- ueberzugpp=aor,
    }
}

m.media.videp={
    mpv={Repo.AOR, single_user_config={"~/.config/mpv"}},
    -- vlc=aor,
    -- clapper=aor,
}
m.media.image={
    mpv={Repo.AOR, single_user_config={"~/.config/mpv"}},
    -- imv=aor,
    -- feh=aor,
    -- gthumb=aor,
    -- swayimg=aor,
}

m.screen.capture={
    -- grim=aor,
    -- flameshot={Repo.AOR},
    hyprshot={Repo.AOR, supporters={hyprpicker=aor}}
}
m.screen.crop.slurp=aor
m.screen.annotate={
    swappy=aor,
    satty=aor,
}

m.screen.record={
    -- wl_screenrec=aur,
    -- obs_studio=aor,
    -- wf_recorder=aor,
    gpu_screen_recorder={Repo.AOR, supporters={gpu_screen_recorder_ui=aor}}
}

m.browser.gui={
    firefox={Repo.AOR, supporters={speech_dispatcher=aor}},
    brave_bin=aur,
    zen_browser_bin=aur,
    google_chrome_bin={Repo.AUR, single_user_config={"~/.config/chrome-flags.conf"}},
    helium_browser_bin={Repo.AUR, single_user_config={"~/.config/helium-flags.conf"}},
    thorium_browser_bin={Repo.AUR, single_user_config={"~/.config/thorium-flags.conf"}},
    microsoft_edge_stable_bin=aur,
}

m.misc={
    -- hugo=aor,
    anki=aor,
    okular=aor,
    mediawriter=aor,
    cava={Repo.AOR, single_user_config={"~/.config/cava"}},
    electron={Repo.AOR, single_user_config={"~/.config/electron-flags.conf"}},
    --TODO: this recipes need extension too, how to write
    python_pywalfox=aur
}
