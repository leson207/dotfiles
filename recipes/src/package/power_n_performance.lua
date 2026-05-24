local root={
    tlp={repo=Repo.AOR, units={"tlp.service", Scope.MULTI_USER}},
    tlp_pd={repo=Repo.AOR, units={"tlp-pd.service", Scope.MULTI_USER}},
    tlp_rdw={repo=Repo.AOR},

    preload={repo=Repo.AUR, units={"preload.service", Scope.MULTI_USER}},
    thermald={repo=Repo.AOR, units={"thermald.service", Scope.MULTI_USER}},
    cpupower={repo=Repo.AOR, units={"cpupower.service", Scope.MULTI_USER}},
    batsignal={repo=Repo.AOR, units={"batsignal.service", Scope.MULTI_USER}},
    irqbalance={repo=Repo.AOR, units={"irqbalance.service", Scope.MULTI_USER}},

    tuned={repo=Repo.AOR, units={"tuned.service", Scope.MULTI_USER}},
    tuned_ppd={repo=Repo.AOR, units={"tuned-ppd.service", Scope.MULTI_USER}},
    ananicy_cpp={repo=Repo.AOR, units={"ananicy-cpp.service", Scope.MULTI_USER}},
    auto_cpufreq={repo=Repo.AUR, units={"auto-cpufreq.service", Scope.MULTI_USER}},
    power_profiles_daemon={repo=Repo.AOR, units={"power-profiles-daemon.service", Scope.MULTI_USER}},
}

return {
    root.tlp,
    root.tlp_rdw,
    root.tlp_pd,
    root.cpupower,
    root.preload,
    root.thermald,
    root.irqbalance,
    root.batsignal
}
