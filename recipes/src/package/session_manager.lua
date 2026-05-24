local root={
    for_wm={
        uwsm={
            uwsm={repo=Repo.AOR, single_user_config={"~./config/uwsm"}},
            libnewt={repo=Repo.AOR}
        }
    },

    for_app={
        app2unit={
            repo=Repo.AUR,
            env={
                APP2UNIT_SLICES="a=app-graphical.slice b=background-graphical.slice s=session-graphical.slice"
            }
        }
    }
}

return {
    root.for_wm.uwsm.uwsm,
    root.for_wm.uwsm.libnewt,
    root.for_app.app2unit
}
