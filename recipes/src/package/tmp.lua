dofile("utils.lua")

local m={}

m.misc={
    espanso_wayland={Repo.UNKNOWN},
    dotter={Repo.GITHUB},
    markdown_oxide=aor,
    zenity=aor,
    papirus_icon_theme=aor,
    glance_bin=aur,

    github_cli=aor,
    gh_dash_bin=aur,

    witr_bin=aur,
    zerobrew_bin=aur,
    stremio=aur;

    ast_grep=aur,
    uutils_coreutils=aur,
    pake=aur,
    sing_box_bin=aur,
    asciidoctor=aor,

    mise=aor,
    just=aor,
    direnv=aor,
    entr=aor,
    watchexec=aor,
    bear=aor,
    ctags=aor,
    compiledb=aur,
    freetube_bin=aur,
}

m.download={
    aria2=aor,
    -- yt_dlp=aor,
    -- qbittorrent=aur,
    -- freedownloadmanager=aur,
}

m.image.editor={
    gimp=aor,
    krita=aor,
    darktable=aor,
    pinta=aur,
    rawtherapee=aor,
    lazpaint_bin=aur,
}

m.pdf={
    zathura=aor,
    zathura_pdf_mupdf=aor,
    zathura_pdf_poppler=aor,
    evince=aor,
    okular=aor,
    mupdf=aor
}

m.archive={
    xarchiver=aor,
    file_roller=aor,
    -- engrampa=aor,
    backend={
        unzip=aor,
        seven_zip=aor,
        unrar=aor,
        tar=aor
    }
}

m.font_viewer={
    gnome_font_viewer=aor;
}

-- m.browser.keyboard_driven={
--     browsh=aur,
--     nyxt=aor,
--     lynx=aor,
--     luakit=aor,
-- }

m.time={
    task=aor,
    timew=aor,
    waston=aur,

    activitywatch_bin=aur,
    hamster_time_tracker=aur,
}

m.email={
    thunderbird=aor,
    betterbird_bin=aur,
    stalwart_cli=aur,
    stalwart_mail=aur,
}

m.ai={
    gemini_cli=aor,
    openai_codex=aor,

    jan_bin=aur,
    cc_switch_bin=aur,
    chatgpt_desktop_bin=aur,
    nextchat_bin=aur,
}

m.secret={
    seahorse={
        Repo.AOR,
        supporters={
            gnome_keyring={Repo.AOR, units={"gnome-keyring-daemon.service", scope=Scope.SINGLE_USER}}
        }
    },
    bitwardern={
        Repo.AOR,
        supporters={
            gnome_keyring={Repo.AOR, units={"gnome-keyring-daemon.service", scope=Scope.SINGLE_USER}}
        }
    }
}

m.backup={
    borg=aor,
    restic=aor,
    timeshift=aor,
}

m.disk.mount.remote.sshfs=aor

m.audio.gui={
    pavucontrol=aor,
    easyeffects=aor,
    qpwgraph=aor,
}

m.network.firewall.ufw={Repo.AOR, supporters={gufw=aor}}

m.git_server={
    gitea=aor,
    forgejo=aor,
}

m.office={
    onlyoffice=aur,
    openoffice=aur,
    libreoffice_fresh=aor,

    abiword=aor,
    gnumeric=aor,
}

m.social={
    telegram_desktop=aor,
    vesktop_bin=aur,
    fractal=aor,
    fluffychat_bin=aur,
    spotify={
        Repo.AUR,
        single_user_config={"~/.config/spotify"},
        supporters={spicetify_cli={Repo.AUR, single_user_config={"~/.config/spicetify"}}}
    },
    spotify_tui=aor,
}

m.note_taking={
    memos=aur,
    zettlr=aur,
    obsidian=aor,

    clickup=aur,
    appflowy_bin=aur,
    logseq_desktop_bin=aur,
    joplin_desktop=aur,
    notesnook_bin=aur,
    vnote_bin=aur,
}
