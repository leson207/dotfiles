from src.schema.enumeration import Relationship, Repo, Scope
from src.schema.atomic import Unit, Package, Topic


map = {}

Topic(
    name="kernel",
    recipes=[
        Package(
            name="linux",
            repo=Repo.OFFICIAL,
            multi_user_config=["/boot/loader/entries/arch.conf"],
            supporters=[Package("linux-headers", Repo.OFFICIAL)]
        ),
        Package(
            name="linux-zen",
            repo=Repo.OFFICIAL,
            multi_user_config=["/boot/loader/entries/arch-zen.conf"],
            supporters=[Package("linux-zen-headers", Repo.OFFICIAL)]
        )
    ]
)

Topic(
    name="microcode",
    recipes=[
        Package(
            name="intel-ucode",
            repo=Repo.OFFICIAL,
            multi_user_config=["/boot/loader/entries"]
        )
    ]
)

Topic(name="init system", recipes=[Package("systemd", Repo.OFFICIAL, single_user_config=["~/.config/systemd"])])
Topic(name="firmware", recipes=[Package("linux-firmware", Repo.OFFICIAL)])
Topic(name="boot-manager", recipes=[Package("efibootmgr", Repo.OFFICIAL)])
Topic(name="privilege", recipes=[Package("sudo", Repo.OFFICIAL)])
Topic(name="display-server-protocol", recipes=[Package("wayland", Repo.OFFICIAL)])

Topic(
    name="base",
    relationship=Relationship.ASSOCIATED,
    recipes=[
        Package("base", Repo.OFFICIAL),
        Package("base-devel", Repo.OFFICIAL)
    ]
)

Topic(
    name="graphic",
    recipes=[
        Topic(
            name="driver",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Package(
                    name="mesa",
                    repo=Repo.OFFICIAL,
                    supporters=[Package("mesa-utils", Repo.OFFICIAL)]
                ),
                Package("intel-media-driver", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="rendering",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Package("vulkan-intel", Repo.OFFICIAL),
                Package("vulkan-radeon", Repo.OFFICIAL),
                Package("vulkan-mesa-implicit-layers", Repo.OFFICIAL),
            ]
        ),
        Topic(
            name="video acceleration",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Package(
                    name="libva",
                    repo=Repo.OFFICIAL,
                    supporters=[Package("libva-utils", Repo.OFFICIAL)]
                ),
                Package("libva-intel-driver", Repo.OFFICIAL),
            ]
        )
    ]
)

Topic(
    name="disk",
    recipes=[
        Topic(name="driver", recipes=[Package("ntfs-3g", Repo.OFFICIAL)]),
        Topic(
            name="local-mount",
            recipes=[
                Package(
                    name="udisks2",
                    repo=Repo.OFFICIAL,
                    units=[Unit(name="udisks2.service", scope=Scope.MULTI_USER)],
                    supporters=[Package(name="udiskie", repo=Repo.OFFICIAL)]
                ),
            ]
        ),
        Topic(
            name="virtual-filesystem",
            recipes=[
                Package(
                    name="gvfs",
                    repo=Repo.OFFICIAL,
                    supporters=[
                        Package("gvfs-mtp", Repo.OFFICIAL),
                        # Package("gvfs-smb", Repo.OFFICIAL)
                    ]
                )
            ]
        ),
        Topic(
            name="strim",
            recipes=[Package("util-linux", Repo.OFFICIAL, units=[Unit(name="fstrim.service", scope=Scope.MULTI_USER)])]
        )
    ]
)

Topic(
    name="audio",
    recipes=[
        Topic(
            name="sound-system",
            recipes=[
                Package(
                    name="pipewire",
                    repo=Repo.OFFICIAL,
                    units=[Unit("pipewire.service", Scope.SINGLE_USER)],
                    supporters=[
                        Package("wireplumber", Repo.OFFICIAL, units=[Unit("wireplumber.service", Scope.SINGLE_USER)]),
                        Package("pipewire-pulse", Repo.OFFICIAL, units=[Unit("pipewire-pulse.service", Scope.SINGLE_USER)]),
                        Package("pipewire-audio", Repo.OFFICIAL),
                        Package("pipewire-alsa", Repo.OFFICIAL),
                        Package("alsa-utils", Repo.OFFICIAL),
                    ]
                )
            ]
        )
    ]
)

Topic(
    name="network",
    recipes=[
        Topic(
            name="internet",
            recipes=[
                Package(
                    name="NetworkManager",
                    repo=Repo.OFFICIAL,
                    units=[Unit("NetworkManager.service", Scope.MULTI_USER)],
                    supporters=[
                        Package("iwd", Repo.OFFICIAL, units=[Unit("iwd.service", Scope.MULTI_USER)]),
                        Package("dnsmasq", Repo.OFFICIAL, units=[Unit("dnsmasq.service", Scope.MULTI_USER)]),
                    ]
                ),
            ]
        ),
        Topic(
            name="ssh",
            recipes=[Package("openssh", Repo.OFFICIAL, units=[Unit("sshd.service", Scope.MULTI_USER)])]
        )
    ]
)

Topic(
    name="power",
    recipes=[
        Topic(
            name="power",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                # Package("tlp", Repo.OFFICIAL, units=[Unit("tlp.service", Scope.MULTI_USER)]),
                Package("batsignal", Repo.OFFICIAL, units=[Unit("batsignal.service", Scope.MULTI_USER)]),
                Package("cpupower", Repo.OFFICIAL, units=[Unit("cpupower.service", Scope.MULTI_USER)]),
                Package(
                    name="tuned",
                    repo=Repo.OFFICIAL,
                    units=[Unit("tuned.service", Scope.MULTI_USER)],
                    supporters=[Package("tuned-ppd", Repo.OFFICIAL, units=[Unit("tuned-ppd.service", Scope.MULTI_USER)])]
                ),
            ]
        ),
        Topic(
            name="performance",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Package("preload", Repo.OFFICIAL, units=[Unit("preload.service", Scope.MULTI_USER)]),
                Package("auto-cpufreq", Repo.OFFICIAL, units=[Unit("auto-cpufreq.service", Scope.MULTI_USER)]),
                Package("irqbalance", Repo.OFFICIAL, units=[Unit("irqbalance.service", Scope.MULTI_USER)]),
                Package("thermald", Repo.OFFICIAL, units=[Unit("thermald.service", Scope.MULTI_USER)]),
                Package("ananicy-cpp", Repo.OFFICIAL, units=[Unit("ananicy-cpp.service", Scope.MULTI_USER)]),
            ]
        )
    ]
)

Topic(
    name="package-manager",
    recipes=[
        # Package("guix", Repo.AUR),
        # Package("nix", Repo.OFFICIAL),
        Package("pacman", Repo.OFFICIAL, multi_user_config=["/etc/pacman.conf"]),
    ]
)

map["mirror"]=Topic(
    name="mirror",
    recipes=[Package("reflector", Repo.OFFICIAL, units=[Unit("reflector.timer", Scope.MULTI_USER)])]
)

