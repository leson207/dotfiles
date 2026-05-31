local root={
    video={
        mpv={
            repo=Repo.AOR,
            single_user_config={"~/.config/mpv"},
        },
        vlc={repo=Repo.AOR},
        clapper={repo=Repo.AOR},

    },

    image={
        gui={
            mpv={
                repo=Repo.AOR,
                single_user_config={"~/.config/mpv"},
            },
            imv={repo=Repo.AOR},
            feh={repo=Repo.AOR},
            gthumb={repo=Repo.AOR},
            swayimg={repo=Repo.AOR},
        },
        tui={
            ueberzugpp={repo=Repo.AOR},
        }
    },

    text={
        featherpad={repo=Repo.AOR}
    },

    pdf={
        zathura={
            zathura={repo=Repo.AOR},
            zathura_pdf_mupdf={repo=Repo.AOR},
            zathura_pdf_poppler={repo=Repo.AOR}
        },
        evince={repo=Repo.AOR},
        mupdf={repo=Repo.AOR},
    },

    office={
        onlyoffice_bin={repo=Repo.AUR},

        libreoffice_fresh={repo=Repo.AOR},
        libreoffice_fresh_vi={repo=Repo.AOR},
        libreoffice_fresh_en_gb={repo=Repo.AOR},
    },

    archive={
        engrampa={repo=Repo.AOR},
        xarchiver={repo=Repo.AOR},
        file_roller={repo=Repo.AOR},
    },

    not_decied={
        gnome_font_viewer={repo=Repo.AOR},
        -- compress
        tar={repo=Repo.AOR},
        gzip={repo=Repo.AOR},
        bzip2={repo=Repo.AOR},
        xz={repo=Repo.AOR},
        zstd={repo=Repo.AOR},

        -- package compress
        libarchive={repo=Repo.AOR},
        unrar={repo=Repo.AOR},
        unzip={repo=Repo.AOR},
        seven_zip={repo=Repo.AOR}, -- 7zip
        zip={repo=Repo.AOR},
    }
}

return {
    root.video.mpv,
    root.image.gui.mpv,
    root.image.tui.ueberzugpp,
    root.text.featherpad,

    root.pdf.zathura.zathura,
    root.pdf.zathura.zathura_pdf_poppler,

    root.office.onlyoffice_bin,

    root.archive.xarchiver
}
