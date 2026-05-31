local Repo={
    AOR=1,
    AUR=2,
}

local Scope={
    MULTI_USER=1,
    SINGLE_USER=2,
}

local Tag={
    AUDIO=1,
    PIPEWIRE=1,
    EMACS=1,
    TEXT_EDITOR=1,
    TUI=1,
    GUI=1,
    KEYBOARD_DRIVEN=1,
    GNU=1
}

local pkg={
    pipewire={
        repo=Repo.AOR,
        tags={Tag.AUDIO, Tag.PIPEWIRE},
        units={
            pipewire_service={
                name="pipewire.service",
                scope=Scope.SINGLE_USER
            }
        }
    },
    pipewire_audio={
        repo=Repo.AOR,
        tags={Tag.AUDIO, Tag.PIPEWIRE},
        units={
            pipewire_audio_service={
                name="pipewire-audio.service",
                scope=Scope.SINGLE_USER
            }
        }
    },
    emacs_wayland={
        repo=Repo.AOR,
        tag={Tag.TEXT_EDITOR, Tag.EMACS, Tag.TUI, Tag.GUI, Tag.KEYBOARD_DRIVEN, Tag.GNU},
        config={
            default={"~/.config/doom"}
        },
        units={
            emacs_service={
                name="emacs.service",
                scope=Scope.SINGLE_USER
            }
        },
        autostart={"emacs --daemon"}
    }
}


-- LV1: single package
-- LV2: main package and it optional
-- LV3: category of LV2
-- LV4: category of LV3
-- extend/plug - parent - child - peer
-- assumption?

