from src.schema.enumeration import Repo, Scope
from src.schema.atomic import Unit, Package, Topic


map = {}

map["intel"]=Topic(
    name="intel",
    recipes=[
        Package(
            name="intel-ucode",
            repo=Repo.OFFICIAL,
            multi_user_config=[
                "/boot/loader/entries/arch.conf"
                "/boot/loader/entries/arch-zen.conf"
            ]
        ),
        Package("vulkan-intel", Repo.OFFICIAL),
        Package("intel-media-driver", Repo.OFFICIAL),
        Package("libva-intel-driver", Repo.OFFICIAL),
        # Topic(name="monitor", recipes=[Package("intel-gpu-tools", Repo.OFFICIAL)])
    ]
)

map["amd"]=Topic(
    name="amd",
    recipes=[
        Package("vulkan-radeon", Repo.OFFICIAL),
        Package("radeontop", Repo.OFFICIAL),
        Package("amdgpu-top", Repo.OFFICIAL)
    ]
)

map["gnu"]=Topic(
    name="gnu",
    recipes=[
        Package("gcc", Repo.OFFICIAL),
        Package("gdb", Repo.OFFICIAL),
        Package("ld", Repo.OFFICIAL),
        Package("libstdc++", Repo.OFFICIAL),
        Package("libstdc++abi", Repo.OFFICIAL),
    ]
)

map["clang"]=Topic(
    name="clang",
    recipes=[
        Package("clang", Repo.OFFICIAL),
        Package("lldb", Repo.OFFICIAL),
        Package("lld", Repo.OFFICIAL),
        Package("libc++", Repo.OFFICIAL),
        Package("libc++abi", Repo.OFFICIAL),
    ]
)

map["hypr"]=Topic(
    name="hypr",
    recipes=[
        Package("hyprland", Repo.OFFICIAL),
        Package("hyprlock", Repo.OFFICIAL),
        Package("xdg-desktop-portal-hyprland", Repo.OFFICIAL),
        Package("hyprqt6engine", Repo.AUR),
        Package("hyprpaper", Repo.OFFICIAL, units=[Unit("hyprpaper.service", Scope.SINGLE_USER)]),
        Package("hyprpolkitagent", Repo.OFFICIAL, units=[Unit("hyprpolkitagent.service", Scope.SINGLE_USER)]),
        Package("hypridle", Repo.OFFICIAL, units=[Unit("hypridle.service", Scope.SINGLE_USER)]),
        Package("hyprsunset", Repo.OFFICIAL, units=[Unit("hyprsunset.service", Scope.SINGLE_USER)]),
        Package("hyprlauncher", Repo.OFFICIAL),
        Package("xdg-desktop-portal-hyprland", Repo.OFFICIAL),

        # this not official but support only for hyprland
        Package("hyprshot", Repo.OFFICIAL, supporters=[Package("hyprpicker", Repo.OFFICIAL)]),
    ]
)

map["nwg"]=None
map["sway"]=None

Topic(
    name="github/charmbracelet-misc",
    recipes=[
        Package("gum", Repo.AUR),
        Package("vhs", Repo.AUR),
        Package("glow", Repo.AUR),
        Package("crush", Repo.AUR),
        Package("lipgloss", Repo.AUR),
    ]
)
