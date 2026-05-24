local root={
    internet={
        iwd={repo=Repo.AOR, units={"iwd.service", Scope.MULTI_USER}},
        dnsmasq={repo=Repo.AOR, units={"dnsmasq.service", Scope.MULTI_USER}},
        networkmanager={repo=Repo.AOR, units={"NetworkManager.service", Scope.MULTI_USER}},

    },

    ssh={
        openssh={
            repo=Repo.AOR,
            units={"sshd.service", Scope.MULTI_USER},
            -- units={"sshdgenkeys.service", Scope.MULTI_USER}
        }
    },

    firewall={
        ufw={
            ufw={repo=Repo.AOR},
            gufw={repo=Repo.AOR},
        },
        firewalld={repo=Repo.AOR}
    }
}

return {
    root.internet.iwd,
    root.internet.networkmanager,
    root.ssh.openssh
}

