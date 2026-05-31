from box import Box
from src.v1.enumeration import Repo, Scope, Tag
from src.v1.schema import Unit, PkgSpec, PkgVar, PkgRecipe, UsageRecipe


db = Box(
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

    ueberzugpp=PkgSpec(
        name="ueberzugpp",
        repo=Repo.AOR,
        tags=[Tag.IMAGE_VIEWER, Tag.TUI],
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
)
