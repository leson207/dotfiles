from .enumeration import Relationship, Repo, Scope
from .atomic import Unit

from box import Box

m=Box()

# m.bootloader.systemd={
#     "repo": Repo.AOR,
#     "multi_user_config": [
#         "/boot/loader/entries/linux.conf"
#         "/boot/loader/entries/lixux-zen.conf"
#     ],
#     "supporter": {
#         "kernel": {
#             "linux": {
#                 "repo": Repo.AOR,
#                 "supporters": {"linux_headers": {"repo": Repo.AOR}}
#             },
#             "linux-zen": {
#                 "repo": Repo.AOR,
#                 "supporters": {"linux_zen_headers": {"repo": Repo.AOR}}
#             },
#         },
#         "microcode": Box(repo=Repo.AOR)
#     }
# }

m.bootloader.systemd=Box(
    repo=Repo.AOR,
    multi_user_config=[
        "/boot/loader/entries/linux.conf"
        "/boot/loader/entries/lixux-zen.conf"
    ],
    supporter=Box(
        kernel=Box(
            linux=Box(
                repo=Repo.AOR,
                supporters=Box(linux_headers=Box(repo=Repo.AOR))
            ),
            linux_zen=Box(
                repo=Repo.AOR,
                supporters=Box(linux_zen_headers=Box(repo=Repo.AOR))
            ),
        ),
        microcode=Box(repo=Repo.AOR)
    )
)

m.init_system.systemd=Box(repo=Repo.AOR, single_user_config=["~/.config/systemd"])
m.firmware.linux_firmware=Box(repo=Repo.AOR)
m.boot_manager.efibootmgr=Box(repo=Repo.AOR)
m.privilege.sudo=Box(repo=Repo.AOR)
m.display_server_protocol.wayland=Box(repo=Repo.AOR)

m.base.rel=Relationship.ASSOCIATED
m.base.base=Box(repo=Repo.AOR)
m.base.base_devel=Box(repo=Repo.AOR)

# m.media_driver{opengl, vulkan}
# vaapi

m.graphic.opengl.rel=Relationship.ASSOCIATED
m.graphic.opengl.mesa=Box(repo=Repo.AOR, supporters=Box(mesa_utils=Box(repo=Repo.AOR)))

m.graphic.rel=Relationship.ASSOCIATED
m.graphic.vulkan.vulkan_intel=Box(repo=Repo.AOR)
m.graphic.vulkan.vulkan_radeon=Box(repo=Repo.AOR)
m.graphic.vulkan.vulkan_mesa_implicit_layers=Box(repo=Repo.AOR)

m.graphic.video.rel=Relationship.ASSOCIATED
m.graphic.vaapi.libva=Box(repo=Repo.AOR, supporters=Box(libva_utils=Box(repo=Repo.AOR)))
m.graphic.vaapi.libva_intel_driver=Box(repo=Repo.AOR)
m.graphic.vaapi.intel_media_driver=Box(repo=Repo.AOR)

m.disk.driver.ntfs_3g=Box(repo=Repo.AOR)
m.disk.mount.udisks2=Box(
    name="udisks2",
    repo=Repo.AOR,
    units=[Unit(name="udisks2.service", scope=Scope.MULTI_USER)],
    supporters=Box(udiskie=Box(repo=Repo.AOR))
)

m.disk.virtual_file_system.gvfs=Box(
    repo=Repo.AOR,
    supporters=Box(
        gvfs_mtp=Box(repo=Repo.AOR),
        # gvfs_smb=Box(repo=Repo.AOR)
    )
)

m.disk.strim.util_linux=Box(repo=Repo.AOR, units=[Unit(name="fstrim.service", scope=Scope.MULTI_USER)])

m.audio.processor.pipewire=Box(
    repo=Repo.AOR,
    units=[Unit("pipewire.service", Scope.SINGLE_USER)],
    supporter=Box(
        wireplumber=Box(repo=Repo.AOR, units=[Unit("wireplumber.service", Scope.SINGLE_USER)]),
        pipewire_pulse=Box(repo=Repo.AOR, units=[Unit("pipewire-pulse.service", Scope.SINGLE_USER)]),
        pipewire_audio=Box(repo=Repo.AOR),
        pipewire_alsa=Box(repo=Repo.AOR),
    )
)

m.network.internet.networkmanager=Box(
    repo=Repo.AOR,
    units=[Unit("NetworkManager.service", Scope.MULTI_USER)],
    supporters=Box(
        iwd=Box(repo=Repo.AOR, units=[Unit("iwd.service", Scope.MULTI_USER)]),
        dnsmasq=Box(repo=Repo.AOR, units=[Unit("dnsmasq.service", Scope.MULTI_USER)]),
    )
)
m.network.ssh.openssh=Box(repo=Repo.AOR, units=[Unit("sshd.service", Scope.MULTI_USER)])

m.power.power=Box(
    # tlp=Box(repo=Repo.AOR, units=[Unit("tlp.service", Scope.MULTI_USER)]),
    batsignal=Box(repo=Repo.AOR, units=[Unit("batsignal.service", Scope.MULTI_USER)]),
    cpupower=Box(repo=Repo.AOR, units=[Unit("cpupower.service", Scope.MULTI_USER)]),
    tunned_ppd=Box(
        repo=Repo.AOR,
        units=[Unit("tunned-ppd.service", Scope.MULTI_USER)],
        supporters=Box(tuned=Box(repo=Repo.AOR, units=[Unit("tuned.service", Scope.MULTI_USER)]))
    )
)

m.power.performance=Box(
    preload=Box(repo=Repo.AOR, units=[Unit("preload.service", Scope.MULTI_USER)]),
    auto_cpufreq=Box(repo=Repo.AOR, units=[Unit("auto-cpufreq.service", Scope.MULTI_USER)]),
    irqbalance=Box(repo=Repo.AOR, units=[Unit("irqbalance.service", Scope.MULTI_USER)]),
    thermald=Box(repo=Repo.AOR, units=[Unit("thermald.service", Scope.MULTI_USER)]),
    ananicy_cpp=Box(repo=Repo.AOR, units=[Unit("ananicy-cpp.service", Scope.MULTI_USER)]),
)

m.package_manager=Box(
    guix=Box(repo=Repo.AUR),
    nix=Box(repo=Repo.AOR),
    pacman=Box(repo=Repo.AOR, multi_user_config=["/etc/pacman.conf"]),
)

m.mirror.reflector=Box(repo=Repo.AOR, units=[Unit("reflector.timer", Scope.MULTI_USER)])
