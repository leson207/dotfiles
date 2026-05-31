return {
    shell={
        zsh={repo=Repo.AOR},
        bash={repo=Repo.AOR},
        fish={repo=Repo.AOR},
        nushell={
            repo=Repo.AOR,
            single_user_config={
                "~/.config/nushell/env.nu",
                "~/.config/nushell/config.nu",
            },
        },
    },

    history={
        atuin={
            repo=Repo.AOR,
            single_user_config={"~/.config/atuin"},
            auto_start={{"atuin", "daemon", "start"}},
            installation={
                {"mkdir", "~/.local/share/atuin/"},
                {"atuin", "init", "nu", "|", "save", "~/.local/share/atuin/init.nu"},
            }
        },
    },

    prompt={
        starship={
            repo=Repo.AOR,
            single_user_config={"~/.config/starship.toml"},
            installation={
                {"mkdir", "($nu.data-dir | path join \"vendor/autoload\")"},
                {"starship", "init", "nu", "|", "save", "-f", "($nu.data-dir | path join \"vendor/autoload/starship.nu\")"}
            }
        },
    }
}

