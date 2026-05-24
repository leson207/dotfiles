local root={
    fuzzel={
        repo=Repo.AOR,
        single_user_config={"~/.config/fuzzel"},
    },
    rofi={
        repo=Repo.AOR,
        single_user_config={"~/.config/rofi"},
    },
    hyprlauncher={
        repo=Repo.AOR,
        single_user_config={"~/.config/hypr/hyprlauncher.conf"},
    },
}

return {
    root.fuzzel
}
