local root={
    telegram={
        telegram_desktop={repo=Repo.AOR}
    },

    discord={
        vesktop_bin={repo=Repo.AUR}
    },

    matrix={
        fractal={repo=Repo.AOR},
        fluffychat_bin={repo=Repo.AUR}
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
    }
}

return {
    root.telegram.telegram_desktop,
}

