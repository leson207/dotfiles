local root={
    systemd={
        repo=Repo.AOR,
        units={"systemd-timesyncd", Scope.MULTI_USER},
        installation={
            {"sudo", "timedatectl", "set-timezone", "Asia/Ho_Chi_Minh"},
            {"sudo", "timedatectl", "set-ntp", "true"},
            {"sudo", "timedatectl", "set-local-rtc", "0"},
            {"timedatectl", "status"},
            {"hwclock", "--systohc"},
        }
    }
}

return {
    root.systemd
}
