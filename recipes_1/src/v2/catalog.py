from box import Box
from src.v2.schema import Unit, PkgSpec
from src.v2.enumeration import Repo, Scope, Tag


db=Box(
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

    glibc=PkgSpec(
        name="glibc",
        repo=Repo.AOR,
        tags=[Tag.C_LIBRARY, Tag.ARCH_PREINSTALLED],
    ),

    sudo=PkgSpec(
        name="sudo",
        repo=Repo.AOR,
        tags=[Tag.AUTHENTICATOR],
        configs=Box(default=["/etc/sudoers.d/10-foo"])
    ),


    base_devel=PkgSpec(
        name="base-devel",
        repo=Repo.AOR,
        tags=[]
    ),
    make=PkgSpec(
        name="make",
        repo=Repo.AOR,
        tags=[Tag.BUILD_SYSTEM, Tag.CXX, Tag.GNU]
    ),
    ninja=PkgSpec(
        name="ninja",
        repo=Repo.AOR,
        tags=[Tag.BUILD_SYSTEM, Tag.CXX]
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
    git=PkgSpec(
        name="git",
        repo=Repo.AOR,
        tags=[Tag.VERSION_CONTROL_SYSTEM]
    ),
    git_delta=PkgSpec(
        name="git-delta",
        repo=Repo.AOR,
        tags=[Tag.PAGER, Tag.GIT]
    ),
    less=PkgSpec(
        name="less",
        repo=Repo.AOR,
        tags=[Tag.TEXT_VIEWER, Tag.TUI]
    ),

    pacman=PkgSpec(
        name="pacman",
        repo=Repo.AOR,
        tags=[Tag.PACKAGE_MANAGER, Tag.ARCH_PREINSTALLED],
    ),
    yay=PkgSpec(
        name="yay",
        repo=Repo.GITHUB,
        tags=[Tag.PACKAGE_MANAGER],
    ),
    paru=PkgSpec(
        name="paru",
        repo=Repo.GITHUB,
        tags=[Tag.PACKAGE_MANAGER],
    ),
    reflector=PkgSpec(
        name="reflector",
        repo=Repo.AOR,
        tags=[Tag.MIRROR],
        units=Box(reflector_timer=Unit(name="reflector.timer", scope=Scope.MULTI_USER))
    ),
    
    mesa=PkgSpec(
        name="mesa",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.OPENGL, Tag.VA_API]
    ),
    intel_media_driver=PkgSpec(
        name="intel-media-driver",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.INTEL, Tag.VA_API]
    ),
    vulkan_intel=PkgSpec(
        name="vulkan-intel",
        repo=Repo.AOR,
        tags=[Tag.GRAPHIC, Tag.VULKAN, Tag.INTEL]
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

    udisks2=PkgSpec(
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
        tags=[Tag.DISK, Tag.FS_UTILS]
    ),
    exfatprogs=PkgSpec(
        name="exfatprogs",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.FS_UTILS]
    ),
    ntfsprogs=PkgSpec(
        name="ntfsprogs",
        repo=Repo.AOR,
        tags=[Tag.DISK, Tag.FS_UTILS]
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

    nushell=PkgSpec(
        name="nushell",
        repo=Repo.AOR,
        tags=[Tag.SHELL],
        configs=Box(default=[
            "~/.config/nushell/env.nu",
            "~/.config/nushell/config.nu",
        ])
    ),
    starship=PkgSpec(
        name="starship",
        repo=Repo.AOR,
        tags=[Tag.SHELL_PROMPT],
    ),
    atuin=PkgSpec(
        name="atuin",
        repo=Repo.AOR,
        tags=[Tag.SHELL_HISTORY],
        auto_start=[["atuin", "daemon", "start"]],
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
    libgsf=PkgSpec(
        name="libgsf",
        repo=Repo.AOR,
        tags=[Tag.THUMBNAIL, Tag.LIBRARY],
    ),
    poppler_glib=PkgSpec(
        name="poppler-glib",
        repo=Repo.AOR,
        tags=[Tag.THUMBNAIL, Tag.LIBRARY],
    ),

    seven_zip=PkgSpec(
        name="7zip",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE],
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

    fcitx5=PkgSpec(
        name="fcitx5",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.INPUT_METHOD],
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
        # reference=["https://hi.imnhan.com/fcitx/"]
    ),
    fcitx5_gtk=PkgSpec(
        name="fcitx5-gtk",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.GTK]
    ),
    fcitx5_qt=PkgSpec(
        name="fcitx5-qt",
        repo=Repo.AOR,
        tags=[Tag.FCITX5, Tag.QT]
    ),
    fcitx5_configtool=PkgSpec(
        name="fcitx5-configtool",
        repo=Repo.AOR,
        tags=[Tag.FCITX5]
    ),
    fcitx5_unikey=PkgSpec(
        name="fcitx5-unikey",
        repo=Repo.AOR,
        tags=[Tag.FCITX5]
    ),
)

db2=Box(
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
    ),

    mpv=PkgSpec(
        name="mpv",
        repo=Repo.AOR,
        tags=[Tag.VIDEO_PLAYER, Tag.KEYBOARD_DRIVEN],
    ),

    imv=PkgSpec(
        name="imv",
        repo=Repo.AOR,
        tags=[Tag.IMAGE_VIEWER, Tag.KEYBOARD_DRIVEN],
    ),

    featherpad=PkgSpec(
        name="featherpad",
        repo=Repo.AOR,
        tags=[Tag.TEXT_EDITOR],
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

    xarchive=PkgSpec(
        name="xarchive",
        repo=Repo.AOR,
        tags=[Tag.ARCHIVE_VIEWER],
    ),

    libreoffice_fresh=PkgSpec(
        name="libreoffice-fresh",
        repo=Repo.AOR,
        tags=[Tag.OFFICE, Tag.LIBRE_OFFICE],
    ),
    libreoffice_fresh_vi=PkgSpec(
        name="libreoffice-fresh-vi",
        repo=Repo.AOR,
        tags=[Tag.OFFICE, Tag.LIBRE_OFFICE],
    ),
    libreoffice_fresh_en_gb=PkgSpec(
        name="libreoffice-fresh-en-gb",
        repo=Repo.AOR,
        tags=[Tag.OFFICE, Tag.LIBRE_OFFICE],
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
)

db3=Box(
    cliphist=PkgSpec(
        name="cliphist",
        repo=Repo.AOR,
        tags=[Tag.CLIPBOARD_MANAGER],
    ),
    wl_clip_persist=PkgSpec(
        name="wl-clip-persist",
        repo=Repo.AOR,
        tags=[Tag.CLIPBOARD],
    ),

    fuzzel=PkgSpec(
        name="fuzzel",
        repo=Repo.AOR,
        tags=[Tag.APP_LAUNCHER],
        configs=Box(default=["~/.config/fuzzel"])
    ),
    app2unit=PkgSpec(
        name="app2unit",
        repo=Repo.AUR,
        tags=[Tag.APP_LAUNCHER]
    ),

    btop=PkgSpec(
        name="btop",
        repo=Repo.AOR,
        tags=[Tag.MONITOR, Tag.TUI],
        configs=Box(default=["~/.config/btop"])
    ),
)
