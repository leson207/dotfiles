from src.schema.enumeration import Repo, Scope
from src.schema.atomic import Unit, PackageRecipe, TopicRecipe


map = {}

map["core"]=TopicRecipe(
    name="core",
    recipes=[
        TopicRecipe(
            name="kernel",
            recipes=[
                PackageRecipe(
                    name="linux",
                    repo=Repo.OFFICIAL,
                    multi_user_config=["/boot/loader/entries/arch.conf"],
                    supporters=[PackageRecipe("linux-headers", Repo.OFFICIAL)]
                ),
                PackageRecipe(
                    name="linux-zen",
                    repo=Repo.OFFICIAL,
                    multi_user_config=["/boot/loader/entries/arch-zen.conf"],
                    supporters=[PackageRecipe("linux-zen-headers", Repo.OFFICIAL)]
                )
            ]
        ),
        TopicRecipe(name="firmware", recipes=[PackageRecipe("linux-firmware", Repo.OFFICIAL)]),
        TopicRecipe(
            name="base",
            recipes=[PackageRecipe("base", Repo.OFFICIAL, supporters=[PackageRecipe("base-devel", Repo.OFFICIAL)])]
        ),
        TopicRecipe(name="boot-manager", recipes=[PackageRecipe("efibootmgr", Repo.OFFICIAL)]),
        TopicRecipe(name="privilege", recipes=[PackageRecipe("sudo", Repo.OFFICIAL)])
    ]
)

map["graphic"]=TopicRecipe(
    name="graphic",
    recipes=[
        TopicRecipe(
            name="rendering",
            recipes=[
                PackageRecipe(
                    name="mesa",
                    repo=Repo.OFFICIAL,
                    supporters=[
                        PackageRecipe("mesa-utils", Repo.OFFICIAL),
                        PackageRecipe("vulkan-mesa-implicit-layers", Repo.OFFICIAL),
                    ]
                )
            ]
        ),
        TopicRecipe(
            name="video encode/decode",
            recipes=[
                PackageRecipe(
                    name="libva",
                    repo=Repo.OFFICIAL,
                    # supporters=[PackageRecipe("libva-utils", Repo.OFFICIAL)]
                )
            ]
        )
    ]
)

map["intel"]=TopicRecipe(
    name="intel",
    recipes=[
        TopicRecipe(name="ucode", recipes=[PackageRecipe("intel-ucode", Repo.OFFICIAL)]),
        TopicRecipe(
            name="graphic",
            recipes=[
                PackageRecipe("vulkan-intel", Repo.OFFICIAL),
                PackageRecipe("intel-media-driver", Repo.OFFICIAL),
                PackageRecipe("libva-intel-driver", Repo.OFFICIAL),
            ]
        ),
        # TopicRecipe(name="monitor", recipes=[PackageRecipe("intel-gpu-tools", Repo.OFFICIAL)])
    ]
)

map["amd"]=TopicRecipe(
    name="amd",
    recipes=[
        TopicRecipe(name="graphic", recipes=[PackageRecipe("vulkan-radeon", Repo.OFFICIAL)]),
        # TopicRecipe(
        #     name="monitor",
        #     recipes=[
        #         PackageRecipe("radeontop", Repo.OFFICIAL),
        #         PackageRecipe("amdgpu-top", Repo.OFFICIAL)
        #     ]
        # )
    ]
)

map["disk"]=TopicRecipe(
    name="disk",
    recipes=[
        TopicRecipe(name="driver", recipes=[PackageRecipe("ntfs-3g", Repo.OFFICIAL)]),
        TopicRecipe(
            name="local-mount",
            recipes=[
                PackageRecipe(
                    name="udisks2",
                    repo=Repo.OFFICIAL,
                    units=[Unit(name="udisks2.service", scope=Scope.MULTI_USER)],
                    supporters=[PackageRecipe(name="udiskie", repo=Repo.OFFICIAL)]
                ),
            ]
        ),
        TopicRecipe(name="remote-mount", recipes=[PackageRecipe("sshfs", Repo.OFFICIAL)]),
        TopicRecipe(
            name="virtual-filesystem",
            recipes=[
                PackageRecipe(
                    name="gvfs",
                    repo=Repo.OFFICIAL,
                    supporters=[
                        PackageRecipe("gvfs-mtp", Repo.OFFICIAL), # This only for thunar if i not wrong
                        # PackageRecipe("gvfs-smb", Repo.OFFICIAL)
                    ]
                )
            ]
        ),
        TopicRecipe(
            name="utils",
            recipes=[PackageRecipe("util-linux", Repo.OFFICIAL, units=[Unit(name="fstrim.service", scope=Scope.MULTI_USER)])]
        )
    ]
)

map["audio"]=TopicRecipe(
    name="audio",
    recipes=[
        TopicRecipe(
            name="sound-system",
            recipes=[
                PackageRecipe(
                    name="pipewire",
                    repo=Repo.OFFICIAL,
                    units=[Unit("pipewire.service", Scope.MULTI_USER)],
                    supporters=[
                        PackageRecipe("wireplumber", Repo.OFFICIAL, units=[Unit("wireplumber.service", Scope.MULTI_USER)]),
                        PackageRecipe("pipewire-pulse", Repo.OFFICIAL, units=[Unit("pipewire-pulse.service", Scope.MULTI_USER)]),
                        PackageRecipe("pipewire-audio", Repo.OFFICIAL),
                        PackageRecipe("pipewire-alsa", Repo.OFFICIAL),
                        PackageRecipe("alsa-utils", Repo.OFFICIAL),
                    ]
                )
            ]
        ),
        # TopicRecipe(
        #     name="gui",
        #     recipes=[
        #         PackageRecipe("pavucontrol", Repo.OFFICIAL),
        #         PackageRecipe("easyeffects", Repo.OFFICIAL),
        #         PackageRecipe("qpwgraph", Repo.OFFICIAL),
        #     ]
        # )
    ]
)

map["network"]=TopicRecipe(
    name="network",
    recipes=[
        TopicRecipe(
            name="internet",
            recipes=[
                PackageRecipe("NetworkManager", Repo.OFFICIAL, units=[Unit("NetworkManager.service", Scope.MULTI_USER)]),
                # PackageRecipe("iwd", Repo.OFFICIAL, units=[Unit("iwd.service", Scope.MULTI_USER)])
            ]
        ),
        TopicRecipe(
            name="ssh",
            recipes=[PackageRecipe("openssh", Repo.OFFICIAL, units=[Unit("sshd.service", Scope.MULTI_USER)])]
        ),
        # TopicRecipe(
        #     name="firewall",
        #     recipes=[PackageRecipe("ufw", Repo.OFFICIAL, supporters=[PackageRecipe("gufw", Repo.OFFICIAL)]) ]
        # )
    ]
)

map["laptop"]=TopicRecipe(
    name="power",
    recipes=[
        TopicRecipe(
            name="power",
            recipes=[
                # PackageRecipe("tlp", Repo.OFFICIAL, units=[Unit("tlp.service", Scope.MULTI_USER)]),
                PackageRecipe("batsignal", Repo.OFFICIAL, units=[Unit("batsignal.service", Scope.MULTI_USER)]),
                PackageRecipe("cpupower", Repo.OFFICIAL, units=[Unit("cpupower.service", Scope.MULTI_USER)]),
                PackageRecipe(
                    name="tuned",
                    repo=Repo.OFFICIAL,
                    units=[Unit("tuned.service", Scope.MULTI_USER)],
                    supporters=[PackageRecipe("tuned-ppd", Repo.OFFICIAL, units=[Unit("tuned-ppd.service", Scope.MULTI_USER)])]
                ),
            ]
        ),
        TopicRecipe(
            name="performance",
            recipes=[
                PackageRecipe("preload", Repo.OFFICIAL, units=[Unit("preload.service", Scope.MULTI_USER)]),
                PackageRecipe("auto-cpufreq", Repo.OFFICIAL, units=[Unit("auto-cpufreq.service", Scope.MULTI_USER)]),
                PackageRecipe("irqbalance", Repo.OFFICIAL, units=[Unit("irqbalance.service", Scope.MULTI_USER)]),
                PackageRecipe("thermald", Repo.OFFICIAL, units=[Unit("thermald.service", Scope.MULTI_USER)]),
                PackageRecipe("ananicy-cpp", Repo.OFFICIAL, units=[Unit("ananicy-cpp.service", Scope.MULTI_USER)]),
            ]
        )
    ]
)

map["mirror"]=TopicRecipe(
    name="mirror",
    recipes=[PackageRecipe("reflector", Repo.OFFICIAL, units=[Unit("reflector.timer", Scope.MULTI_USER)])]
)

