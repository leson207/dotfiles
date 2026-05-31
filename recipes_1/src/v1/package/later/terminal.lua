return {
    emulator={
        foot={
            repo=Repo.AOR,
            single_user_config={"~/.config/foot"},
            auto_start={{"foot", "--server"}}
        },
        wezterm_git={
            repo=Repo.AUR,
            single_user_config={"~/.config/wezterm"}
        },
        kitty={
            repo=Repo.AOR,
            single_user_config={"~/.config/kitty"},
        },
        ghostty={
            repo=Repo.AOR,
            single_user_config={"~/.config/ghostty"},
            units={"app-com.mitchellh.ghostty.service", Scope.SINGLE_USER},
        },
        alacritty={
            repo=Repo.AOR,
            single_user_config={"~/.config/alacritty"},
        }
    },

    multiplexer={
        tmux={
            repo=Repo.AOR,
            single_user_config={"~/.tmux.conf"},
        },
        zellij={repo=Repo.AOR}
    }
}
