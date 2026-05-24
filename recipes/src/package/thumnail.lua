local root={
    tumbler={repo=Repo.AOR, units={"tumblerd.service", Scope.SINGLE_USER}},
    ffmpegthumbnailer={repo=Repo.AOR},
    freetype2={repo=Repo.AOR},
    libgepub={repo=Repo.AOR},
    libgsf={repo=Repo.AOR},
    libopenraw={repo=Repo.AOR},
    poppler_glib={repo=Repo.AOR},
}

return {
    root.tumbler,
    root.ffmpegthumbnailer,
    root.freetype2,
    root.libgepub,
    root.libgsf,
    root.libopenraw,
    root.poppler_glib
}
