local root={
    dms_shell_niri={
        repo=Repo.AOR,
        units={"dms.service", Scope.SINGLE_USER},
    },
    theme={
        gtk={
            gtk3={repo=Repo.AOR},
            adw_gtk_theme={repo=Repo.AOR},
            installation={
                "~/.config/gtk-3.0/settings.ini",
                "[Settings] \
                gtk-icon-theme-name=Papirus-Dark"
            }
        },
        qt={
            qt6ct={repo=Repo.AOR},
            qt6ct_kde={repo=Repo.AOR},
            installation={
                "~/.config/qt6ct/qt6ct.conf",
                "[Appearance]\
                icon_theme=Papirus-Dark"
            }
        },
        icon={
             breeze_icons={repo=Repo.AOR},
             papirus_icon_theme={repo=Repo.AOR},
             adwaita_icon_theme={repo=Repo.AOR},
             hicolor_icon_theme={repo=Repo.AOR},
            -- Tela, Nordzy
        },
        firefox={
            python_pywalfox={
                repo=Repo.AUR,
                installation={
                    "ln -sf ~/.cache/wal/dank-pywalfox.json ~/.cache/wal/colors.json"
                },
                installation_v1={
                    {"about:config", "toolkit.legacyuserprofilecustomizations.stylesheets", "true"},
                    {"about:config", "vg.context-properties.content.enabled", "true"},
                    {"about:config", "userChrome.theme-material", "true"},

                    "export PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name \"*.default-release\" | head -n 1)",
                    "curl -L -o \"$PROFILE_DIR/chrome.zip\" https://github.com/edelvarden/material-fox-updated/releases/download/v2.0.0/chrome.zip",
                    "unzip -o \"$PROFILE_DIR/chrome.zip\" -d \"$PROFILE_DIR\"",
                    "rm \"$PROFILE_DIR/chrome.zip\"",

                    "export PROFILE_DIR=$(find ~/.mozilla/firefox -maxdepth 1 -type d -name \"*.default-release\" | head -n 1)",
                    "rm -f \"$PROFILE_DIR/chrome/theme-material-blue.css\"",
                    "ln -sf ~/.config/DankMaterialShell/firefox.css \"$PROFILE_DIR/chrome/theme-material-blue.css\""
                }
            }
        },
        zen_browser={
            installation={
                "export PROFILE_DIR=$(find ~/.zen -maxdepth 1 -type d -name \"*.Default Profile\" | head -n 1)",
                "mkdir -p \"$PROFILE_DIR/chrome\"",
                "ln -sf ~/.config/DankMaterialShell/zen.css \"$PROFILE_DIR/chrome/userChrome.css\"",
                {"about:config", "toolkit.legacyUserProfileCustomizations.stylesheets", "true"}
            }
        },
        ghostty={
            installation={
                {"echo \"theme = dankcolors\" >> ~/.config/ghostty/config"},
                {"echo \"app-notifications = no-clipboard-copy,no-config-reload\" >> ~/.config/ghostty/config"}
            }
        },
        kitty={
            installation={
                "echo \"include dank-tabs.conf\" >> ~/.config/kitty/kitty.conf",
                "echo \"include dank-theme.conf\" >> ~/.config/kitty/kitty.conf"
            }
        },
        foot={
            "~/.config/foot/foot.ini",
            "[main]\
            include=~/.config/foot/dank-colors.ini"
        },
        alacritty={
            "~/.config/alacritty/alacritty.toml",
            "[general]\
                import = [\
                    \"~/.config/alacritty/dank-theme.toml\"\
                ]"
        }

    },

    kimageformats={repo=Repo.AOR},
    cava={repo=Repo.AOR},
    dgop={repo=Repo.AOR},
    dsearch_bin={
        repo=Repo.AUR,
        units={"dsearch.service", Scope.SINGLE_USER},
    },
    matugen={repo=Repo.AUR},
    qt6_multimedia={repo=Repo.AUR},
    papirus_icon_theme={
        repo=Repo.AOR,
        env={
            "QS_ICON_THEME=Papirus"
        }
    }
}
