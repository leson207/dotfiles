from box import Box

from src.v4.schema import Install, PkgRecipe, PackageManager, UsageRecipe, Unit
from src.v4.enumeration import Scope


Ins=Box(
    AUR=Install("aur", PackageManager("paru", ("paru", "-S"))),
    ACR=Install("core", PackageManager("pacman", ("sudo", "pacman", "-S"))),
    AER=Install("extra", PackageManager("pacman", ("sudo", "pacman", "-S"))),
)

resource=[
    "https://github.com/hyprland-community/awesome-hyprland",
    "https://wiki.hypr.land/Useful-Utilities",
]

x=Box()

x.pdf=UsageRecipe(
    [
        PkgRecipe(
            "zathura",
            Ins.AER,
            [
                PkgRecipe("zathura-pdf-mupdf", Ins.AER)
            ]
        )
    ]
)

x.text=UsageRecipe(
    [
        PkgRecipe("featherpad", Ins.AER)
    ]
)

x.image=UsageRecipe(
    [
        PkgRecipe("imv", Ins.AER)
    ]
)

x.video=UsageRecipe(
    [
        PkgRecipe("mpv", Ins.AER)
    ]
)

x.thunar=PkgRecipe(
    "thunar",
    Ins.AER,
    [
        PkgRecipe(
            "gvfs",
            Ins.AER,
            [
                PkgRecipe("gcfs-mtp", Ins.AER),
                PkgRecipe(
                    "udisks2",
                    Ins.AER,
                    [
                        PkgRecipe("e2fsprogs", Ins.AER),
                        PkgRecipe("ntfsprogs", Ins.AER),
                        PkgRecipe("dofstools", Ins.AER),
                        PkgRecipe("exfatprogs", Ins.AER),
                    ],
                    units=[Unit("udisks2.service", scope=Scope.MULTI_USER)]
                ),
            ]
        ),
        PkgRecipe("thunar-volman", Ins.AER),
        PkgRecipe("thunar-archive-plugin", Ins.AER),
        PkgRecipe(
            "tumbler",
            Ins.AER,
            [
                PkgRecipe("ffmpegthumbnailer", Ins.AER),
                PkgRecipe("libgsf", Ins.AER),
                PkgRecipe("poppler-glib", Ins.AER),
            ],
            units=[Unit("tumblerd.service", Scope.SINGLE_USER)]
        )
    ],
    auto_start=[["thunar", "--daemon"]],
)

x.yazi=PkgRecipe(
    "yazi",
    Ins.AER,
    [
        PkgRecipe("7zip", Ins.AER),
        PkgRecipe("ueberzugpp", Ins.AER),
        PkgRecipe("chafa", Ins.AER),
        PkgRecipe("jq", Ins.AER),
        PkgRecipe("poppler", Ins.AER),
        PkgRecipe("resvg", Ins.AER),
        PkgRecipe("imagemagick", Ins.AER),
    ]
)

x.file_manager=UsageRecipe(
    [
        PkgRecipe("pcmanfm", Ins.AER),
        PkgRecipe("pcmanfm-qt", Ins.AER),
        PkgRecipe("nemo", Ins.AER),
        PkgRecipe("nautilus", Ins.AER),
        PkgRecipe("thunar", Ins.AER),

        PkgRecipe("yazi", Ins.AER),
        PkgRecipe("superfile", Ins.AER),
    ]
)

x.screenshot=UsageRecipe(
    [
        PkgRecipe("grimp", Ins.AER),
        PkgRecipe("slurp", Ins.AER),
        PkgRecipe("swappy", Ins.AER),
        PkgRecipe("satty", Ins.AER),
        PkgRecipe("flameshot", Ins.AER),
    ]
)

x.screen_recorder=UsageRecipe(
    [
        PkgRecipe(
            "gpu-screen-recorder",
            Ins.AER,
            [PkgRecipe("gpu-screen-recorder-ui", Ins.AER)],
            units=[Unit("gpu-screen-recorder.service", Scope.SINGLE_USER)]
        ),
    ]
)

x.terminal_emulator=UsageRecipe(
    [
        PkgRecipe(
            "foot",
            Ins.AER,
            configs=["~/.config/foot"],
            auto_start=[["foot", "--server"]]
        )
    ]
)

x.archive=UsageRecipe(
    [
        PkgRecipe(
            "xarchive",
            Ins.AER,
            [
                # PkgRecipe("7zip", Ins.AER),
                # PkgRecipe("unzip", Ins.AER),
                # PkgRecipe("zip", Ins.AER),
                # PkgRecipe("libarchive", Ins.ACR),
            ]
        )

    ]
)
