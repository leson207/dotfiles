from .enumeration import Repo
from box import Box

m=Box()

m.intel=Box(
    intel_ucode=Box(repo=Repo.AOR),
    vulkan_intel=Box(repo=Repo.AOR),
    intel_media_driver=Box(repo=Repo.AOR),
    libva_intel_driver=Box(repo=Repo.AOR),
    intel_gpu_tools=Box(repo=Repo.AOR),
)

m.amd=Box(
    vulkan_radeon=Box(repo=Repo.AOR),
    radeontop=Box(repo=Repo.AOR),
    amdgpu_top=Box(repo=Repo.AOR),
)

m.gnu={
    "gcc": {"repo": Repo.AOR},
    "gdb": {"repo": Repo.AOR},
    "ld": {"repo": Repo.AOR},
    "libstdc++": {"repo": Repo.AOR},
    "libstdc++abi": {"repo": Repo.AOR},
}

m.llvm={
    "clang": {"repo": Repo.AOR},
    "lldb": {"repo": Repo.AOR},
    "lld": {"repo": Repo.AOR},
    "libc++": {"repo": Repo.AOR},
    "libc++abi": {"repo": Repo.AOR},
}

m.hypr=Box(
    hyprland=Box(repo=Repo.AOR),
    hyprlock=Box(repo=Repo.AOR),
    hypridle=Box(repo=Repo.AOR),
    hyprpaper=Box(repo=Repo.AOR),
    hyprsunset=Box(repo=Repo.AOR),
    hyprlauncher=Box(repo=Repo.AOR),
    hyprpolkitagent=Box(repo=Repo.AOR),
    hyprqt6engine=Box(repo=Repo.AOR),
    xdg_desktop_portal_hyprland=Box(repo=Repo.AOR),
    hyprshot=Box(repo=Repo.AOR),
    hyprpicker=Box(repo=Repo.AOR),
)

m["github/charmbracelet"]=Box(
    gum=Box(repo=Repo.AOR),
    vhs=Box(repo=Repo.AOR),
    glow=Box(repo=Repo.AOR),
    crush=Box(repo=Repo.AOR),
    lipgloss=Box(repo=Repo.AOR),
)

m.nwg=None
m.sway=None
