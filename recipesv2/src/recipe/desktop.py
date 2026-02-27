from src.schema.enumeration import Relationship, Repo, Scope
from src.schema.atomic import Unit, Package, Topic


map = {}

Topic(
    name="dotfile-manager",
    recipes=[
        Package("stow", Repo.OFFICIAL),
        # Package("chemzmoi", Repo.OFFICIAL),
    ]
)

map["window-compositor"]=Topic(
    name="window-compositor",
    recipes=[
        Package(
            name="hyprland",
            repo=Repo.OFFICIAL,
            single_user_config=[
                "~/.config/hypr/hyprland",
                "~/.config/hypr/hyprland.conf",
            ],
        ),
        # Package("river", Repo.OFFICIAL),
        # Package("niri", Repo.OFFICIAL),
        # Package("mangowc", Repo.OFFICIAL)
    ]
)

Topic(
    name="session-manager",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package("app2unit", Repo.AUR),
        Package(
            name="uwsm",
            repo=Repo.OFFICIAL,
            single_user_config=["~./config/uwsm"],
            supporters=[Package("libnewt", Repo.OFFICIAL)]
        )
    ]
)

Topic(
    name="display-manager",
    recipes=[Package(name="sddm", repo=Repo.OFFICIAL, units=[Unit("sddm.service", Scope.MULTI_USER)])]
)

Topic(
    name="screen-share",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package("xdg-desktop-portal-gtk", Repo.OFFICIAL),
        Package("xdg-desktop-portal-hyprland", Repo.OFFICIAL),
    ]
)

Topic(
    name="bar",
    recipes=[
        Package(
            name="waybar",
            repo=Repo.OFFICIAL,
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
        Package("matugen", Repo.OFFICIAL, single_user_config=["~/.config/matugen"]),
        # Package("python-colorthief", Repo.OFFICIAL),
        # Package("kde-material-you-colors", Repo.AUR),
    ]
)

Topic(
    name="qt-theming",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package("qt5ct", Repo.OFFICIAL, single_user_config=["~/.config/qt5ct"]),
        Package("qt6ct", Repo.OFFICIAL, single_user_config=["~/.config/qt5ct"]),
        Package("hyprqt6engine", Repo.AUR),
        Package("kvantum", Repo.OFFICIAL, single_user_config=["~/.config/Kvantum"]),
    ]
)

Topic(
    name="gtk-theming",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package(
            name="",
            repo=Repo.OFFICIAL,
            single_user_config=[
                "~/.config/gtk-3.0",
                "~/.config/gtk-4.0"
            ]
        ),
        Package("nwglook", Repo.OFFICIAL, single_user_config=["~/.config/nwg-look"]),
        Package(
            name="orchis-theme",
            repo=Repo.OFFICIAL,
            supporters=[
                Package("vimix-cursors", Repo.OFFICIAL),
                Package("tela-circle-icon-theme", Repo.OFFICIAL),
            ]
        ),
        Package("gnome-themes-extra", Repo.OFFICIAL),
    ]
)

Topic(
    name="wallpaper",
    recipes=[
        Topic(
            name="setter",
            recipes=[
                # Package("swww", Repo.OFFICIAL),
                # Package("awww-bin", Repo.AUR),
                # Package("swaybg", Repo.OFFICIAL),
                # Package("mpvpaper", Repo.AUR),
                Package(
                    name="hyprpaper",
                    repo=Repo.OFFICIAL,
                    units=[Unit("hyprpaper.service", Scope.SINGLE_USER)],
                    single_user_config=["~/.config/hypr/hyprpaper.conf"]
                ),
            ]
        ),
        Topic(
            name="picker",
            recipes=[
                Package("rofi", Repo.OFFICIAL, single_user_config=["~/.config/rofi"]),
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
                Package("hyprlock", Repo.OFFICIAL, single_user_config=["~/.config/hypr/hyprlock.conf"]),
                # Package("quickshell", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="polkit",
            recipes=[Package("hyprpolkitagent", Repo.OFFICIAL, units=[Unit("hyprpolkitagent.service", Scope.SINGLE_USER)])]
        ),
        Topic(
            name="idle",
            recipes=[
                Package(
                    name="hypridle",
                    repo=Repo.OFFICIAL,
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
                    repo=Repo.OFFICIAL,
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
        Package("fuzzel", Repo.OFFICIAL, single_user_config=["~/.config/fuzzel"]),
        Package("hyprlauncher", Repo.OFFICIAL, single_user_config=["~/.config/hypr/hyprlauncher.conf"]),
    ]
)

Topic(
    name="notification",
    recipes=[
        # Package("fnott", Repo.OFFICIAL),
        # Package("dunst", Repo.OFFICIAL, single_user_config=["~/.config/dunst"]),
        # Package("mako", Repo.OFFICIAL, units=[Unit("mako.service", Scope.SINGLE_USER)], single_user_config=["~/.config/mako"]),
        Package(
            name="swaync",
            repo=Repo.OFFICIAL,
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
            recipes=[Package("wl-clipboard", Repo.OFFICIAL)]
        ),
        Topic(
            name="history",
            recipes=[
                # Package("copyq", Repo.OFFICIAL),
                Package("cliphist", Repo.OFFICIAL),
                # Package("nwg-clipman", Repo.OFFICIAL),
                # Package("wl-clip-persist", Repo.OFFICIAL),
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
                    repo=Repo.OFFICIAL,
                    single_user_config=[
                        "~/.config/fcitx5/config"
                        "~/.config/fcitx5/profile"
                    ],
                    supporters=[
                        Package("fcitx5-unikey", Repo.OFFICIAL),
                        Package("fcitx5-configtool", Repo.OFFICIAL)
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
                Package("noto-fonts", Repo.OFFICIAL),
                Package("noto-fonts-cjk", Repo.OFFICIAL),
                Package("noto-fonts-emoji", Repo.OFFICIAL)
            ]
        ),
        Topic(
            name="ttf",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Package("ttf-opensans", Repo.OFFICIAL),
                Package("ttf-fira-code", Repo.OFFICIAL),
                Package("ttf-cascadia-code-nerd", Repo.OFFICIAL),
                Package("ttf-jetbrains-mono-nerd", Repo.OFFICIAL)
            ]
        ),
        Topic(
            name="tex-gyre",
            relationship=Relationship.ASSOCIATED,
            recipes=[Package("tex-gyre-fonts", Repo.OFFICIAL)]
        )
    ]
)

Topic(
    name="shell",
    recipes=[
        # Package("zsh", Repo.OFFICIAL),
        # Package("fish", Repo.OFFICIAL),
        Package("bash", Repo.OFFICIAL, single_user_config=["~/.bashrc", "~/.bash_profile"]),
        Package(
            name="nushell",
            repo=Repo.OFFICIAL,
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
    recipes=[Package("atuin", Repo.OFFICIAL)]
)

Topic(
    name="shell-promt",
    recipes=[Package("starship", Repo.OFFICIAL, single_user_config=["~/.config/starship.toml"])]
)

Topic(
    name="terminal-emulator",
    recipes=[
        Package(
            name="foot",
            repo=Repo.OFFICIAL,
            units=[Unit("foot-server.service", Scope.SINGLE_USER)],
            single_user_config=["~/.config/foot"]
        ),
        Package(
            name="wezterm-git",
            repo=Repo.AUR,
            single_user_config=["~/.config/wezterm"]
        ),
        Package("kitty", Repo.OFFICIAL, single_user_config=["~/.config/kitty"]),
        # Package("aclacritty", Repo.OFFICIAL),
        # Package("ghostty", Repo.OFFICIAL, units=[Unit("app-com.mitchellh.ghostty.service", Scope.SINGLE_USER)]),
    ]
)

Topic(
    name="terminal-multiplexer",
    recipes=[
        Package("tmux", Repo.OFFICIAL, single_user_config=["~/.tmux.conf"]),
        Package("zellij", Repo.OFFICIAL),
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
                    repo=Repo.OFFICIAL,
                    supporters=[
                        Package("thunar-volman", Repo.OFFICIAL),
                        Package("thunar-archive-plugin", Repo.OFFICIAL),
                        Package("thunar-media-tags-plugin", Repo.OFFICIAL),
                        # Package("catfish", Repo.OFFICIAL),
                        # Package("plocate", Repo.OFFICIAL),
                        # Package("zeitgeist", Repo.OFFICIAL),
                    ]
                ),
                Package(
                    name="yazi",
                    repo=Repo.OFFICIAL,
                    single_user_config=["~/.config/yazi"],
                    supporters=[
                        Package("7zip", Repo.OFFICIAL),
                        Package("chafa", Repo.OFFICIAL),
                        Package("ffmpeg", Repo.OFFICIAL),
                        Package("jq", Repo.OFFICIAL),
                        Package("poppler", Repo.OFFICIAL),
                        Package("resvg", Repo.OFFICIAL),
                        Package(
                            name="imagemagick",
                            repo=Repo.OFFICIAL,
                            supporters=[Package("libjpeg-turbo", Repo.OFFICIAL)]
                        )
                    ]
                ),
                # Package("superfile", Repo.OFFICIAL)
            ]
        ),
        Topic(
            name="misc",
            recipes=[
                Package("xdg-user-dirs", Repo.OFFICIAL, units=[Unit("xdg-user-dirs-update.service", Scope.SINGLE_USER)]),
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
            repo=Repo.OFFICIAL,
            units=[Unit("tumblerd.service", Scope.SINGLE_USER)],
            supporters=[
                Package("ffmpegthumbnailer", Repo.OFFICIAL),
                Package("freetype2", Repo.OFFICIAL),
                Package("libgepub", Repo.OFFICIAL),
                Package("libgsf", Repo.OFFICIAL),
                Package("libopenraw", Repo.OFFICIAL),
                Package("poppler-glib", Repo.OFFICIAL),
                Package("libarchive", Repo.OFFICIAL),

                # Package("ueberzugpp", Repo.OFFICIAL),
            ]
        )
    ]
)

Topic(
    name="video-player",
    recipes=[
        Package("mpv", Repo.OFFICIAL, single_user_config=["~/.config/mpv"]),
        Package("vlc", Repo.OFFICIAL, single_user_config=["~/.config/vlc"]),
        # Package("clapper", Repo.OFFICIAL),
    ]
)

Topic(
    name="image-viewer",
    recipes=[
        Package("mpv", Repo.OFFICIAL, single_user_config=["~/.config/mpv"]),
        # Package("imv", Repo.OFFICIAL),
        # Package("feh", Repo.OFFICIAL),
        # Package("gthumb", Repo.OFFICIAL),
        # Package("swayimg", Repo.OFFICIAL),
    ]
)

Topic(
    name="screen-shot",
    recipes=[
        # Topic(
        #     name="capture",
        #     recipes=[
        #         Package("grim", Repo.OFFICIAL)
        #     ]
        # ),
        # Topic(
        #     name="crop",
        #     recipes=[
        #         Package("slurp", Repo.OFFICIAL)
        #     ]
        # ),
        # Topic(
        #     name="annotate",
        #     recipes=[
        #         Package("swappy", Repo.OFFICIAL),
        #         Package("satty", Repo.OFFICIAL)
        #     ]
        # ),
        Topic(
            name="full",
            recipes=[
                # Package("flameshot", Repo.OFFICIAL),
                Package("hyprshot", Repo.OFFICIAL, supporters=[Package("hyprpicker", Repo.OFFICIAL)]),
            ]
        )
    ]
)

Topic(
    name="screen-recorder",
    recipes=[
        # Package("wl-screenrec", Repo.AUR),
        # Package("obs-studio", Repo.OFFICIAL),
        # Package("wf-recorder", Repo.OFFICIAL),
        Package("gpu-screen-recorder", Repo.AUR, supporters=[Package("gpu-screen-recorder-ui", Repo.AUR)]),
    ]
)

Topic(
    name="browser",
    recipes=[
        Topic(
            name="gui",
            recipes=[
                Package("firefox", Repo.OFFICIAL, supporters=[Package("speech-dispatcher", Repo.OFFICIAL)]),
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
        #         Package("nyxt", Repo.OFFICIAL),
        #         Package("luakit", Repo.OFFICIAL),
        #         Package("lynx", Repo.OFFICIAL),
        #         Package("browsh", Repo.AUR),
        #     ]
        # )
    ]
)

Topic(
    name="misc",
    recipes=[
        Package("hugo", Repo.AUR),
        Package("anki-bin", Repo.AUR),
        Package("okular", Repo.OFFICIAL),
        Package("mediawriter", Repo.OFFICIAL),
        Package("cava", Repo.OFFICIAL, single_user_config=["~/.config/cava"]),
        Package("electron", Repo.OFFICIAL, single_user_config=["~/.config/electron-flags.conf"])
    ]
)

#TODO: this recipes need extension too, how to write
Topic(
    name="firefox-theme",
    recipes=[Package("python-pywalfox", Repo.AUR)]
)
