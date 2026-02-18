from re import Pattern
from src.schema.enumeration import Repo, Scope
from src.schema.atomic import Unit, PackageRecipe, TopicRecipe


map = {}

# coexist
TopicRecipe(
    name="time",
    recipes=[
        PackageRecipe("task", Repo.OFFICIAL),
        PackageRecipe("timew", Repo.OFFICIAL),

        PackageRecipe("watson", Repo.AUR),
        PackageRecipe("activitywatch-bin", Repo.AUR),
        PackageRecipe("hamster-time-tracker", Repo.OFFICIAL),
    ]
)

# TODO: They just share a same trait, not alternative. how to handle that? The same as nwg
TopicRecipe(
    name="github/charmbracelet-misc",
    recipes=[
        PackageRecipe("gum", Repo.AUR),
        PackageRecipe("vhs", Repo.AUR),
        PackageRecipe("glow", Repo.AUR),
        PackageRecipe("crush", Repo.AUR),
        PackageRecipe("lipgloss", Repo.AUR),
    ]
)

TopicRecipe(
    name="gtk-theme",
    recipes=[
        PackageRecipe(
            name="orchis-theme",
            repo=Repo.OFFICIAL,
            supporters=[
                PackageRecipe("vimix-cursors", Repo.OFFICIAL),
                PackageRecipe("tela-circle-icon-theme", Repo.OFFICIAL),
            ]
        ),
        PackageRecipe("gnome-themes-extra", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="firefox-theme",
    recipes=[PackageRecipe("python-pywalfox", Repo.AUR)]
)

TopicRecipe(
    name="torrent",
    recipes=[PackageRecipe("qbittorrent", Repo.OFFICIAL)]
)

TopicRecipe(
    name="email",
    recipes=[
        PackageRecipe("thunderbird", Repo.OFFICIAL),
        PackageRecipe("betterbird-bin", Repo.AUR),
        PackageRecipe("stalwart-mail", Repo.AUR),
        PackageRecipe("stalwart-cli", Repo.AUR),
    ]
)

TopicRecipe(
    name="spotifiy",
    recipes=[
        PackageRecipe("spotifiy", Repo.AUR),
        PackageRecipe("spicetify-cli", Repo.AUR),
        PackageRecipe("spotifiy-tui", Repo.OFFICIAL),
    ]
)

TopicRecipe(
    name="misc",
    recipes=[
        PackageRecipe("espanso-wayland", Repo.UNKNOWN),
        PackageRecipe("zenity", Repo.OFFICIAL),
        PackageRecipe("cava", Repo.OFFICIAL),
        PackageRecipe("papirus-icon-theme", Repo.OFFICIAL),
        PackageRecipe("glance-bin", Repo.AUR),
        PackageRecipe("gh-dash-bin", Repo.AUR),
        PackageRecipe("witr-bin", Repo.AUR),

        PackageRecipe("ast-grep", Repo.AUR),
        PackageRecipe("uutils-coreutils", Repo.AUR),
        PackageRecipe("broot", Repo.AUR),
        PackageRecipe("pake", Repo.AUR),
        PackageRecipe("sing-box-bin", Repo.AUR),
    ]
)

TopicRecipe(
    name="ai",
    recipes=[
        PackageRecipe("jan-bin", Repo.AUR),
        PackageRecipe("cc-switch-bin", Repo.AUR),
        PackageRecipe("chatgpt-desktop-bin", Repo.AUR),
        PackageRecipe("nextchat-bin", Repo.AUR),
        PackageRecipe("cherry-studio-bin", Repo.AUR),
        PackageRecipe("gpt4all-chat-git", Repo.AUR),
        PackageRecipe("anythingllm-desktop-bin", Repo.AUR),
        PackageRecipe("open-webui", Repo.AUR),
        PackageRecipe("ollama-bin", Repo.AUR),
        PackageRecipe("goose-desktop-bin", Repo.AUR),
    ]
)
