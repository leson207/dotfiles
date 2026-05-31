from email.policy import default
from box import Box
from src.enumeration import Repo, Scope, Tag
from src.schema import Unit, PkgSpec, PkgVar, PkgRecipe, UsageRecipe


db = Box(
    sudo=PkgSpec(
        name="sudo",
        repo=Repo.AOR,
        tags=[Tag.AUTHENTICATOR],
        configs=Box(default=["/etc/sudoers.d/10-foo"])
    ),
    glibc=PkgSpec(
        name="glibc",
        repo=Repo.AOR,
        tags=[Tag.C_LIBRARY, Tag.ARCH_PREINSTALLED],
    ),
    systemd=PkgSpec(
        name="systemd",
        repo=Repo.AOR,
        tags=[Tag.SERVICE_MANAGER, Tag.ARCH_PREINSTALLED, Tag.BOOT_LOADER],
        configs=Box(default=["~/.config/systemd"]),
        units=Box(systemd_timesyncd_service=Unit(name="systemd-timesyncd.service", scope=Scope.MULTI_USER))
    ),
    linux=PkgSpec(
        name="linux",
        repo=Repo.AOR,
        tags=[Tag.KERNEL],
    ),
    linux_cachyos_bore=PkgSpec(
        name="linux-cachyos-bore",
        repo=Repo.AUR,
        tags=[Tag.KERNEL],
    ),
    linux_headers=PkgSpec(
        name="linux-headers",
        repo=Repo.AOR,
        tags=[Tag.HEADERS],
    ),
    linux_cachyos_bore_headers=PkgSpec(
        name="linux-cachyos-bore-headers",
        repo=Repo.AUR,
        tags=[Tag.HEADERS],
    ),
    linux_firmware=PkgSpec(
        name="linux-firmware",
        repo=Repo.AOR,
        tags=[Tag.FIRMWARE],
    ),
    intel_ucode=PkgSpec(
        name="intel-ucode",
        repo=Repo.AOR,
        tags=[Tag.MICROCODE],
    ),
    
    efibootmgr=PkgSpec(
        name="efibootmgr",
        repo=Repo.AOR,
        tags=[Tag.BOOT_MANAGER],
    ),

    # base=PkgSpec(
    #     name="base",
    #     repo=Repo.AOR,
    #     tags=[Tag.USERLAND, Tag.ARCH_PREINSTALLED]
    # ),
    # base_devel=PkgSpec(
    #     name="base-devel",
    #     repo=Repo.AOR,
    #     tags=[Tag.USERLAND]
    # ),
    # coreutils=PkgSpec(
    #     name="coreutils",
    #     repo=Repo.AOR,
    #     tags=[Tag.USERLAND, Tag.COREUTILS, Tag.ARCH_PREINSTALLED]
    # ),

    git=PkgSpec(
        name="git",
        repo=Repo.AOR,
        tags=[Tag.VERSION_CONTROL_SYSTEM]
    ),
    delta=PkgSpec(
        name="git-delta",
        repo=Repo.AOR,
        tags=[Tag.SYNTAX_HIGHLIGHTING]
    ),
    less=PkgSpec(
        name="less",
        repo=Repo.AOR,
        tags=[Tag.TEXT_VIEWER, Tag.TUI]
    ),

    nix=PkgSpec(
        name="nix",
        repo=Repo.AOR,
        tags=[Tag.SYSTEM_PACKAGE_MANAGER]
    ),
    pacman=PkgSpec(
        name="pacman",
        repo=Repo.AOR,
        tags=[Tag.SYSTEM_PACKAGE_MANAGER],
    ),
    yay=PkgSpec(
        name="yay",
        repo=Repo.GITHUB,
        tags=[Tag.SYSTEM_PACKAGE_MANAGER],
    ),
    paru=PkgSpec(
        name="paru",
        repo=Repo.GITHUB,
        tags=[Tag.SYSTEM_PACKAGE_MANAGER],
    ),
    reflector=PkgSpec(
        name="reflector",
        repo=Repo.AOR,
        tags=[Tag.MIRROR_FILTER],
        units=Box(reflector_timer=Unit(name="reflector.timer", scope=Scope.MULTI_USER))
    ),

    mesa=PkgSpec(
        name="mesa",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC,]
    ),
    mesa_utils=PkgSpec(
        name="mesa-utils",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.MESA]
    ),
    libva=PkgSpec(
        name="libva",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.LIBVA]
    ),
    libva_utils=PkgSpec(
        name="libva-utils",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.LIBVA]
    ),
    # vulkan_mesa_implicit_layers=PkgSpec(
    #     name="vulkan-mesa-implicit-layers",
    #     repo=Repo.AOR,
    #     tags=[Tag.GRAPHIC, Tag.VULKAN, Tag.MESA]
    # ),
    vulkan_intel=PkgSpec(
        name="vulkan-intel",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.VULKAN, Tag.INTEL]
    ),
    # libva_intel_driver=PkgSpec(
    #     name="libva-intel-driver",
    #     repo=Repo.AOR,
    #     tags=[Tag.GRAPHIC, Tag.LIBVA, Tag.INTEL]
    # ),
    intel_media_diriver=PkgSpec(
        name="intel-media-driver",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.INTEL]
    ),
    vulkan_radeon_driver=PkgSpec(
        name="vulkan-radeon-driver",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.VULKAN, Tag.AMD]
    ),

    pipewire=PkgSpec(
        name="pipewire",
        repo=Repo.AOR,
        tags=[Tag.AUDIO, Tag.PIPEWIRE],
        units=Box(pipewire=Unit(name="pipewire.service", scope=Scope.SINGLE_USER)),
    ),
    wireplumber=PkgSpec(
        name="wireplumber",
        repo=Repo.AOR,
        tags=[Tag.AUDIO, Tag.PIPEWIRE],
        units=Box(pipewire=Unit(name="wireplumber.service", scope=Scope.SINGLE_USER)),
    ),
    pipewire_pulse=PkgSpec(
        name="pipewire-pulse",
        repo=Repo.AOR,
        tags=[Tag.AUDIO, Tag.PIPEWIRE],
        units=Box(pipewire=Unit(name="pipewire-pulse.service", scope=Scope.SINGLE_USER)),
    ),
    # pipewire_audio=PkgSpec(
    #     name="pipewire-audio",
    #     repo=Repo.AOR,
    #     tags=[Tag.AUDIO, Tag.PIPEWIRE],
    # ),
    pipewire_alsa=PkgSpec(
        name="pipewire-alsa",
        repo=Repo.AOR,
        tags=[Tag.AUDIO, Tag.PIPEWIRE],
    ),

    iwd=PkgSpec(
        name="iwd",
        repo=Repo.AOR,
        tags=[Tag.INTERNET],
        units=Box(iwd=Unit(name="iwd.service", scope=Scope.MULTI_USER)),
    ),
    networkmanager=PkgSpec(
        name="networkmanager",
        repo=Repo.AOR,
        tags=[Tag.INTERNET],
        units=Box(iwd=Unit(name="NetworkManager.service", scope=Scope.MULTI_USER)),
    ),
    openssh=PkgSpec(
        name="openssh",
        repo=Repo.AOR,
        tags=[Tag.SSH],
        units=Box(
            sshd=Unit(name="sshd.service", scope=Scope.MULTI_USER),
            sshdgenkeys=Unit(name="sshdgenkeys.service", scope=Scope.MULTI_USER),
        ),
    ),

    udisk2=PkgSpec(
        name="udisks2",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.MOUNT],
        units=Box(udisks2=Unit("udisks2.service", scope=Scope.MULTI_USER))
    ),
    udiskie=PkgSpec(
        name="udiskie",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.MOUNT],
        auto_start=[["udiskie"]]
    ),

    e2fsprogs=PkgSpec(
        name="e2fsprogs",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.FILESYSTEM_USERSPACE_UTILITIES]
    ),
    exfatprogs=PkgSpec(
        name="exfatprogs",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.FILESYSTEM_USERSPACE_UTILITIES]
    ),
    ntfsprogs=PkgSpec(
        name="ntfsprogs",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.FILESYSTEM_USERSPACE_UTILITIES]
    ),

    gvfs=PkgSpec(
        name="gvfs",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.GVFS, Tag.VIRTUAL_FILESYSTEM]
    ),
    gvfs_mtp=PkgSpec(
        name="gvfs-mtp",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.GVFS, Tag.VIRTUAL_FILESYSTEM]
    ),
    util_linux=PkgSpec(
        name="util-linux",
        repo=Repo.AOR,
        tags=[Tag.DISK],
        units=Box(fstrim=Unit("fstrim.timer", Scope.MULTI_USER))
    ),

    tlp=PkgSpec(
        name="tlp",
        repo=Repo.AOR,
        tags=[Tag.POWER],
        units=Box(tlp=Unit("tlp.service", Scope.MULTI_USER))
    ),
    tlp_rdw=PkgSpec(
        name="tlp-rdw",
        repo=Repo.AOR,
        tags=[Tag.POWER]
    ),
    # tlp_pd=PkgSpec(
    #     name="tlp-pd",
    #     repo=Repo.AOR,
    #     tags=[Tag.POWER],
    #     units=Box(tlp_Pd=Unit("tlp-pd.service", Scope.MULTI_USER))
    # ),
    thermal=PkgSpec(
        name="thermal",
        repo=Repo.AOR,
        tags=[Tag.PERFORMANCE],
         units=Box(thermal=Unit("thermal.service", Scope.MULTI_USER))
    ),
    irqbalance=PkgSpec(
        name="irqbalance",
        repo=Repo.AOR,
        tags=[Tag.PERFORMANCE],
         units=Box(irqbalance=Unit("irqbalance.service", Scope.MULTI_USER))
    ),
    batsignal=PkgSpec(
        name="batsignal",
        repo=Repo.AOR,
        tags=[Tag.POWER],
         units=Box(batsignal=Unit("batsignal.service", Scope.MULTI_USER))
    ),
    # ananicy_cpp=PkgSpec(
    #     name="ananicy-cpp",
    #     repo=Repo.AOR,
    #     tags=[Tag.PERFORMANCE],
    #      units=Box(ananicy_cpp=Unit("ananicy-cpp.service", Scope.MULTI_USER))
    # ),
    # preload=PkgSpec(
    #     name="preload",
    #     repo=Repo.AOR,
    #     tags=[Tag.PERFORMANCE],
    #      units=Box(preload=Unit("preload.service", Scope.MULTI_USER))
    # ),
    # cpupower=PkgSpec(
    #     name="cpupower",
    #     repo=Repo.AOR,
    #     tags=[Tag.PERFORMANCE],
    #     units=Box(cpupower=Unit("cpupower.service", Scope.MULTI_USER))
    # ),

    noto_fonts=PkgSpec(
        name="noto-fonts",
        repo=Repo.AOR,
        tags=[Tag.FONT, Tag.NOTO],
    ),
    noto_fonts_cjk=PkgSpec(
        name="noto-fonts-cjk",
        repo=Repo.AOR,
        tags=[Tag.FONT, Tag.NOTO],
    ),
    noto_fonts_emoji=PkgSpec(
        name="noto-fonts-emoji",
        repo=Repo.AOR,
        tags=[Tag.FONT, Tag.NOTO],
    ),
    ttf_fira_code=PkgSpec(
        name="ttf-fira-code",
        repo=Repo.AOR,
        tags=[Tag.FONT, Tag.TTF, Tag.MONOSPACE],
    ),
    ttf_fira_code_nerd=PkgSpec(
        name="ttf-fira-code-nerd",
        repo=Repo.AOR,
        tags=[Tag.FONT, Tag.TTF, Tag.MONOSPACE, Tag.NERD_FONT],
    ),
    ttf_jetbrains_mono=PkgSpec(
        name="ttf-jetbrains-mono",
        repo=Repo.AOR,
        tags=[Tag.FONT, Tag.TTF, Tag.MONOSPACE],
    ),
    ttf_jetbrains_mono_nerd=PkgSpec(
        name="ttf-jetbrains-mono-nerd",
        repo=Repo.AOR,
        tags=[Tag.FONT, Tag.TTF, Tag.MONOSPACE, Tag.NERD_FONT],
    ),

    niri=PkgSpec(
        name="niri",
        repo=Repo.AOR,
        tags=[Tag.WINDOW_COMPOSITOR, Tag.WAYLAND],
        configs=Box(default=["~/.config/niri"])
    ),
    xwayland_satelite=PkgSpec(
        name="xwayland_satelite",
        repo=Repo.AOR,
        tags=[Tag.XWAYLAND]
    ),
    
    xdg_desktop_portal_gtk=PkgSpec(
        name="xdg-desktop-portal-gtk",
        repo=Repo.AOR,
        tags=[Tag.XDG, Tag.DESKTOP_PORTAL, Tag.GTK]
    ),
    
    app2unit=PkgSpec(
        name="app2unit",
        repo=Repo.AUR,
        tags=[Tag.APP_MANAGER]
    ),

    fcitx5=PkgSpec(
        name="fcitx5",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.INPUT_METHOD, Tag.FRAMEWORK],
        configs=Box(
            default=[
                "~/.config/fcitx5/config",
                "~/.config/fcitx5/profile"
            ]
        ),
        env_vars=[
            ["QT_IM_MODULE", "fcitx"],
            ["GTK_IM_MODULE", "fcitx"],
            ["XMODIFIERS", "@im=fcitx"],
            ["SDL_IM_MODULE", "fcitx",],
            ["GLFW_IM_MODULE", "fcitx"],
        ],
        # reference={
        #     "https://hi.imnhan.com/fcitx/"
        # }
    ),

    fcitx5_gtk=PkgSpec(
        name="fcitx5-gtk",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.GTK, Tag.IME]
    ),
    fcitx5_qt=PkgSpec(
        name="fcitx5-qt",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.QT, Tag.IME]
    ),
    fcitx5_unikey=PkgSpec(
        name="fcitx5-unikey",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.IME]
    ),
    fcitx5_configtool=PkgSpec(
        name="fcitx5-configtool",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.IME]
    ),

    nushell=PkgSpec(
        name="nushell",
        repo=Repo.AOR,
        tags=[Tag.SHELL],
        configs=Box(default=[
            "~/.config/nushell/env.nu",
            "~/.config/nushell/config.nu",
        ])
    ),
    atuin=PkgSpec(
        name="atuin",
        repo=Repo.AOR,
        tags=[Tag.SHELL_HISTORY],
        auto_start=[["atuin", "daemon", "start"]],
    ),
    starship=PkgSpec(
        name="starship",
        repo=Repo.AOR,
        tags=[Tag.SHELL_PROMPT],
    ),

    foot=PkgSpec(
        name="foot",
        repo=Repo.AOR,
        tags=[Tag.TERMINAL_EMULATOR],
        configs=Box(default=["~/.config/foot"]),
        auto_start=[["foot", "--server"]]
    ),
    tmux=PkgSpec(
        name="tmux",
        repo=Repo.AOR,
        tags=[Tag.TERMINAL_MULTIPLEXER],
        configs=Box(default=["~/.tmux.conf"])
    ),

    firefox=PkgSpec(
        name="firefox",
        repo=Repo.AOR,
        tags=[Tag.BROWSER, Tag.FIREFOX]
    ),
    zen_browser_bin=PkgSpec(
        name="zen-browser-bin",
        repo=Repo.AUR,
        tags=[Tag.BROWSER, Tag.FIREFOX]
    ),
    brave_bin=PkgSpec(
        name="brave-bin",
        repo=Repo.AUR,
        tags=[Tag.BROWSER, Tag.CHROMIUM],
        configs=Box(default=["~/.config/brave-flags.conf"])
    ),
    helium_browser_bin=PkgSpec(
        name="helium-browser-bin",
        repo=Repo.AUR,
        tags=[Tag.BROWSER, Tag.CHROMIUM],
    ),

    fuzzel=PkgSpec(
        name="fuzzel",
        repo=Repo.AOR,
        tags=[Tag.APP_LAUNCHER],
        configs=Box(default=["~/.config/fuzzel"])
    ),

    make=PkgSpec(
        name="make",
        repo=Repo.AOR,
        tags=[Tag.BUILD_SYSTEM, Tag.CXX, Tag.GNU]
    ),
    gcc=PkgSpec(
        name="gcc",
        repo=Repo.AOR,
        tags=[Tag.COMPILER, Tag.CXX, Tag.GNU]
    ),
    ccache=PkgSpec(
        name="ccache",
        repo=Repo.AOR,
        tags=[Tag.COMPILER_CACHE, Tag.CXX]
    ),
    mold=PkgSpec(
        name="mold",
        repo=Repo.AOR,
        tags=[Tag.LINKER, Tag.CXX]
    ),
    gdb=PkgSpec(
        name="gdb",
        repo=Repo.AOR,
        tags=[Tag.DEBUGGER, Tag.CXX]
    ),
    uv=PkgSpec(
        name="uv",
        repo=Repo.AOR,
        tags=[Tag.PYTHON_PACKAGE_MANAGER, Tag.PYTHON]
    ),

    neovim=PkgSpec(
        name="neovim",
        repo=Repo.AOR,
        tags=[Tag.TEXT_EDITOR, Tag.TUI, Tag.KEYBOARD_DRIVEN],
        configs=Box(default=["~/.config/lazyvim"])
    ),
    emacs_wayland=PkgSpec(
        name="emacs-wayland",
        repo=Repo.AOR,
        tags=[Tag.TEXT_EDITOR, Tag.TUI, Tag.GUI, Tag.KEYBOARD_DRIVEN, Tag.GNU, Tag.EMACS],
        units=Box(emacs=Unit("emacs.service", Scope.SINGLE_USER)),
        configs=Box(default=["~/.config/doom"])
    ),

    btop=PkgSpec(
        name="btop",
        repo=Repo.AOR,
        tags=[Tag.MONITOR, Tag.TUI],
        configs=Box(default=["~/.config/btop"])
    ),

    gpu_screen_recorder=PkgSpec(
        name="gpu-screen-recorder",
        repo=Repo.AOR,
        tags=[Tag.SCREEN_RECORDER],
        units=Box(gpu_screen_recorder=Unit("gpu-screen-recorder.service", Scope.SINGLE_USER))
    ),
    gpu_screen_recorder_ui=PkgSpec(
        name="gpu-screen-recorder-ui",
        repo=Repo.AOR,
        tags=[Tag.SCREEN_RECORDER, Tag.GUI],
        units=Box(gpu_screen_recorder_ui=Unit("gpu-screen-recorder-ui.service", Scope.SINGLE_USER))
    ),

    tumbler=PkgSpec(
        name="tumbler",
        repo=Repo.AOR,
        tags=[Tag.THUMBNAIL],
        units=Box(tumblerd=Unit("tumblerd.service", Scope.SINGLE_USER))
    ),
    ffmpegthumbnailer=PkgSpec(
        name="ffmpegthumbnailer",
        repo=Repo.AOR,
        tags=[Tag.THUMBNAIL],
    ),
    # freetype2=PkgSpec(
    #     name="freetype2",
    #     repo=Repo.AOR,
    #     tags=[Tag.THUMBNAIL, Tag.LIBRARY],
    # ),
    # libgepub=PkgSpec(
    #     name="libgepub",
    #     repo=Repo.AOR,
    #     tags=[Tag.THUMBNAIL, Tag.LIBRARY],
    # ),
    libgsf=PkgSpec(
        name="libgsf",
        repo=Repo.AOR,
        tags=[Tag.THUMBNAIL, Tag.LIBRARY],
    ),
    # libopenraw=PkgSpec(
    #     name="libopenraw",
    #     repo=Repo.AOR,
    #     tags=[Tag.THUMBNAIL, Tag.LIBRARY],
    # ),
    poppler_glib=PkgSpec(
        name="poppler-glib",
        repo=Repo.AOR,
        tags=[Tag.THUMBNAIL, Tag.LIBRARY],
    ),

    mpv=PkgSpec(
        name="mpv",
        repo=Repo.AOR,
        tags=[Tag.VIDEO_PLAYER, Tag.KEYBOARD_DRIVEN],
    ),

    ueberzugpp=PkgSpec(
        name="ueberzugpp",
        repo=Repo.AOR,
        tags=[Tag.IMAGE_VIEWER, Tag.TUI],
    ),

    featherpad=PkgSpec(
        name="featherpad",
        repo=Repo.AOR,
        tags=[Tag.TEXT_EDITOR],
    ),
    
    libreoffice_fresh=PkgSpec(
        name="libreoffice-fresh",
        repo=Repo.AOR,
        tags=[Tag.OFFICE],
    ),
    libreoffice_fresh_vi=PkgSpec(
        name="libreoffice-fresh-vi",
        repo=Repo.AOR,
        tags=[Tag.OFFICE],
    ),
    libreoffice_fresh_en_gb=PkgSpec(
        name="libreoffice-fresh-en-gb",
        repo=Repo.AOR,
        tags=[Tag.OFFICE],
    ),

    zathura=PkgSpec(
        name="zathura",
        repo=Repo.AOR,
        tags=[Tag.PDF_VIEWER, Tag.ZATHURA, Tag.KEYBOARD_DRIVEN],
    ),
    zathura_pdf_mupdf=PkgSpec(
        name="zathura-pdf-mupdf",
        repo=Repo.AOR,
        tags=[Tag.PDF_VIEWER, Tag.ZATHURA],
    ),
    # zathura_pdf_poppler=PkgSpec(
    #     name="zathura-pdf-popper",
    #     repo=Repo.AOR,
    #     tags=[Tag.PDF_VIEWER, Tag.ZATHURA],
    # ),

    xarchive=PkgSpec(
        name="xarchive",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE],
    ),

    thunar=PkgSpec(
        name="thunar",
        repo=Repo.AOR,
        tags=[Tag.FILE_MANAGER, Tag.THUNAR, Tag.GUI],
        auto_start=[["thunar", "--daemon"]],
    ),
    
    thunar_volman=PkgSpec(
        name="thunar-volman",
        repo=Repo.AOR,
        tags=[Tag.THUNAR],
    ),
    thunar_archive_plugin=PkgSpec(
        name="thunar-archive-plugin",
        repo=Repo.AOR,
        tags=[Tag.THUNAR],
    ),
    
    yazi=PkgSpec(
        name="yazi",
        repo=Repo.AOR,
        tags=[Tag.FILE_MANAGER],
    ),
    
    seven_zip=PkgSpec(
        name="7zip",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE],
    ),
    chafa=PkgSpec(
        name="chafa",
        repo=Repo.AOR,
        tags=[Tag.IMAGE_VIEWER],
    ),
    jq=PkgSpec(
        name="jq",
        repo=Repo.AOR,
        tags=[Tag.JSON],
    ),
    poppler=PkgSpec(
        name="poppler",
        repo=Repo.AOR,
        tags=[Tag.PDF],
    ),
    resvg=PkgSpec(
        name="resvg",
        repo=Repo.AOR,
        tags=[Tag.SVG],
    ),
    imagemagick=PkgSpec(
        name="imagemagick",
        repo=Repo.AOR,
        tags=[Tag.THUMBNAIL],
    ),

    unzip=PkgSpec(
        name="unzip",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE]
    ),
    zip=PkgSpec(
        name="zip",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE]
    ),
    unrar=PkgSpec(
        name="unrar",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE]
    ),
    libarchive=PkgSpec(
        name="libarchive",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE]
    ),

    qt6_wayland=PkgSpec(
        name="qt6-wayland",
        repo=Repo.AOR,
        tags=[Tag.QT]
    ),

    wl_clipboard=PkgSpec(
        name="wl-clipboard",
        repo=Repo.AOR,
        tags=[Tag.CLIPBOARD],
    ),
    wl_clipboard_persist=PkgSpec(
        name="wl-clipboard-persist",
        repo=Repo.AOR,
        tags=[Tag.CLIPBOARD],
    ),
    cliphist=PkgSpec(
        name="cliphist",
        repo=Repo.AOR,
        tags=[Tag.CLIPBOARD],
    ),
)
