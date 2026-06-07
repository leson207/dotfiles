from box import Box

from src.v4.schema import Install, PkgRecipe, PackageManager, UsageRecipe, Unit
from src.v4.enumeration import Scope

Ins=Box(
    AUR=Install("aur", PackageManager("paru", ("paru", "-S"))),
    ACR=Install("core", PackageManager("pacman", ("sudo", "pacman", "-S"))),
    AER=Install("extra", PackageManager("pacman", ("sudo", "pacman", "-S"))),
)

x=Box()

x.virtual_machine = UsageRecipe(
    [
        PkgRecipe("qemu-img", Ins.AER),
        PkgRecipe("edk2-ovmf", Ins.AER),
        PkgRecipe("qemu-system-x86", Ins.AER),
        PkgRecipe("qemu-audio-pipewire", Ins.AER),
        # PkgRecipe("qemu-ui-spice-core ", Ins.AER),
        # PkgRecipe("qemu-chardev-spice", Ins.AER),
        # PkgRecipe("qemu-hw-display-qxl", Ins.AER),

        PkgRecipe(
            "libvirt",
            Ins.AER,
            units=[
                Unit("libvirtd.socket", scope=Scope.MULTI_USER),
            ],
        ),

        PkgRecipe("virt-manager", Ins.AER),
        PkgRecipe("dnsmasq", Ins.AER),
    ],
    [
        ["sudo", "usermod", "-aG", "kvm", "$USER"],
        ["sudo", "usermod", "-aG", "libvirt", "$USER"],

        ["sudo", "virsh", "net-autostart", "default"],
        ["sudo", "virsh", "net-start", "default"],

        ["sudo", "ufw", "route", "allow", "from", "192.168.122.0/24"]
    ],
)

x.nushell=PkgRecipe(
    "nushell",
    Ins.AER,
    [
        PkgRecipe(
            "starship",
            Ins.AER,
            configs=["~/.config/starship.toml"],
            bootstrap=[
                ["mkdir", "($nu.data-dir | path join \"vendor/autoload\")"],
                ["starship", "init", "nu", "|", "save", "-f", "($nu.data-dir | path join \"vendor/autoload/starship.nu\")"]
            ]
        ),
        PkgRecipe(
            "atuin",
            Ins.AER,
            configs=["~/.config/atuin"],
            bootstrap=[
                ["mkdir", "~/.local/share/atuin/"],
                ["atuin", "init", "nu", "|", "save", "~/.local/share/atuin/init.nu"],
            ],
             auto_start=[["atuin", "daemon", "start"]]
        ),
    ],
    configs=["~/.config/nushell"]
)

x.zsh=PkgRecipe(
    "zsh",
    Ins.AER,
    [
        PkgRecipe("atuin", Ins.AER, configs=["~/.config/atuin"], auto_start=[["atuin", "daemon", "start"]]),
        PkgRecipe("starship", Ins.AER, configs=["~/.config/starship.toml"])
    ],
    configs=["~/.zshrc"]
)

x.cmd=UsageRecipe(
    [
        PkgRecipe("tree", Ins.AER),
        PkgRecipe("fd", Ins.AER),
        PkgRecipe("fzf", Ins.AER),
        PkgRecipe("ripgrep", Ins.AER),
        PkgRecipe("bat", Ins.AER),
        PkgRecipe("eza", Ins.AER),
        PkgRecipe("zoxide", Ins.AER),
        PkgRecipe("fastfetch", Ins.AER),
    ]
)
