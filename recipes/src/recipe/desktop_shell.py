from src.recipe.schema import EXTRA, USER, Recipe

display_manager=Recipe(
    pkg=[
        ["sddm", EXTRA],
        ["sddm-astronaut-theme", USER]
    ],
)

window_compositor=Recipe(
    pkg=[
        ["niri", EXTRA],
        ["xwayland-satellite", EXTRA],
        ["xdg-desktop-portal-gtk", EXTRA],

        ["dms-shell", EXTRA],
        # ["dankcalendar-bin", USER],
        ["dsearch-bin", USER],
        ["dgop", EXTRA],

        ["wl-clip-persist", EXTRA],

        ["cava", EXTRA],
        ["matugen", EXTRA],

        ["qt5-wayland", EXTRA],
        ["qt6-wayland", EXTRA],

        ["fuzzel", EXTRA],
        ["app2unit", USER]
    ],
    config=[
        "~/.config/niri",
        "~/.config/fuzzel",
        "~/.config/DankMaterialShell",

        ["systemctl", "--user", "add-wants", "niri.service", "dms"],
        # ["systemctl", "--user", "enable", "dcal.service"],
        ["systemctl", "--user", "enable", "dsearch.service"],
    ],
    env=[
        ["GDK_BACKEND", "wayland"],
        ["QT_QPA_PLATFORM", "wayland"],
        ["ELECTRON_OZONE_PLATFORM_HINT", "auto"],

        ["_JAVA_AWT_WM_NONREPARENTING", "1"],

        ["DMS_HIDE_TRAYIDS", "discord,spotify,slack,teams"]
    ],
    auto_start=[
        ["wl-clip-persist", "--clipboard", "regular"],
    ]
)

theme=Recipe(
    pkg=[
        ["qt6ct", EXTRA],
        ["qt5ct", EXTRA],
        ["kvantum", EXTRA],
        ["kvantum-qt5", EXTRA],

        ["nwg-look", EXTRA],

        # ["orchis-theme", EXTRA],
        ["adw-gtk-theme", EXTRA],
        # ["vimix-cursors", EXTRA],
        # ["papirus-icon-theme", EXTRA],
        ["tela-circle-icon-theme-standard", EXTRA],
    ],
    config=[
        "~/.config/qt6ct",
        "~/.config/qt5ct",
        "~/.config/Kvantum",

        "~/gtkrc-2.0",
        "~/.config/gtk-3.0",
        "~/.config/gtk-4.0",
        # "~/.icons/default/index.theme",
        "~/.config/xsettingsd/xsettingsd.conf",
    ],
    env=[
        ["QS_ICON_THEME", "Tela-cicle"],

        ["QT_QPA_PLATFORMTHEME", "qt5ct"],
        ["QT_QPA_PLATFORMTHEME_QT6", "qt6ct"],
    ]
)
