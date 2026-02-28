from src.schema.enumeration import Repo, Scope
from src.schema.atomic import Package, Topic, Unit


map = {}

Topic(
    name="misc",
    recipes=[
        Package("espanso-wayland", Repo.UNKNOWN),
        Package("zenity", Repo.AOR),
        Package("papirus-icon-theme", Repo.AOR),
        Package("glance-bin", Repo.AUR),
        Package("gh-dash-bin", Repo.AUR),
        Package("witr-bin", Repo.AUR),
        Package("zerobrew-bin", Repo.AUR),

        Package("ast-grep", Repo.AUR),
        Package("uutils-coreutils", Repo.AUR),
        Package("pake", Repo.AUR),
        Package("sing-box-bin", Repo.AUR),
        Package("qbittorrent", Repo.AOR)
    ]
)

Topic(
    name="time",
    recipes=[
        Package("task", Repo.AOR),
        Package("timew", Repo.AOR),

        Package("watson", Repo.AUR),
        Package("activitywatch-bin", Repo.AUR),
        Package("hamster-time-tracker", Repo.AOR),
    ]
)

Topic(
    name="email",
    recipes=[
        Package("thunderbird", Repo.AOR),
        Package("betterbird-bin", Repo.AUR),
        Package("stalwart-mail", Repo.AUR),
        Package("stalwart-cli", Repo.AUR),
    ]
)

Topic(
    name="ai",
    recipes=[
        Package("gemini-cli", Repo.AOR),
        Package("openai-codex", Repo.AOR),

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
            repo=Repo.AOR,
            supporters=[
                Package("gnome-keyring", Repo.AOR, units=[Unit("gnome-keyring-daemon.service", scope=Scope.SINGLE_USER)])
            ]
        ),
        Package(
            name="bitwardern",
            repo=Repo.AOR,
            supporters=[
                Package("gnome-keyring", Repo.AOR, units=[Unit("gnome-keyring-daemon.service", scope=Scope.SINGLE_USER)])]
        ),
    ]
)

Topic(
    name="backup",
    recipes=[
        Package("borg", Repo.AOR),
        Package("restic", Repo.AOR),
        Package("timeshift", Repo.AOR),
    ]
)

Topic(name="disk-remote-mount", recipes=[Package("sshfs", Repo.AOR)])

Topic(
    name="audio-gui",
    recipes=[
        Package("pavucontrol", Repo.AOR),
        Package("easyeffects", Repo.AOR),
        Package("qpwgraph", Repo.AOR),
    ]
)

Topic(
    name="firewall",
    recipes=[Package("ufw", Repo.AOR, supporters=[Package("gufw", Repo.AOR)]) ]
)

Topic(
    name="git-server",
    recipes=[
        Package("gitea", Repo.AOR),
        Package("forgejo", Repo.AOR)
    ]
)

Topic(
    name="office",
    recipes=[
        Package("onlyoffice", Repo.AUR),
        Package("libreoffice-fresh", Repo.AOR),
        Package("openoffice", Repo.AOR),
    ]
)

Topic(
    name="note-taking",
    recipes=[
        # Package("memos", Repo.AUR),
        # Package("zettlr ", Repo.AUR),
        Package("obsidian", Repo.AOR),

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
        Package("telegram-desktop", Repo.AOR),

        # discord
        Package("vesktop-bin", Repo.AUR),

        # matrix
        Package("fractal", Repo.AOR),
        Package("fluffychat-bin", Repo.AUR),

        # spotify
        Package(
            name="spotify",
            repo=Repo.AUR,
            single_user_config=["~/.config/spotify"],
            supporters=[Package("spicetify-cli", Repo.AUR, single_user_config=["~/.config/spicetify"])]
        ),
        Package("spotify-tui", Repo.AOR),
    ]
)
