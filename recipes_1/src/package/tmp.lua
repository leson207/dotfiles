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
    pake=aur,
    sing_box_bin=aur,
    asciidoctor=aor,

    mise=aor,
    just=aor,
    direnv=aor,
    entr=aor,
    watchexec=aor,
    ctags=aor,
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

m.audio.gui={
    pavucontrol=aor,
    easyeffects=aor,
    qpwgraph=aor,
}

m.office={
    abiword=aor,
    gnumeric=aor,
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

m.intel={
    intel_ucode=aor,
    vulkan_intel=aor,
    intel_media_driver=aor,
    libva_intel_driver=aor,
    intel_gpu_tools=aor,
}

m.amd={
    vulkan_radeon=aor,
    radeontop=aor,
    amdgpu_top=aor,
}

m.hypr={
    hyprland=aor,
    hyprlock=aor,
    hypridle=aor,
    hyprpaper=aor,
    hyprsunset=aor,
    hyprlauncher=aor,
    hyprpolkitagent=aor,
    hyprqt6engine=aor,
    xdg_desktop_portal_hyprland=aor,
    hyprshot=aor,
    hyprpicker=aor,
}

m["github/charmbracelet"]={
    gum=aor,
    vhs=aor,
    glow=aor,
    crush=aor,
    lipgloss=aor,
}

m.nwg={}
m.sway={}

m={
    network={
        internet={
            {
                sub_recipes={
                    {
                        package={"systemd-networkd", Repo.AOR},
                        units={
                            {"systemd-networkd.service", Scope.MULTI_USER},
                            {"systemd-resolved.service", Scope.MULTI_USER},
                        },
                        multi_user_config={
                            "sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf",
                            "/etc/systemd/network/20-wired.network"
                        }
                    },
                    {
                        package={"wpa_supplicant", Repo.AOR},
                        units={"wpa_supplicant@wlp2s0.service", Scope.MULTI_USER},
                        multi_user_config={
                            "/etc/systemd/network/25-wireless.network"
                        }
                    },
                }
            }
        }
    }
}
