local root={
    qt={
        config={
            qt5ct={repo=Repo.AOR, single_user_config={"~/.config/qt5ct"}},
            qt6ct={repo=Repo.AOR, single_user_config={"~/.config/qt6ct"}, env={QT_QPA_PLATFORMTHEME="qt6ct"}},
            kvantum={repo=Repo.AOR, single_user_config={"~/.config/Kvantum"}, env={ QT_STYLE_OVERRIDE="kvantum"}}
        }
    },

    gtk={
        config={
            gtk3={
                repo=Repo.AOR,
                single_user_config={"~/.config/gtk-3.0"},
            },
            gtk4={
                repo=Repo.AOR,
                single_user_config={"~/.config/gtk-4.0"},
            },
            nwg_look={
                repo=Repo.AOR,
                single_user_config={"~/.config/nwg-look"},
            },
        },
        theme={
            orchis_theme={repo=Repo.AOR},
            vimix_cursors={repo=Repo.AOR},
            tela_circle_icon_theme={repo=Repo.AOR},
        }
    }
}

return {
    root.qt.config.qt5ct,
    root.qt.config.qt6ct,
    root.qt.config.kvantum,

    root.gtk.config.gtk3,
    root.gtk.config.gtk4,
    root.gtk.config.nwg_look,

    -- check below
    root.gtk.theme.orchis_theme,
    root.gtk.theme.vimix_cursors,
    root.gtk.theme.tela_circle_icon_theme,
}
