from .enumeration import Relationship, Repo, Scope
from .atomic import Unit
from box import Box

m=Box()

m.dotfile_manager=Box(
    # stow=Box(repo=Repo.AOR),
    # chemzmoi=Box(repo=Repo.AOR),
)

m.window_compositor=Box(
    # niri=Box(repo=Repo.AOR),
    # river=Box(repo=Repo.AOR),
    # mangowc=Box(repo=Repo.AOR),
    hyprland=Box(
        repo=Repo.AOR,
        single_user_config=[
            "~/.config/hypr/hyprland",
            "~/.config/hypr/hyprland.conf",
        ]
    )
)

m.session_manager.relationship=Relationship.ASSOCIATED
m.session_manager=Box(
    app2unit=Box(repo=Repo.AOR),
    uwsm=Box(
        repo=Repo.AOR,
        single_user_config=["~./config/uwsm"],
        supporters=Box(libnewt=Box(repo=Repo.AOR))
    )
)

m.display_manager.sddm=Box(repo=Repo.AOR, units=[Unit("sddm.service", Scope.MULTI_USER)])

m.screen_share.relationship=Relationship.ASSOCIATED
m.screen_share=Box(
    xdg_desktop_portal_gtk=Box(repo=Repo.AOR),
    xdg_desktop_portal_hyprland=Box(repo=Repo.AOR)
)

m.bar=Box(
    waybar=Box(
        repo=Repo.AOR,
        units=[Unit("waybar.service", Scope.SINGLE_USER)],
        single_user_config=["~/.config/waybar"]
    ),
    # eww=Box(repo=Repo.AOR),
    # ags=Box(repo=Repo.AOR),
    # hyprpanel=Box(repo=Repo.AOR),
    # quickshell=Box(repo=Repo.AOR),
)

m.color_extractor=Box(
    # pywall=Box(repo=Repo.AOR),
    # wallust=Box(repo=Repo.AOR),
    # hellwal=Box(repo=Repo.AOR),
    matugen=Box(repo=Repo.AOR, single_user_config=["~/.config/matugen"]),
    # python_colorthief=Box(repo=Repo.AOR),
    # kde_material_you_colors=Box(repo=Repo.AOR),
)
m.qt_theme.relationship=Relationship.ASSOCIATED
m.qt_theme=Box(
    qt5ct=Box(repo=Repo.AOR, single_user_config=["~/.config/qt5ct"]),
    qt6ct=Box(repo=Repo.AOR, single_user_config=["~/.config/qt6ct"]),
    hyprqt6engine=Box(repo=Repo.AOR),
    kvantum=Box(repo=Repo.AOR, single_user_config=["~/.config/Kvantum"]),
)

m.gtk_theme.relationship=Relationship.ASSOCIATED
m.gtk_theme=Box(
    gtk=Box(
        single_user_config=[
            "~/.config/gtk-3.0",
            "~/.config/gtk-4.0"
        ]
    ),
    nwg_look=Box(repo=Repo.AOR, single_user_config=["~/.config/nwg-look"]),
    orchis_theme=Box(
        repo=Repo.AOR,
        supporters=Box(
            vimix_cursors=Box(repo=Repo.AOR),
            tela_circle_icon_theme=Box(repo=Repo.AOR),
        ),
    ),
    gnome_themes_extra=Box(repo=Repo.AOR),
)

m.wallpaper.setter=Box(
    # swww=Box(repo=Repo.AOR),
    # swaybg=Box(repo=Repo.AOR),
    # awww_bin=Box(repo=Repo.AUR),
    # mpvpaper=Box(repo=Repo.AUR),
    hyprpaper=Box(
        repo=Repo.AOR,
        units=[Unit("hyprpaper.service", Scope.SINGLE_USER)],
        single_user_config=["~/.config/hypr/hyprpaper.conf"]
    )
)

m.wallpaper.picker=Box(
    rofi=Box(repo=Repo.AOR, single_user_config=["~/.config/rofi"]),
    # waypaper=Box(repo=Repo.AUR),
    # waytrogen_bin=Box(repo=Repo.AUR),
)

m.screen_lock.hyprlock=Box(repo=Repo.AOR, single_user_config=["~/.config/hypr/hyprlock.conf"])
m.polkit.hyprpolkitagent=Box(repo=Repo.AOR, units=[Unit("hyprpolkitagent.service", Scope.SINGLE_USER)])
m.idle.hypridle=Box(
    repo=Repo.AOR,
    units=[Unit("hypridle.service", Scope.SINGLE_USER)],
    single_user_config=["~/.config/hypr/hypridle.conf"]
)
m.backlight.hyprsunset=Box(
    repo=Repo.AOR,
    units=[Unit("hyprsunset.service", Scope.SINGLE_USER)],
    single_user_config=["~/.config/hypr/hyprsunset.conf"]
)

m.launcher=Box(
    fuzzel=Box(repo=Repo.AOR, single_user_config=["~/.config/fuzzel"]),
    hyprlauncher=Box(repo=Repo.AOR, single_user_config=["~/.config/hypr/hyprlauncher.conf"]),
)

m.notification=Box(
    # fnott=Box(repo=Repo.AOR),
    # dunst=Box(repo=Repo.AOR, single_user_config=["~/.config/dunst"]),
    # mako=Box(repo=Repo.AOR, units=[Unit("mako.service", Scope.SINGLE_USER)], single_user_config=["~/.config/mako"]),
    swaync=Box(repo=Repo.AOR, units=[Unit("swaync.service", Scope.SINGLE_USER)], single_user_config=["~/.config/swaync"]),
)

m.clipboard.copy_paste.wl_clipboard=Box(repo=Repo.AOR)
m.clipboard.history=Box(
    # copyq=Box(repo=Repo.AOR),
    cliphist=Box(repo=Repo.AOR),
    # nwg_clipman=Box(repo=Repo.AOR),
    # wl_clllip_persist=Box(repo=Repo.AOR),
)

m.input.method.fcitx5=Box(
    repo=Repo.AOR,
    single_user_config=[
        "~/.config/fcitx5/config"
        "~/.config/fcitx5/profile"
    ],
    supporters=Box(
        fcitx5_unikey=Box(repo=Repo.AOR),
        fcitx5_configtool=Box(repo=Repo.AOR)
    )
)
m.input.remapper=Box(
    kanata_bin=Box(repo=Repo.AUR, single_user_config=["~/.config/kanata"]),
    # wlr_which_key=Box(repo=Repo.AUR),
    # xremap_hypr_bin=Box(repo=Repo.AUR),
    # xremap_wlroots_bin=Box(repo=Repo.AUR),
)

m.font.noto=Box(
    noto_fonts=Box(repo=Repo.AOR),
    noto_fonts_cjk=Box(repo=Repo.AOR),
    noto_fonts_emoji=Box(repo=Repo.AOR),
)
m.font.ttf=Box(
    ttf_opensans=Box(repo=Repo.AOR),
    ttf_fira_code=Box(repo=Repo.AOR),
    ttf_cascadia_code_nerd=Box(repo=Repo.AOR),
    ttf_jetbrains_mono_nerd=Box(repo=Repo.AOR),
)
m.font.tex.tex_gyre_fonts=Box(repo=Repo.AOR),

m.shell=Box(
    zsh=Box(repo=Repo.AOR),
    fish=Box(repo=Repo.AOR),
    bash=Box(repo=Repo.AOR, single_user_config=["~/.bashrc", "~/.bash_profile"]),
    nushell=Box(
        repo=Repo.AOR,
        single_user_config=[
            # "~/.config/nushell",
            "~/.config/nushell/config.nu",
            "~/.config/nushell/env.nu",
        ]
    )
)
m.shell.history.atuin=Box(repo=Repo.AOR)
m.shell.prompt.starship=Box(repo=Repo.AOR, single_user_config=["~/.config/starship.toml"])

m.terminal.emulator=Box(
    foot=Box(
        repo=Repo.AOR,
        units=[Unit("foot-server.service", Scope.SINGLE_USER)],
        single_user_config=["~/.config/foot"]
    ),
    wezterm_git=Box(
        repo=Repo.AUR,
        single_user_config=["~/.config/wezterm"]
    ),
    kitty=Box(repo=Repo.AOR, single_user_config=["~/.config/kitty"]),
    aclacritty=Box(repo=Repo.AOR),
    ghostty=Box(repo=Repo.AOR, units=[Unit("app-com.mitchellh.ghostty.service", Scope.SINGLE_USER)]),
)

m.terminal.multiplexer=Box(
    tmux=Box(repo=Repo.AOR, single_user_config=["~/.tmux.conf"]),
    zellij=Box(repo=Repo.AOR),
)

m.file.manager=Box(
    thunar=Box(
        repo=Repo.AOR,
        supporters=Box(
            thunar_volman=Box(repo=Repo.AOR),
            thunar_archive_plugin=Box(repo=Repo.AOR),
            thunar_media_tags_plugin=Box(repo=Repo.AOR),
            # catfish=Box(repo=Repo.AOR),
            # plocate=Box(repo=Repo.AOR),
            # zeitgeist=Box(repo=Repo.AOR),
        )
    ),
    yazi=Box(
        repo=Repo.AOR,
        single_user_config=["~/.config/yazi"],
        supporters={
            "7zip": {"repo": Repo.AOR},
            "chafa": {"repo": Repo.AOR},
            "ffmpeg": {"repo": Repo.AOR},
            "jq": {"repo": Repo.AOR},
            "poppler": {"repo":Repo.AOR},
            "resvg": {"repo":Repo.AOR},
            "imagemagick": {
                "repo": Repo.AOR,
                "supporters": {"libjpeg-turbo": {"repo": Repo.AOR}}
            }
        }
    ),
    superfile=Box(repo=Repo.AOR)
)
m.file.misc=Box(
    xdg_user_dirs=Box(repo=Repo.AOR, units=[Unit("xdg-user-dirs-update.service", Scope.SINGLE_USER)]),
    czkawka_gui_bin=Box(repo=Repo.AUR),
)

m.file.thumnail.tumbler=Box(
    repo=Repo.AOR,
    units=[Unit("tumblerd.service", Scope.SINGLE_USER)],
    supporters=Box(
        ffmpegthumbnailer=Box(repo=Repo.AOR),
        freetype2=Box(repo=Repo.AOR),
        libgepub=Box(repo=Repo.AOR),
        libgsf=Box(Repo.AOR),
        libopenraw=Box(repo=Repo.AOR),
        poppler_glib=Box(repo=Repo.AOR),
        libarchive=Box(repo=Repo.AOR),
        # ueberzugpp=Box(repo=Repo.AOR),
    )
)

m.media.videp=Box(
    mpv=Box(repo=Repo.AOR, single_user_config=["~/.config/mpv"]),
    # vlc=Box(repo=Repo.AOR),
    # clapper=Box(repo=Repo.AOR),
)
m.media.image=Box(
    mpv=Box(repo=Repo.AOR, single_user_config=["~/.config/mpv"]),
    imv=Box(repo=Repo.AOR),
    feh=Box(repo=Repo.AOR),
    gthumb=Box(repo=Repo.AOR),
    swayimg=Box(repo=Repo.AOR),
)

m.screen.capture=Box(
    # grim=Box(repo=Repo.AOR),
    # flameshot=Box(Repo.AOR),
    hyprshot=Box(repo=Repo.AOR, supporters=Box(hyprpicker=Box(repo=Repo.AOR)))
)
m.screen.crop.slurp=Box(repo=Repo.AOR)
m.screen.annotate=Box(
    swappy=Box(repo=Repo.AOR),
    satty=Box(repo=Repo.AOR),
)

m.screen.record=Box(
    wl_screenrec=Box(repo=Repo.AUR),
    obs_studio=Box(repo=Repo.AOR),
    wf_recorder=Box(repo=Repo.AOR),
    gpu_screen_recorder=Box(repo=Repo.AOR, supporters=Box(gpu_screen_recorder_ui=Box(repo=Repo.AOR)))
)

m.browser.gui=Box(
    firefox=Box(repo=Repo.AOR, supporters=Box(speech_dispatcher=Box(repo=Repo.AOR))),
    brave_bin=Box(repo=Repo.AUR),
    zen_browser_bin=Box(repo=Repo.AUR),
    google_chrome_bin=Box(repo=Repo.AUR, single_user_config=["~/.config/chrome-flags.conf"]),
    helium_browser_bin=Box(repo=Repo.AUR, single_user_config=["~/.config/helium-flags.conf"]),
    thorium_browser_bin=Box(repo=Repo.AUR, single_user_config=["~/.config/thorium-flags.conf"]),
    microsoft_edge_stable_bin=Box(repo=Repo.AUR),
)
m.browser.keyboard_driven=Box(
    browsh=Box(repo=Repo.AUR),
    nyxt=Box(repo=Repo.AOR),
    lynx=Box(repo=Repo.AOR),
    luakit=Box(repo=Repo.AOR),
)

m.misc=Box(
    hugo=Box(repo=Repo.AOR),
    anki_bin=Box(repo=Repo.AUR),
    okular=Box(repo=Repo.AOR),
    mediawriter=Box(repo=Repo.AOR),
    cava=Box(repo=Repo.AOR, single_user_config=["~/.config/cava"]),
    electron=Box(repo=Repo.AOR, single_user_config=["~/.config/electron-flags.conf"]),
    #TODO: this recipes need extension too, how to write
    python_pywalfox=Box(repo=Repo.AUR)
)
