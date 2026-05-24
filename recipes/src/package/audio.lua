local root={
    pipewire={
        pipewire={repo=Repo.AOR, units={"pipewire.service", scope=Scope.SINGLE_USER}},
        wireplumber={repo=Repo.AOR, units={"wireplumber.service", scope=Scope.SINGLE_USER}},
        pipewire_pulse={repo=Repo.AOR, units={"pipewire-pulse.service", scope=Scope.SINGLE_USER}},
        pipewire_audio={repo=Repo.AOR},
        pipewire_alsa={repo=Repo.AOR},
    }
}

return {
    root.pipewire.pipewire,
    root.pipewire.wireplumber,
    root.pipewire.pipewire_pulse,
    root.pipewire.pipewire_audio,
    root.pipewire.pipewire_alsa,
}
