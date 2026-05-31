local root={
    telegram={
        telegram_desktop={repo=Repo.AOR}
    },

    discord={
        vesktop_bin={repo=Repo.AUR},
        dorion_bin={repo=Repo.AUR},
    },

    matrix={
        fractal={repo=Repo.AOR},
        cinny_desktop_bin={repo=Repo.AUR},
        fluffychat_bin={repo=Repo.AUR},
        gomuks_web_bin={repo=Repo.AUR},
        iamb_git={repo=Repo.AUR},
        commet_bin={repo=Repo.AOR}
    },

    spotify={
        gui={
            spotify={repo=Repo.AUR, single_user_config={"~/.config/spotify"}},
            spicetify_cli={repo=Repo.AUR, single_user_config={"~/.config/spicetify"}},
        },
        tui={
            spotify_tui={repo=Repo.AOR}
        }
    },

    youtube={
        freetube_bin={repo=Repo.AUR},
    },

    steam={
        steam={repo=Repo.AOR},
        millennium={repo=Repo.AUR}
    }
}

return {
    root.telegram.telegram_desktop,
}

