local root={
    copy_paste={
        wl_clipboard={repo=Repo.AOR}
    },

    persist={
        wl_clip_persist={
            repo=Repo.AOR,
            auto_start={{"wl-clip-persist", "--clipboard regular"}}
        },
    },

    history={
        cliphist={
            repo=Repo.AOR,
            units={"cliphist.service", Scope.SINGLE_USER},
            auto_start={
                {"wl-paste", "--type", "text", "watch", "cliphist", "store"},
                {"wl-paste", "--type", "image", "watch", "cliphist", "store"},
            },
        },
        copyq={repo=Repo.AOR},
        nwg_clipman={repo=Repo.AOR},
    },
}

return {
    root.copy_paste.wl_clipboard,
    root.persist.wl_clip_persist,
    root.history.cliphist
}
