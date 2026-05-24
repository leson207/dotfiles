local root={
    capture={
        grim={repo=Repo.AOR},
        hyprshot={repo=Repo.AOR},
        flameshot={repo=Repo.AOR}
    },
    crop={
        slurp={repo=Repo.AOR},
    },
    annotate={
        swappy={repo=Repo.AOR},
        satty={repo=Repo.AOR},
    },
    freeze={
        wayfreeze_git={repo=Repo.AUR}
    }
}

return {
    root.capture.hyprshot
}
