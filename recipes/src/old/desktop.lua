dofile("utils.lua")

local M={
    qt={
        misc={
            {
                env={
                    QT_QPA_PLATFORM="wayland;xcb",
                    QT_ENABLE_HIGHDPI_SCALING=1,
                    QT_AUTO_SCREEN_SCALE_FACTOR=1,
                    QT_WAYLAND_DISABLE_WINDOWDECORATION=1,
                }
            }
        },
        theme_config={
            {
                sub_recipes={
                    {
                        package={"qt5ct", Repo.AOR},
                        single_user_config={"~/.config/qt5ct"},
                    },
                    {
                        package={"qt6ct", Repo.AOR},
                        single_user_config={"~/.config/qt6ct"},
                        env={
                            QT_QPA_PLATFORMTHEME="qt6ct"
                        }
                    },
                    -- {
                    --     package={"hyprqt6engine", Repo.AUR},
                    -- },
                    {
                        package={"kvantum", Repo.AOR},
                        single_user_config={"~/.config/Kvantum"},
                        env={
                            QT_STYLE_OVERRIDE="kvantum"
                        }
                    }
                }
            }
        },
    },

    gtk={
        theme_config={
            {
                sub_recipes={
                    {
                        package={"nwg-look", Repo.AOR},
                        single_user_config={"~/.config/nwg-look"},
                    },
                },
                single_user_config={
                    "~/.config/gtk-3.0",
                    "~/.config/gtk-4.0"
                },
                env={
                    GDK_SCALE=1,
                    GDK_DPI_SCALE=1,
                    GDK_BACKEND="wayland,x11",
                }
            }
        },
        theme={
            {
                sub_recipes={
                    {
                        package={"orchis-theme", Repo.AOR}
                    },
                    {
                        package={"vimix-cursors", Repo.AOR}
                    },
                    {
                        package={"tela-circle-icon-theme", Repo.AOR}
                    }
                }
            }
        }
    },
}

return M
