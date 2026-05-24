dofile("utils.lua")

local m={}


m.intel={
    intel_ucode=aor,
    vulkan_intel=aor,
    intel_media_driver=aor,
    libva_intel_driver=aor,
    intel_gpu_tools=aor,
}

m.amd={
    vulkan_radeon=aor,
    radeontop=aor,
    amdgpu_top=aor,
}

m.gnu={
    gcc=aor,
    gdb=aor,
    ld=aor,
    ["libstdc++"]=aor,
    ["libstdc++abi"]=aor,
}

m.llvm={
    clang= aor,
    lldb= aor,
    lld= aor,
    ["libc++"]=aor,
    ["libc++abi"]=aor,
}

m.hypr={
    hyprland=aor,
    hyprlock=aor,
    hypridle=aor,
    hyprpaper=aor,
    hyprsunset=aor,
    hyprlauncher=aor,
    hyprpolkitagent=aor,
    hyprqt6engine=aor,
    xdg_desktop_portal_hyprland=aor,
    hyprshot=aor,
    hyprpicker=aor,
}

m["github/charmbracelet"]={
    gum=aor,
    vhs=aor,
    glow=aor,
    crush=aor,
    lipgloss=aor,
}

m.nwg={}
m.sway={}
