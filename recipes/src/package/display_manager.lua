local root={
    sddm={
        sddm={
            repo=Repo.AOR,
            units={"sddm.service", Scope.MULTI_USER},
            multiple_user_config={
                "/etc/sddm.conf",
                "/etc/sddm.conf.d/virtualkbd.conf",
            }
        },
        qt6_svg={repo=Repo.AOR},
        qt6_wayland={repo=Repo.AOR},
        qt6_virtualkeyboard={repo=Repo.AOR},
        qt6_multimedia_ffmpeg={repo=Repo.AOR},

        installation={
            {"sudo", "git", "clone", "-b", "master", "--depth", "1", "https://github.com/keyitdev/sddm-astronaut-theme.git", "/usr/share/sddm/themes/sddm-astronaut-theme"},
            {"sudo", "cp", "-r", "/usr/share/sddm/themes/sddm-astronaut-theme/Fonts/*", "/usr/share/fonts/"},
            "/usr/share/sddm/themes/sddm-astronaut-theme/metadata.desktop"
        }
    }
}

return {
    root.sddm
}
