from box import Box

from src.v4.schema import Install, PkgRecipe, PackageManager, UsageRecipe, Unit
from src.v4.enumeration import Scope


Ins=Box(
    AUR=Install("aur", PackageManager("paru", ("paru", "-S"))),
    ACR=Install("core", PackageManager("pacman", ("sudo", "pacman", "-S"))),
    AER=Install("extra", PackageManager("pacman", ("sudo", "pacman", "-S"))),
)

x=Box()

x.window_compositor=UsageRecipe(
    [
        PkgRecipe("niri", Ins.AER, configs=["~/.config/niri"]),
        PkgRecipe("xwayland-satelite", Ins.AER),
        PkgRecipe("xdg-desktop-portal-gtk", Ins.AER),
        PkgRecipe("qt6-wayland", Ins.AER),
    ]
)


x.clipbard=UsageRecipe(
    [
        PkgRecipe(
            "cliphist",
            Ins.AER,
            auto_start=[
                ["wl-paste", "--type", "text", "watch", "cliphist", "store"],
                ["wl-paste", "--type", "image", "watch", "cliphist", "store"],
                # "cliphist list | fuzzel --dmenu --with-nth 2 | cliphist decode | wl-copy"
            ],
        ),
        PkgRecipe(
            "wl-clip-persist",
            Ins.AER,
            auto_start=[["wl-clip-persist", "--clipboard", "regular"]]
        )
    ]
)

x.waybar=PkgRecipe(
    "waybar",
    Ins.AER,
    configs=["~/.config/waybar"],
    units=[Unit("waybar.service", Scope.SINGLE_USER)]
)

x.app_launcher=UsageRecipe(
    [
        PkgRecipe(
            "fuzzel",
            Ins.AER,
            configs=["~/.config/fuzzel"]
        ),
        PkgRecipe(
            "app2unit",
            Ins.AUR,
            env_vars=[
                ["APP2UNIT_SLICES", "a=app-graphical.slice b=background-graphical.slice s=session-graphical.slice"]
            ]
        )
    ]
)

x.app_launcher=UsageRecipe(
    [
        PkgRecipe("fuzzel", Ins.AER),
        PkgRecipe("rofi", Ins.AER),
        PkgRecipe("wofi", Ins.AER),
        PkgRecipe("walker", Ins.AUR),
        PkgRecipe("anyrun", Ins.AUR),
        PkgRecipe("vincinae", Ins.AUR),
    ]
)

x.display_manager=UsageRecipe(
    [
        PkgRecipe(
            "sddm",
            Ins.AER,
            [
                PkgRecipe("sddm-astronaut-theme", Ins.AUR)
            ],
            configs=["/etc/sddm.conf", "/etc/sddm.conf.d"]
        )
    ]
)
x.polkit_agent=UsageRecipe(
    [
        PkgRecipe("seatd", Ins.AER),
        PkgRecipe("polkit", Ins.AER),

        PkgRecipe("polkit-gnome", Ins.AER)
    ]
)

x.idle_management=UsageRecipe(
    [
        PkgRecipe("swayidle", Ins.AER)
    ]
)

x.screen_lock=UsageRecipe(
    [
        PkgRecipe("swaylock", Ins.AER),
        PkgRecipe("waylock", Ins.AER),

        PkgRecipe(
            "gtklock",
            Ins.AER,
            [
                PkgRecipe("gtklock-playerctl-module", Ins.AER),
                PkgRecipe("gtklock-powerbar-module ", Ins.AER),
                PkgRecipe("gtklock-userinfo-module", Ins.AER),
            ]
        )
    ]
)

x.backlight=UsageRecipe(
    [
        PkgRecipe("wlsunset", Ins.AER),
        PkgRecipe("wluma", Ins.AER),
        PkgRecipe("gammastep", Ins.AER),
        PkgRecipe("redshift", Ins.AER),
    ]
)

x.meta_control=UsageRecipe(
    [
        PkgRecipe("playctl", Ins.AER),
        PkgRecipe("brightnessctl", Ins.AER),
        PkgRecipe("ddcutil", Ins.AER),
        PkgRecipe("libpulse", Ins.AER),
    ]
)

x.osd=UsageRecipe(
    [
        PkgRecipe("swayosd", Ins.AER)
    ]
)

x.wallpaper=UsageRecipe(
    [
        PkgRecipe("awww", Ins.AER),
        PkgRecipe("swaybg", Ins.AER),
        PkgRecipe("wallutils", Ins.AER),
        PkgRecipe("wpaperd", Ins.AER),
    ]
)

x.notification=UsageRecipe(
    [
        PkgRecipe("mako", Ins.AER),
        PkgRecipe("dunst", Ins.AER),
        PkgRecipe("fnott", Ins.AER),
        PkgRecipe("swaync", Ins.AER),
    ]
)

x.display_manager_and_greeter=UsageRecipe(
    [
        PkgRecipe("greetd", Ins.AER),
        PkgRecipe("sddm", Ins.AER),
    ]
)

x.control_gui=UsageRecipe(
    [
        PkgRecipe("pavucontrol", Ins.AER),
        PkgRecipe("nm-applet", Ins.AER),
    ]
)
