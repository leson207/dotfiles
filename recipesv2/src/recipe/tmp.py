from src.schema.enumeration import Repo, Scope
from src.schema.atomic import Package, Topic, Unit


map = {}

Topic(
    name="misc",
    recipes=[
        Package("espanso-wayland", Repo.UNKNOWN),
        Package("zenity", Repo.OFFICIAL),
        Package("papirus-icon-theme", Repo.OFFICIAL),
        Package("glance-bin", Repo.AUR),
        Package("gh-dash-bin", Repo.AUR),
        Package("witr-bin", Repo.AUR),
        Package("zerobrew-bin", Repo.AUR),

        Package("ast-grep", Repo.AUR),
        Package("uutils-coreutils", Repo.AUR),
        Package("pake", Repo.AUR),
        Package("sing-box-bin", Repo.AUR),
        Package("qbittorrent", Repo.OFFICIAL)
    ]
)

Topic(
    name="time",
    recipes=[
        Package("task", Repo.OFFICIAL),
        Package("timew", Repo.OFFICIAL),

        Package("watson", Repo.AUR),
        Package("activitywatch-bin", Repo.AUR),
        Package("hamster-time-tracker", Repo.OFFICIAL),
    ]
)

Topic(
    name="email",
    recipes=[
        Package("thunderbird", Repo.OFFICIAL),
        Package("betterbird-bin", Repo.AUR),
        Package("stalwart-mail", Repo.AUR),
        Package("stalwart-cli", Repo.AUR),
    ]
)

Topic(
    name="ai",
    recipes=[
        Package("gemini-cli", Repo.OFFICIAL),
        Package("openai-codex", Repo.OFFICIAL),

        Package("jan-bin", Repo.AUR),
        Package("cc-switch-bin", Repo.AUR),
        Package("chatgpt-desktop-bin", Repo.AUR),
        Package("nextchat-bin", Repo.AUR),
        Package("cherry-studio-bin", Repo.AUR),
        Package("gpt4all-chat-git", Repo.AUR),
        Package("anythingllm-desktop-bin", Repo.AUR),
        Package("open-webui", Repo.AUR),
        Package("ollama-bin", Repo.AUR),
        Package("goose-desktop-bin", Repo.AUR),
    ]
)

Topic(
    name="secret",
    recipes=[
        Package(
            name="seahorse",
            repo=Repo.OFFICIAL,
            supporters=[
                Package("gnome-keyring", Repo.OFFICIAL, units=[Unit("gnome-keyring-daemon.service", scope=Scope.SINGLE_USER)])
            ]
        ),
        Package(
            name="bitwardern",
            repo=Repo.OFFICIAL,
            supporters=[
                Package("gnome-keyring", Repo.OFFICIAL, units=[Unit("gnome-keyring-daemon.service", scope=Scope.SINGLE_USER)])]
        ),
    ]
)

Topic(
    name="backup",
    recipes=[
        Package("borg", Repo.OFFICIAL),
        Package("restic", Repo.OFFICIAL),
        Package("timeshift", Repo.OFFICIAL),
    ]
)

Topic(name="disk-remote-mount", recipes=[Package("sshfs", Repo.OFFICIAL)])

Topic(
    name="audio-gui",
    recipes=[
        Package("pavucontrol", Repo.OFFICIAL),
        Package("easyeffects", Repo.OFFICIAL),
        Package("qpwgraph", Repo.OFFICIAL),
    ]
)

Topic(
    name="firewall",
    recipes=[Package("ufw", Repo.OFFICIAL, supporters=[Package("gufw", Repo.OFFICIAL)]) ]
)

Topic(
    name="git-server",
    recipes=[
        Package("gitea", Repo.OFFICIAL),
        Package("forgejo", Repo.OFFICIAL)
    ]
)

Topic(
    name="office",
    recipes=[
        Package("onlyoffice", Repo.AUR),
        Package("libreoffice-fresh", Repo.OFFICIAL),
        Package("openoffice", Repo.OFFICIAL),
    ]
)

Topic(
    name="note-taking",
    recipes=[
        # Package("memos", Repo.AUR),
        # Package("zettlr ", Repo.AUR),
        Package("obsidian", Repo.OFFICIAL),

        # Package("appflowy-bin", Repo.AUR),
        # Package("logseq-desktop-bin", Repo.AUR),
        # Package("joplin-desktop", Repo.AUR),
        # Package("notesnook-bin", Repo.AUR),
        # Package("vnote-bin", Repo.AUR),
    ]
)

Topic(
    name="social",
    recipes=[
        # telegram
        Package("telegram-desktop", Repo.OFFICIAL),

        # discord
        Package("vesktop-bin", Repo.AUR),

        # matrix
        Package("fractal", Repo.OFFICIAL),
        Package("fluffychat-bin", Repo.AUR),

        # spotify
        Package(
            name="spotify",
            repo=Repo.AUR,
            single_user_config=["~/.config/spotify"],
            supporters=[Package("spicetify-cli", Repo.AUR, single_user_config=["~/.config/spicetify"])]
        ),
        Package("spotify-tui", Repo.OFFICIAL),
    ]
)
