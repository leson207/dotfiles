from src.schema.enumeration import Repo, Scope
from src.schema.atomic import Unit, PackageRecipe, TopicRecipe


map = {}

map["window-compositor"]=TopicRecipe(
    name="window-compositor",
    recipes=[
        PackageRecipe("hyprland", Repo.OFFICIAL),
        # PackageRecipe("river", Repo.OFFICIAL),
        # PackageRecipe("niri", Repo.OFFICIAL),
        # PackageRecipe("mangowc", Repo.OFFICIAL)
    ]
)

TopicRecipe(
    name="session-manager",
    recipes=[PackageRecipe("uwsm", Repo.OFFICIAL, supporters=[PackageRecipe("libnewt", Repo.OFFICIAL)])]
)

TopicRecipe(
    name="app-manager",
    recipes=[
        PackageRecipe("app2unit", Repo.AUR),
        PackageRecipe("uwsm", Repo.OFFICIAL, supporters=[PackageRecipe("libnewt", Repo.OFFICIAL)])
    ]
)

# TopicRecipe(
#     name="session-manager",
#     recipes=[
#         PackageRecipe("uwsm", Repo.OFFICIAL, supporters=[PackageRecipe("libnewt", Repo.OFFICIAL)]),
#         TopicRecipe(
#             name="app-launcher",
#             recipes=[PackageRecipe("app2unit", Repo.AUR)]
#         )
#     ]
# )

TopicRecipe(
    name="display-manager",
    recipes=[
        PackageRecipe(
            name="sddm",
            repo=Repo.OFFICIAL,
            units=[Unit("sddm.service", Scope.MULTI_USER)]
        )
    ]
)

TopicRecipe(
    name="xgd-dirs",
    recipes=[
        PackageRecipe("xdg-user-dirs", Repo.OFFICIAL, units=[Unit("xdg-user-dirs-update.service", Scope.SINGLE_USER)]),
    ]
)

TopicRecipe(
    name="screen-share",
    recipes=[
        PackageRecipe("xdg-desktop-portal", Repo.OFFICIAL),
        PackageRecipe("xdg-desktop-portal-gtk", Repo.OFFICIAL),
        PackageRecipe("xdg-desktop-portal-hyprland", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="bar",
    recipes=[
        PackageRecipe("waybar", Repo.OFFICIAL, units=[Unit("waybar.service", Scope.SINGLE_USER)]),
        # PackageRecipe("eww", Repo.UNKNOWN),
        # PackageRecipe("ags", Repo.UNKNOWN),
        # PackageRecipe("quickshell", Repo.UNKNOWN),
        # PackageRecipe("hyprpanel", Repo.UNKNOWN),
    ]
)

TopicRecipe(
    name="color-extractor",
    recipes=[
        # PackageRecipe("wallust", Repo.AUR),
        PackageRecipe("matugen", Repo.OFFICIAL),
        # PackageRecipe("hellwal", Repo.AUR),
        # PackageRecipe("python-colorthief", Repo.OFFICIAL),
        # PackageRecipe("kde-material-you-colors", Repo.AUR),
    ]
)

TopicRecipe(
    name="qt-config",
    recipes=[
        PackageRecipe("qt5ct", Repo.OFFICIAL),
        PackageRecipe("qt6ct", Repo.OFFICIAL),
        PackageRecipe("hyprqt6engine", Repo.AUR),
    ]
)

TopicRecipe(
    name="qt-theme-engine",
    recipes=[
        PackageRecipe("kvantum", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="gtk-theming",
    TopicRecipe=[
        PackageRecipe("nwglook", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="wallpaper",
    recipes=[
        TopicRecipe(
            name="setter",
            recipes=[
                # PackageRecipe("swww", Repo.OFFICIAL),
                # PackageRecipe("awww-bin", Repo.AUR),
                # PackageRecipe("swaybg", Repo.OFFICIAL),
                # PackageRecipe("mpvpaper", Repo.AUR),
                PackageRecipe("hyprpaper", Repo.OFFICIAL, units=[Unit("hyprpaper.service", Scope.SINGLE_USER)]),
            ]
        ),
        TopicRecipe(
            name="picker",
            recipes=[
                PackageRecipe("rofi", Repo.OFFICIAL),
                # PackageRecipe("waypaper", Repo.AUR),
                # PackageRecipe("waytrogen-bin", Repo.AUR),
            ]
        ),
        TopicRecipe(
            name="misc",
            recipes=[PackageRecipe("wallutils", Repo.OFFICIAL)]
        )
    ]
)

TopicRecipe(
    name="desktop-component",
    recipes=[
        TopicRecipe(
            name="screen-lock",
            recipes=[
                PackageRecipe("hyprlock", Repo.OFFICIAL),
                # PackageRecipe("quickshell", Repo.OFFICIAL),
            ]
        ),
        TopicRecipe(
            name="polkit",
            recipes=[PackageRecipe("hyprpolkitagent", Repo.OFFICIAL, units=[Unit("hyprpolkitagent.service", Scope.SINGLE_USER)])]
        ),
        TopicRecipe(
            name="idle",
            recipes=[PackageRecipe("hypridle", Repo.OFFICIAL, units=[Unit("hypridle.service", Scope.SINGLE_USER)])]
        ),
        TopicRecipe(
            name="backlight",
            recipes=[PackageRecipe("hyprsunset", Repo.OFFICIAL, units=[Unit("hyprsunset.service", Scope.SINGLE_USER)])]
        )
    ]
)

TopicRecipe(
    name="launcher",
    recipes=[
        PackageRecipe("fuzzel", Repo.OFFICIAL),
        PackageRecipe("hyprlauncher", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="notification",
    recipes=[
        # PackageRecipe("dunst", Repo.OFFICIAL),
        # PackageRecipe("fnott", Repo.OFFICIAL),
        # PackageRecipe("mako", Repo.OFFICIAL, units=[Unit("mako.service", Scope.SINGLE_USER)]),
        PackageRecipe("swaync", Repo.OFFICIAL, units=[Unit("swaync.service", Scope.SINGLE_USER)]),
    ]
)

TopicRecipe(
    name="video-player",
    recipes=[
        PackageRecipe("mpv", Repo.OFFICIAL),
        PackageRecipe("vlc", Repo.OFFICIAL),
        # PackageRecipe("clapper", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="image-viewer",
    recipes=[
        PackageRecipe("mpv", Repo.OFFICIAL),
        # PackageRecipe("imv", Repo.OFFICIAL),
        # PackageRecipe("feh", Repo.OFFICIAL),
        # PackageRecipe("gthumb", Repo.OFFICIAL),
        # PackageRecipe("swayimg", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="screen-shot",
    recipes=[
        # TopicRecipe(
        #     name="shot",
        #     recipes=[
        #         PackageRecipe("grim", Repo.OFFICIAL)
        #     ]
        # ),
        # TopicRecipe(
        #     name="crop",
        #     recipes=[
        #         PackageRecipe("slurp", Repo.OFFICIAL)
        #     ]
        # ),
        # TopicRecipe(
        #     name="edit",
        #     recipes=[
        #         PackageRecipe("swappy", Repo.OFFICIAL),
        #         PackageRecipe("satty", Repo.OFFICIAL)
        #     ]
        # ),
        TopicRecipe(
            name="full",
            recipes=[
                PackageRecipe("hyprshot", Repo.OFFICIAL, supporters=[PackageRecipe("hyprpicker", Repo.OFFICIAL)]),
                # PackageRecipe("flameshot", Repo.OFFICIAL),
            ]
        )
    ]
)

TopicRecipe(
    name="screen-recorder",
    recipes=[
        PackageRecipe("wl-screenrec", Repo.AUR),
        PackageRecipe("obs-studio", Repo.OFFICIAL),
        PackageRecipe("wf-recorder", Repo.OFFICIAL),
        PackageRecipe("gpu-screen-recorder", Repo.AUR, supporters=[PackageRecipe("gpu-screen-recorder-ui", Repo.AUR)]),
    ]
)

TopicRecipe(
    name="clipboard",
    recipes=[
        TopicRecipe(
            name="copy-paste",
            recipes=[PackageRecipe("wl-clipboard", Repo.OFFICIAL)]
        ),
        TopicRecipe(
            name="history",
            recipes=[
                # PackageRecipe("copyq", Repo.OFFICIAL),
                PackageRecipe("cliphist", Repo.OFFICIAL),
                # PackageRecipe("nwg-clipman", Repo.OFFICIAL),
                # PackageRecipe("wl-clip-persist", Repo.OFFICIAL),
            ]
        )
    ]
)

TopicRecipe(
    name="input",
    recipes=[
        TopicRecipe(
            name="input-method",
            recipes=[
                PackageRecipe(
                    name="fcitx5",
                    repo=Repo.OFFICIAL,
                    supporters=[
                        PackageRecipe("fcitx5-unikey", Repo.OFFICIAL),
                        PackageRecipe("fcitx5-configtool", Repo.OFFICIAL),
                    ]
                )
            ]
        ),
        TopicRecipe(
            name="keyboard-remapper",
            recipes=[
                PackageRecipe(name="katana-bin", repo=Repo.AUR),
                # PackageRecipe(name="wlr-which-key", repo=Repo.AUR)
                # PackageRecipe(name="xremap-hypr-bin", repo=Repo.AUR)
                # PackageRecipe(name="xremap-wlroots-bin", repo=Repo.AUR)
            ]
        )
    ]
)

TopicRecipe(
    name="font",
    recipes=[
        TopicRecipe(
            name="noto-fonts",
            recipes=[
                PackageRecipe("noto-fonts", Repo.OFFICIAL),
                PackageRecipe("noto-fonts-cjk", Repo.OFFICIAL),
                PackageRecipe("noto-fonts-emoji", Repo.OFFICIAL)
            ]
        ),
        TopicRecipe(
            name="ttf",
            recipes=[
                PackageRecipe("ttf-opensans", Repo.OFFICIAL),
                PackageRecipe("ttf-fira-code", Repo.OFFICIAL),
                PackageRecipe("ttf-cascadia-code-nerd", Repo.OFFICIAL),
                PackageRecipe("ttf-jetbrains-mono-nerd", Repo.OFFICIAL)
            ]
        ),
        TopicRecipe(
            name="tex-gyre",
            recipes=[PackageRecipe("tex-gyre-fonts", Repo.OFFICIAL)]
        )
    ]
)

TopicRecipe(
    name="terminal",
    recipes=[
        PackageRecipe("foot", Repo.OFFICIAL, units=[Unit("foot-server.service", Scope.SINGLE_USER)]),
        PackageRecipe("ghostty", Repo.OFFICIAL, units=[Unit("app-com.mitchellh.ghostty.service", Scope.SINGLE_USER)]),
        PackageRecipe("kitty", Repo.OFFICIAL),
        PackageRecipe("aclacritty", Repo.OFFICIAL),
        PackageRecipe("wezterm-git", Repo.AUR),
    ]
)

TopicRecipe(
    name="terminal-multiplexer",
    recipes=[
        PackageRecipe("tmux", Repo.OFFICIAL),
        PackageRecipe("zellij", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="shell",
    recipes=[
        # PackageRecipe("zsh", Repo.OFFICIAL),
        # PackageRecipe("fish", Repo.OFFICIAL),
        PackageRecipe("nushell", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="shell-history",
    recipes=[PackageRecipe("atuin", Repo.OFFICIAL)]
)

TopicRecipe(
    name="shell-promt",
    recipes=[PackageRecipe("atuin", Repo.OFFICIAL)]
)

# TopicRecipe(
#     name="secret",
#     recipes=[
#         PackageRecipe("seahorse", Repo.OFFICIAL, supporters=[PackageRecipe("gnome-keyring", Repo.OFFICIAL)]),
#         PackageRecipe("bitwardern", Repo.OFFICIAL, supporters=[PackageRecipe("gnome-keyring", Repo.OFFICIAL)]),
#     ]
# )

TopicRecipe(
    name="file",
    recipes=[
        TopicRecipe(
            name="manager",
            recipes=[
                PackageRecipe(
                    name="thunar",
                    repo=Repo.OFFICIAL,
                    supporters=[
                        PackageRecipe("thunar-volman", Repo.OFFICIAL),
                        PackageRecipe("thunar-archive-plugin", Repo.OFFICIAL),
                        PackageRecipe("thunar-media-tags-plugin", Repo.OFFICIAL),
                        # PackageRecipe("catfish", Repo.OFFICIAL),
                        # PackageRecipe("plocate", Repo.OFFICIAL),
                        # PackageRecipe("zeitgeist", Repo.OFFICIAL),
                    ]
                ),
                PackageRecipe(
                    name="yazi",
                    repo=Repo.OFFICIAL,
                    supporters=[
                        PackageRecipe("7zip", Repo.OFFICIAL),
                        PackageRecipe("chafa", Repo.OFFICIAL),
                        PackageRecipe("ffmpeg", Repo.OFFICIAL),
                        PackageRecipe("jq", Repo.OFFICIAL),
                        PackageRecipe("poppler", Repo.OFFICIAL),
                        PackageRecipe("resvg", Repo.OFFICIAL),
                        PackageRecipe(
                            name="imagemagick",
                            repo=Repo.OFFICIAL,
                            supporters=[PackageRecipe("libjpeg-turbo", Repo.OFFICIAL)]
                        )
                    ]
                ),
                PackageRecipe("superfile", Repo.OFFICIAL)
            ]
        ),
        TopicRecipe(
            name="backup",
            recipes=[
                PackageRecipe("borg", Repo.OFFICIAL),
                PackageRecipe("restic", Repo.OFFICIAL),
                PackageRecipe("timeshift", Repo.OFFICIAL),
            ]
        ),
        TopicRecipe(
            name="misc",
            recipes=[
                PackageRecipe("fd", Repo.OFFICIAL),
                PackageRecipe("fzf", Repo.OFFICIAL),
                PackageRecipe("bat", Repo.OFFICIAL),
                PackageRecipe("eza", Repo.OFFICIAL),
                PackageRecipe("zoxide", Repo.OFFICIAL),
                PackageRecipe("ripgrep", Repo.OFFICIAL),
                PackageRecipe("rsync", Repo.OFFICIAL),

                PackageRecipe("7zip", Repo.OFFICIAL),
                PackageRecipe("czkawka-gui-bin", Repo.AUR),
            ]
        )
    ]
)

TopicRecipe(
    name="thumnail",
    recipes=[
        PackageRecipe(
            name="tumbler",
            repo=Repo.OFFICIAL,
            units=[Unit("tumblerd.service", Scope.SINGLE_USER)],
            supporters=[
                PackageRecipe("ffmpegthumbnailer", Repo.OFFICIAL),
                PackageRecipe("freetype2", Repo.OFFICIAL),
                PackageRecipe("libgepub", Repo.OFFICIAL),
                PackageRecipe("libgsf", Repo.OFFICIAL),
                PackageRecipe("libopenraw", Repo.OFFICIAL),
                PackageRecipe("poppler-glib", Repo.OFFICIAL),
                PackageRecipe("libarchive", Repo.OFFICIAL),

                # PackageRecipe("ueberzugpp", Repo.OFFICIAL),
            ]
        )
    ]
)


# TopicRecipe(
#     name="package-manager",
#     recipes=[
#         PackageRecipe("nix", Repo.OFFICIAL),
#         PackageRecipe("guix", Repo.AUR),
#     ]
# )

TopicRecipe(
    name="dotfile-manager",
    recipes=[
        PackageRecipe("stow", Repo.OFFICIAL),
        # PackageRecipe("chemzmoi", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="browser",
    recipes=[
        TopicRecipe(
            name="gui",
            recipes=[
                PackageRecipe("firefox", Repo.OFFICIAL, supporters=[PackageRecipe("speech-dispatcher", Repo.OFFICIAL)]),
                PackageRecipe("brave-bin", Repo.AUR),
                PackageRecipe("zen-browser-bin", Repo.AUR),
                PackageRecipe("google-chrome-bin", Repo.AUR),
                PackageRecipe("helium-browser-bin", Repo.AUR),
                PackageRecipe("thorium-browser-bin", Repo.AUR),
                PackageRecipe("microsoft-edge-stable-bin", Repo.AUR)
            ]
        ),
        TopicRecipe(
            name="keyboard-driven",
            recipes=[
                PackageRecipe("nyxt", Repo.OFFICIAL),
                PackageRecipe("luakit", Repo.OFFICIAL),
                PackageRecipe("lynx", Repo.OFFICIAL),
                PackageRecipe("browsh", Repo.AUR),
            ]
        )
    ]
)

TopicRecipe(
    name="social",
    recipes=[
        TopicRecipe(
            name="telegram",
            recipes=[
                PackageRecipe("telegram-desktop", Repo.OFFICIAL),
            ]
        ),
        TopicRecipe(
            name="discord",
            recipes=[PackageRecipe("vesktop-bin", Repo.AUR)]
        ),
        TopicRecipe(
            name="matrix",
            recipes=[
                PackageRecipe("fractal", Repo.OFFICIAL),
                PackageRecipe("fluffychat-bin", Repo.AUR),
            ]
        ),
    ]
)


TopicRecipe(
    name="ai",
    recipes=[
        # PackageRecipe("aider-chat", Repo.AUR),
        PackageRecipe("gemini-cli", Repo.OFFICIAL),
        PackageRecipe("openai-codex", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="utils",
    recipes=[
        PackageRecipe("okular", Repo.OFFICIAL),
        PackageRecipe("mediawriter", Repo.OFFICIAL),
        PackageRecipe("anki-bin", Repo.AUR),
        PackageRecipe("hugo", Repo.AUR),
        PackageRecipe("tree", Repo.AUR),
        PackageRecipe("aria2", Repo.AUR),
        PackageRecipe("dust", Repo.AUR),
        PackageRecipe("dua-cli", Repo.AUR),
        PackageRecipe("progress", Repo.AUR),
        PackageRecipe("fastfetch", Repo.AUR),
    ]
)

TopicRecipe(
    name="monitor",
    recipes=[
        PackageRecipe("atop", Repo.OFFICIAL),
        PackageRecipe("btop", Repo.OFFICIAL),
        PackageRecipe("htop", Repo.OFFICIAL),
        PackageRecipe("nvtop", Repo.OFFICIAL),
        PackageRecipe("glances", Repo.OFFICIAL),
        PackageRecipe("bottom", Repo.OFFICIAL),
        PackageRecipe("hyperfine", Repo.OFFICIAL),
    ]
)
