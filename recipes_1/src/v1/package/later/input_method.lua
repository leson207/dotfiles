return {
    framework={
        fcitx5={
            repo=Repo.AOR,
            single_user_config={
                "~/.config/fcitx5/config",
                "~/.config/fcitx5/profile"
            },
            env={
                QT_IM_MODULE="fcitx",
                -- GTK_IM_MODULE="fcitx",
                XMODIFIERS="@im=fcitx",
                SDL_IM_MODULE="fcitx",
                GLFW_IM_MODULE="fcitx"
            },
            reference={
                "https://hi.imnhan.com/fcitx/"
            }
        }
    },

    engine={
        fcitx5_qt={repo=Repo.AOR},
        fcitx5_gtk={repo=Repo.AOR},
        fcitx5_unikey={repo=Repo.AOR},
        fcitx5_lotus={repo=Repo.AUR, units={"fcitx5-lotus-server@$(whoami).service", Scope.MULTI_USER}},
    },

    configtool={
        fcitx5_configtool={repo=Repo.AOR},
    }
}
