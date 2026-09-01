dofile("utils.lua")

local m={}

m.reference={
    -- https://github.com/end-4/dots-hyprland/blob/main/sdata/deps-info.md
    -- https://github.com/caelestia-dots/shell#manual-installation
    -- https://docs.noctalia.dev/v4/getting-started/installation/#manual-install
    -- https://danklinux.com/docs/dankmaterialshell/installation/
    -- https://github.com/Darkkal44/qylock#-dependencies
    -- https://axeni.de/ax-shell/
    -- https://github.com/snowarch/iNiR/wiki/INSTALL#the-hard-way-manual
    -- github tag: dotifles, quickshell, ricing, unixporn, niri, hyprland, desktop-shell, wayland
}

m.extension={
    -- https://addons.mozilla.org/en-US/firefox/addon/<name>/
    mozila={
        "betterttv",
        {"youtube-addon", "https://github.com/code-charity/youtube"},
        "youtube-nonstop",
        "enhancer-for-youtube",
        {"sponsorblock", "https://github.com/ajayyy/SponsorBlock"},
        {"read-aloud", "https://github.com/ken107/read-aloud"},
        {"popup-blocker", "https://github.com/schomery/popup-blocker"},
        {"immersive-translate", ""},
        {"tree-style-tab",},
        {"ublock-origin",},
        {"onetab"}
    },
    chromium={}
}

m.misc={
    espanso_wayland={Repo.UNKNOWN},
    dotter={Repo.GITHUB},
    markdown_oxide=aor,

    github_cli=aor,
    gh_dash_bin=aur,

    witr_bin=aur,
    zerobrew_bin=aur,
    stremio=aur;

    ast_grep=aur,
    pake=aur,
    asciidoctor=aor,

    mise=aor,
    just=aor,
    direnv=aor,
    entr=aor,
    watchexec=aor,
    compiledb=aur,
    nftables=aor,
}

m.image.editor={
    gimp=aor,
    krita=aor,
    darktable=aor,
    pinta=aur,
    rawtherapee=aor,
    lazpaint_bin=aur,
}

m.office={
    abiword=aor,
    gnumeric=aor,
}

m["github/charmbracelet"]={
    gum=aor,
    vhs=aor,
    glow=aor,
    crush=aor,
    lipgloss=aor,
}
