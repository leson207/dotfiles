from src.schema.enumeration import Relationship, Repo, Scope
from src.schema.atomic import Unit
from box import Box

m=Box()

m.misc=Box(
    espanso_wayland=Box(repo=Repo.UNKNOWN),
    zenity=Box(repo=Repo.AOR),
    papirus_icon_theme=Box(repo=Repo.AOR),
    glance_bin=Box(repo=Repo.AUR),
    gh_dash_bin=Box(repo=Repo.AUR),
    witr_bin=Box(repo=Repo.AUR),
    zerobrew_bin=Box(repo=Repo.AUR),

    ast_grep=Box(repo=Repo.AUR),
    uutils_coreutils=Box(repo=Repo.AUR),
    pake=Box(repo=Repo.AUR),
    sing_box_bin=Box(repo=Repo.AUR),
    qbittorrent=Box(repo=Repo.AUR),
)
m.time=Box(
    task=Box(repo=Repo.AOR),
    timew=Box(repo=Repo.AOR),
    waston=Box(repo=Repo.AUR),

    activitywatch_bin=Box(repo=Repo.AUR),
    hamster_time_tracker=Box(repo=Repo.AUR),
)

m.email=Box(
    thunderbird=Box(repo=Repo.AOR),
    betterbird_bin=Box(repo=Repo.AUR),
    stalwart_cli=Box(repo=Repo.AUR),
    stalwart_mail=Box(repo=Repo.AUR),
)

m.ai=Box(
    gemini_cli=Box(repo=Repo.AOR),
    openai_codex=Box(repo=Repo.AOR),

    jan_bin=Box(repo=Repo.AUR),
    cc_switch_bin=Box(repo=Repo.AUR),
    chatgpt_desktop_bin=Box(repo=Repo.AUR),
    nextchat_bin=Box(repo=Repo.AUR),
)

m.secret=Box(
    seahorse=Box(
        repo=Repo.AOR,
        supporters=Box(
            gnome_keyring=Box(repo=Repo.AOR, units=[Unit("gnome-keyring-daemon.service", scope=Scope.SINGLE_USER)])
        )
    ),
    bitwardern=Box(
        repo=Repo.AOR,
        supporters=Box(
            gnome_keyring=Box(repo=Repo.AOR, units=[Unit("gnome-keyring-daemon.service", scope=Scope.SINGLE_USER)])
        )
    )
)

m.backup=Box(
    borg=Box(repo=Repo.AOR),
    restic=Box(repo=Repo.AOR),
    timeshift=Box(repo=Repo.AOR),
)

m.disk.mount.remote.sshfs=Box(repo=Repo.AOR)

m.audio.gui=Box(
    pavucontrol=Box(repo=Repo.AOR),
    easyeffects=Box(repo=Repo.AOR),
    qpwgraph=Box(repo=Repo.AOR),
)

m.network.firewall.ufw=Box(repo=Repo.AOR, supporters=Box(gufw=Box(repo=Repo.AOR)))

m.git_server=Box(
    gitea=Box(repo=Repo.AOR),
    forgejo=Box(repo=Repo.AOR),
)

m.office=Box(
    onlyoffice=Box(repo=Repo.AUR),
    openoffice=Box(repo=Repo.AUR),
    libreoffice_fresh=Box(repo=Repo.AUR),
)

m.social=Box(
    telegram_desktop=Box(repo=Repo.AOR),
    vesktop_bin=Box(repo=Repo.AUR),
    fractal=Box(repo=Repo.AOR),
    fluffychat_bin=Box(repo=Repo.AUR),
    spotify=Box(
        repo=Repo.AUR,
        single_user_config=["~/.config/spotify"],
        supporters=Box(spicetify_cli=Box(repo=Repo.AUR, single_user_config=["~/.config/spicetify"]))
    ),
    spotify_tui=Box(repo=Repo.AOR),
)

m.note_taking=Box(
    memos=Box(repo=Repo.AUR),
    zettlr=Box(repo=Repo.AUR),
    obsidian=Box(repo=Repo.AOR),

    appflowy_bin=Box(repo=Repo.AUR),
    logseq_desktop_bin=Box(repo=Repo.AUR),
    joplin_desktop=Box(repo=Repo.AUR),
    notesnook_bin=Box(repo=Repo.AUR),
    vnote_bin=Box(repo=Repo.AUR),
)
