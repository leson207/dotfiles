local root={
    thunar={
        thunar={
            repo=Repo.AOR,
            auto_start={{"thunar", "--daemon"}}
        },
        thunar_volman={repo=Repo.AOR},
        thunar_archive_plugin={repo=Repo.AOR},
        thunar_media_tags_plugin={repo=Repo.AOR},
        catfish={repo=Repo.AOR},
        plocate={repo=Repo.AOR},
        clamav={repo=Repo.AOR},
        clamtk={repo=Repo.AOR},
    },

    yazi={
        yazi={repo=Repo.AOR},
        seven_zip={repo=Repo.AOR},
        chafa={repo=Repo.AOR},
        jq={repo=Repo.AOR},
        poppler={repo=Repo.AOR},
        resvg={repo=Repo.AOR},
        imagemagick={repo=Repo.AOR},
        ueberzugpp={repo=Repo.AOR},
    },

    superfile={repo=Repo.AOR}
}

local picked={
    root.thunar.thunar,
    root.thunar.thunar_volman,
    root.thunar.thunar_archive_plugin,
    root.thunar.thunar_media_tags_plugin,

    root.yazi.yazi,
    root.yazi.seven_zip,
    root.yazi.chafa,
    root.yazi.jq,
    root.yazi.poppler,
    root.yazi.resvg,
    root.yazi.imagemagick,
    root.yazi.ueberzugpp
}

return picked
