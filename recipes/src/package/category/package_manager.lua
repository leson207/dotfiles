return {
    nix={repo=Repo.AOR},
    guix={repo=Repo.AOR},
    pacman={repo=Repo.AOR, multi_user_config={"/etc/pacman.conf"}},
    yay={
        repo=Repo.GITHUB,
        installation={
            "cd ~/.cache",
            "git clone https://aur.archlinux.org/yay.git",
            "cd yay",
            "makepkg -si"
        }
    },
    paru={
        repo=Repo.GITHUB,
        installation={
            "cd ~/.cache",
            "git clone https://aur.archlinux.org/paru.git",
            "cd yay",
            "makepkg -si"
        }
    },
    reflector={repo=Repo.AOR, units={"reflector.timer", Scope.MULTI_USER}}
}

