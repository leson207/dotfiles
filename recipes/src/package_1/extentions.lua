dofile("utils.lua")

local m={}

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

m.neovim={
    package_manager={ },
    plugins={
        "godlygeek/tabular",
        "tpope/vim-dadbod",
        "dhruvasagar/vim-table-mode"
    }
}
