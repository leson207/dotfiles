from src.schema.enumeration import Relationship, Repo, Scope
from src.schema.atomic import Unit, Package, Topic


map = {}

Topic(
    name="dotfile-manager",
    recipes=[
        Package("stow", Repo.AOR),
        # Package("chemzmoi", Repo.AOR),
    ]
)

map["window-compositor"]=Topic(
    name="window-compositor",
    recipes=[
        Package(
            name="hyprland",
            repo=Repo.AOR,
            single_user_config=[
                "~/.config/hypr/hyprland",
                "~/.config/hypr/hyprland.conf",
            ],
        ),
        # Package("river", Repo.AOR),
        # Package("niri", Repo.AOR),
        # Package("mangowc", Repo.AOR)
    ]
)

Topic(
    name="session-manager",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package("app2unit", Repo.AUR),
        Package(
            name="uwsm",
            repo=Repo.AOR,
            single_user_config=["~./config/uwsm"],
            supporters=[Package("libnewt", Repo.AOR)]
        )
    ]
)

Topic(
    name="display-manager",
    recipes=[Package(name="sddm", repo=Repo.AOR, units=[Unit("sddm.service", Scope.MULTI_USER)])]
)

Topic(
    name="screen-share",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package("xdg-desktop-portal-gtk", Repo.AOR),
        Package("xdg-desktop-portal-hyprland", Repo.AOR),
    ]
)

Topic(
    name="bar",
    recipes=[
        Package(
            name="waybar",
            repo=Repo.AOR,
            units=[Unit("waybar.service", Scope.SINGLE_USER)],
            single_user_config=["~/.config/waybar"]
        ),
        # Package("eww", Repo.UNKNOWN),
        # Package("ags", Repo.UNKNOWN),
        # Package("hyprpanel", Repo.UNKNOWN),
        # Package("quickshell", Repo.UNKNOWN),
    ]
)

Topic(
    name="color-extractor",
    recipes=[
        # Package("pywall", Repo.AUR),
        # Package("wallust", Repo.AUR),
        # Package("hellwal", Repo.AUR),
        Package("matugen", Repo.AOR, single_user_config=["~/.config/matugen"]),
        # Package("python-colorthief", Repo.AOR),
        # Package("kde-material-you-colors", Repo.AUR),
    ]
)

Topic(
    name="qt-theming",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package("qt5ct", Repo.AOR, single_user_config=["~/.config/qt5ct"]),
        Package("qt6ct", Repo.AOR, single_user_config=["~/.config/qt5ct"]),
        Package("hyprqt6engine", Repo.AUR),
        Package("kvantum", Repo.AOR, single_user_config=["~/.config/Kvantum"]),
    ]
)

Topic(
    name="gtk-theming",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package(
            name="",
            repo=Repo.AOR,
            single_user_config=[
                "~/.config/gtk-3.0",
                "~/.config/gtk-4.0"
            ]
        ),
        Package("nwglook", Repo.AOR, single_user_config=["~/.config/nwg-look"]),
        Package(
            name="orchis-theme",
            repo=Repo.AOR,
            supporters=[
                Package("vimix-cursors", Repo.AOR),
                Package("tela-circle-icon-theme", Repo.AOR),
            ]
        ),
        Package("gnome-themes-extra", Repo.AOR),
    ]
)

Topic(
    name="wallpaper",
    recipes=[
        Topic(
            name="setter",
            recipes=[
                # Package("swww", Repo.AOR),
                # Package("awww-bin", Repo.AUR),
                # Package("swaybg", Repo.AOR),
                # Package("mpvpaper", Repo.AUR),
                Package(
                    name="hyprpaper",
                    repo=Repo.AOR,
                    units=[Unit("hyprpaper.service", Scope.SINGLE_USER)],
                    single_user_config=["~/.config/hypr/hyprpaper.conf"]
                ),
            ]
        ),
        Topic(
            name="picker",
            recipes=[
                Package("rofi", Repo.AOR, single_user_config=["~/.config/rofi"]),
                # Package("waypaper", Repo.AUR),
                # Package("waytrogen-bin", Repo.AUR),
            ]
        )
    ]
)

Topic(
    name="desktop-component",
    recipes=[
        Topic(
            name="screen-lock",
            recipes=[
                Package("hyprlock", Repo.AOR, single_user_config=["~/.config/hypr/hyprlock.conf"]),
            ]
        ),
        Topic(
            name="polkit",
            recipes=[Package("hyprpolkitagent", Repo.AOR, units=[Unit("hyprpolkitagent.service", Scope.SINGLE_USER)])]
        ),
        Topic(
            name="idle",
            recipes=[
                Package(
                    name="hypridle",
                    repo=Repo.AOR,
                    units=[Unit("hypridle.service", Scope.SINGLE_USER)],
                    single_user_config=["~/.config/hypr/hypridle.conf"]
                )
            ]
        ),
        Topic(
            name="backlight",
            recipes=[
                Package(
                    name="hyprsunset",
                    repo=Repo.AOR,
                    units=[Unit("hyprsunset.service", Scope.SINGLE_USER)],
                    single_user_config=["~/.config/hypr/hyprsunset.conf"]
                )
            ]
        )
    ]
)

Topic(
    name="launcher",
    recipes=[
        Package("fuzzel", Repo.AOR, single_user_config=["~/.config/fuzzel"]),
        Package("hyprlauncher", Repo.AOR, single_user_config=["~/.config/hypr/hyprlauncher.conf"]),
    ]
)

Topic(
    name="notification",
    recipes=[
        # Package("fnott", Repo.AOR),
        # Package("dunst", Repo.AOR, single_user_config=["~/.config/dunst"]),
        # Package("mako", Repo.AOR, units=[Unit("mako.service", Scope.SINGLE_USER)], single_user_config=["~/.config/mako"]),
        Package(
            name="swaync",
            repo=Repo.AOR,
            units=[Unit("swaync.service", Scope.SINGLE_USER)],
            single_user_config=["~/.config/swaync"]
        )
    ]
)

Topic(
    name="clipboard",
    recipes=[
        Topic(
            name="copy-paste",
            recipes=[Package("wl-clipboard", Repo.AOR)]
        ),
        Topic(
            name="history",
            recipes=[
                # Package("copyq", Repo.AOR),
                Package("cliphist", Repo.AOR),
                # Package("nwg-clipman", Repo.AOR),
                # Package("wl-clip-persist", Repo.AOR),
            ]
        )
    ]
)

Topic(
    name="input",
    recipes=[
        Topic(
            name="input-method",
            recipes=[
                Package(
                    name="fcitx5",
                    repo=Repo.AOR,
                    single_user_config=[
                        "~/.config/fcitx5/config"
                        "~/.config/fcitx5/profile"
                    ],
                    supporters=[
                        Package("fcitx5-unikey", Repo.AOR),
                        Package("fcitx5-configtool", Repo.AOR)
                    ]
                )
            ]
        ),
        Topic(
            name="keyboard-remapper",
            recipes=[
                Package("katana-bin", Repo.AUR, single_user_config=["~/.config/kanata"]),
                # Package("wlr-which-key", Repo.AUR)
                # Package("xremap-hypr-bin", Repo.AUR)
                # Package("xremap-wlroots-bin", Repo.AUR)
            ]
        )
    ]
)

Topic(
    name="font",
    recipes=[
        Topic(
            name="noto-fonts",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Package("noto-fonts", Repo.AOR),
                Package("noto-fonts-cjk", Repo.AOR),
                Package("noto-fonts-emoji", Repo.AOR)
            ]
        ),
        Topic(
            name="ttf",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Package("ttf-opensans", Repo.AOR),
                Package("ttf-fira-code", Repo.AOR),
                Package("ttf-cascadia-code-nerd", Repo.AOR),
                Package("ttf-jetbrains-mono-nerd", Repo.AOR)
            ]
        ),
        Topic(
            name="tex-gyre",
            relationship=Relationship.ASSOCIATED,
            recipes=[Package("tex-gyre-fonts", Repo.AOR)]
        )
    ]
)

Topic(
    name="shell",
    recipes=[
        # Package("zsh", Repo.AOR),
        # Package("fish", Repo.AOR),
        Package("bash", Repo.AOR, single_user_config=["~/.bashrc", "~/.bash_profile"]),
        Package(
            name="nushell",
            repo=Repo.AOR,
            single_user_config=[
                # "~/.config/nushell",
                "~/.config/nushell/config.nu",
                "~/.config/nushell/env.nu",
            ]
        ),
    ]
)

Topic(
    name="shell-history",
    recipes=[Package("atuin", Repo.AOR)]
)

Topic(
    name="shell-promt",
    recipes=[Package("starship", Repo.AOR, single_user_config=["~/.config/starship.toml"])]
)

Topic(
    name="terminal-emulator",
    recipes=[
        Package(
            name="foot",
            repo=Repo.AOR,
            units=[Unit("foot-server.service", Scope.SINGLE_USER)],
            single_user_config=["~/.config/foot"]
        ),
        Package(
            name="wezterm-git",
            repo=Repo.AUR,
            single_user_config=["~/.config/wezterm"]
        ),
        Package("kitty", Repo.AOR, single_user_config=["~/.config/kitty"]),
        # Package("aclacritty", Repo.AOR),
        # Package("ghostty", Repo.AOR, units=[Unit("app-com.mitchellh.ghostty.service", Scope.SINGLE_USER)]),
    ]
)

Topic(
    name="terminal-multiplexer",
    recipes=[
        Package("tmux", Repo.AOR, single_user_config=["~/.tmux.conf"]),
        Package("zellij", Repo.AOR),
    ]
)

Topic(
    name="file",
    recipes=[
        Topic(
            name="manager",
            recipes=[
                Package(
                    name="thunar",
                    repo=Repo.AOR,
                    supporters=[
                        Package("thunar-volman", Repo.AOR),
                        Package("thunar-archive-plugin", Repo.AOR),
                        Package("thunar-media-tags-plugin", Repo.AOR),
                        # Package("catfish", Repo.AOR),
                        # Package("plocate", Repo.AOR),
                        # Package("zeitgeist", Repo.AOR),
                    ]
                ),
                Package(
                    name="yazi",
                    repo=Repo.AOR,
                    single_user_config=["~/.config/yazi"],
                    supporters=[
                        Package("7zip", Repo.AOR),
                        Package("chafa", Repo.AOR),
                        Package("ffmpeg", Repo.AOR),
                        Package("jq", Repo.AOR),
                        Package("poppler", Repo.AOR),
                        Package("resvg", Repo.AOR),
                        Package(
                            name="imagemagick",
                            repo=Repo.AOR,
                            supporters=[Package("libjpeg-turbo", Repo.AOR)]
                        )
                    ]
                ),
                # Package("superfile", Repo.AOR)
            ]
        ),
        Topic(
            name="misc",
            recipes=[
                Package("xdg-user-dirs", Repo.AOR, units=[Unit("xdg-user-dirs-update.service", Scope.SINGLE_USER)]),
                Package("czkawka-gui-bin", Repo.AUR),
            ]
        )
    ]
)

Topic(
    name="thumnail",
    recipes=[
        Package(
            name="tumbler",
            repo=Repo.AOR,
            units=[Unit("tumblerd.service", Scope.SINGLE_USER)],
            supporters=[
                Package("ffmpegthumbnailer", Repo.AOR),
                Package("freetype2", Repo.AOR),
                Package("libgepub", Repo.AOR),
                Package("libgsf", Repo.AOR),
                Package("libopenraw", Repo.AOR),
                Package("poppler-glib", Repo.AOR),
                Package("libarchive", Repo.AOR),

                # Package("ueberzugpp", Repo.AOR),
            ]
        )
    ]
)

Topic(
    name="video-player",
    recipes=[
        Package("mpv", Repo.AOR, single_user_config=["~/.config/mpv"]),
        # Package("vlc", Repo.AOR),
        # Package("clapper", Repo.AOR),
    ]
)

Topic(
    name="image-viewer",
    recipes=[
        Package("mpv", Repo.AOR, single_user_config=["~/.config/mpv"]),
        # Package("imv", Repo.AOR),
        # Package("feh", Repo.AOR),
        # Package("gthumb", Repo.AOR),
        # Package("swayimg", Repo.AOR),
    ]
)

Topic(
    name="screen-shot",
    recipes=[
        # Topic(
        #     name="capture",
        #     recipes=[
        #         Package("grim", Repo.AOR)
        #     ]
        # ),
        # Topic(
        #     name="crop",
        #     recipes=[
        #         Package("slurp", Repo.AOR)
        #     ]
        # ),
        # Topic(
        #     name="annotate",
        #     recipes=[
        #         Package("swappy", Repo.AOR),
        #         Package("satty", Repo.AOR)
        #     ]
        # ),
        Topic(
            name="full",
            recipes=[
                # Package("flameshot", Repo.AOR),
                Package("hyprshot", Repo.AOR, supporters=[Package("hyprpicker", Repo.AOR)]),
            ]
        )
    ]
)

Topic(
    name="screen-recorder",
    recipes=[
        # Package("wl-screenrec", Repo.AUR),
        # Package("obs-studio", Repo.AOR),
        # Package("wf-recorder", Repo.AOR),
        Package("gpu-screen-recorder", Repo.AOR, supporters=[Package("gpu-screen-recorder-ui", Repo.AOR)]),
    ]
)

Topic(
    name="browser",
    recipes=[
        Topic(
            name="gui",
            recipes=[
                Package("firefox", Repo.AOR, supporters=[Package("speech-dispatcher", Repo.AOR)]),
                Package("brave-bin", Repo.AUR),
                Package("zen-browser-bin", Repo.AUR),
                Package("google-chrome-bin", Repo.AUR, single_user_config=["~/.config/chrome-flags.conf"]),
                Package("helium-browser-bin", Repo.AUR, single_user_config=["~/.config/helium-flags.conf"]),
                Package("thorium-browser-bin", Repo.AUR, single_user_config=["~/.config/thorium-flags.conf"]),
                Package("microsoft-edge-stable-bin", Repo.AUR)
            ]
        ),
        # Topic(
        #     name="keyboard-driven",
        #     recipes=[
        #         Package("browsh", Repo.AUR),
        #         Package("nyxt", Repo.AOR),
        #         Package("lynx", Repo.AOR),
        #         Package("luakit", Repo.AOR),
        #     ]
        # )
    ]
)

Topic(
    name="misc",
    recipes=[
        Package("hugo", Repo.AUR),
        Package("anki-bin", Repo.AUR),
        Package("okular", Repo.AOR),
        Package("mediawriter", Repo.AOR),
        Package("cava", Repo.AOR, single_user_config=["~/.config/cava"]),
        Package("electron", Repo.AOR, single_user_config=["~/.config/electron-flags.conf"])
    ]
)

#TODO: this recipes need extension too, how to write
Topic(
    name="firefox-theme",
    recipes=[Package("python-pywalfox", Repo.AUR)]
)
