local root={
    font={
        noto={
            noto_fonts={repo=Repo.AOR},
            noto_fonts_cjk={repo=Repo.AOR},
            noto_fonts_emoji={repo=Repo.AOR},
        },
        tff={
            tff_opensans={repo=Repo.AOR},
            tff_fira_code={repo=Repo.AOR},
            tff_cascadia_code_nerd={repo=Repo.AOR},
            tff_jetbrains_mono_nerd={repo=Repo.AOR},
        },
        tex_gyre={
            tex_gyre_fonts={repo=Repo.AOR}
        },
    },

    viewer={
        gnome_font_viewer={repo=Repo.AOR}
    }
}

return {
    root.font.noto,
    root.font.tff,
}
