return {
    gui={
        firefox={
            repo=Repo.AOR,
            -- single_user_config={"~/.config/firefox"}
        },
        speech_dispatcher={repo=Repo.AOR},
        python_pywalfox={repo=Repo.AUR},

        brave_bin={repo=Repo.AUR, single_user_config={"~/.config/brave-flags.conf"}},
        zen_browser_bin={repo=Repo.AUR},
        google_chrome_bin={repo=Repo.AUR, single_user_config={"~/.config/chrome-flags.conf"}},
        helium_browser_bin={repo=Repo.AUR},
        thorium_browser_bin={repo=Repo.AUR, single_user_config={"~/.config/thorium-flags.conf"}},
        microsoft_edge_stable_bin={repo=Repo.AUR}
    },
    keyboard_driven={
        browsh={repo=Repo.AUR},
        nyxt={repo=Repo.AOR},
        lynx={repo=Repo.AOR},
        luakit={repo=Repo.AOR},
    }
}

