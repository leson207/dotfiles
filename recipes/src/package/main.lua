require("recipes_1.src.package.later.utils")


local function entry(val)
    assert(val ~= nil, "nil entry")
    return val
end

local kernel=require("category.kernel")
local init_system=require("category.init_system")
local microcode=require("category.microcode")
local initramfs_image=require("category.initramfs_image")
local boot_loader=require("category.boot_loader")
local boot_manager=require("recipes_1.src.package.category.later.boot_manager")

local c_library=require("category.c_library")
local userland=require("recipes_1.src.package.category.later.userland")
local core_utils=require("recipes_1.src.package.category.later.core_utils")
local permission=require("recipes.src.package.category.authenticator")
local package_manager=require("category.package_manager")

-- local time=require("category.time")
-- local locale=require("category.locale")

local firmware=require("category.firmware")
-- local disk=require("category.disk")
local audio=require("category.audio")
local network=require("recipes_1.src.package.category.later.network")
local graphic=require("category.graphic")

local message_bus=require("category.message_bus")
local display_server_protocol=require("recipes_1.src.package.category.later.display_server_protocol")
local window_compositor=require("recipes_1.src.package.later.window_compositor")
local xdg_desktop_portal=require("recipes_1.src.package.later.xdg_desktop_portal")

local dotfile_manager=require("recipes_1.src.package.category.later.dotfile_manager")
local font=require("recipes_1.src.package.later.font")
local session_manager=require("category.session_manager")
local display_manager=require("recipes_1.src.package.category.later.display_manager")

local shell=require("category.shell")
local terminal=require("recipes_1.src.package.later.terminal")

local c={
    kernel.kernel.linux,
    kernel.header.linux_headers,
    kernel.kernel.linux_zen,
    kernel.header.linux_zen_headers,
    kernel.kernel.linux_cachyos_bore,
    kernel.header.linux_cachyos_bore_headers,

    init_system.systemd,
    microcode.intel_ucode,
    boot_loader.systemd,
    boot_manager.efibootmgr,

    initramfs_image.mkinitcpio,

    c_library.glibc,
    userland.base,
    userland.base_devel,
    core_utils.coreutils,
    permission.sudo,
    package_manager.pacman,

    -- time,
    -- locale,
    -- sudo hostnamectl set-hostname arch-box

    firmware.linux_firmware,

    -- disk,
    audio.pipewire,
    audio.wireplumber,
    audio.pipewire_pulse,
    audio.pipewire_audio,
    audio.pipewire_alsa,
    graphic.common.mesa,
    graphic.common.libva,
    graphic.intel.libva_intel_driver,
    graphic.intel.intel_media_driver,
    network.internet.iwd,
    network.internet.networkmanager,
    network.ssh.openssh,

    display_server_protocol.wayland,
    message_bus.dbus,

    window_compositor.niri,
    xdg_desktop_portal.xdg_desktop_portal_gtk,

    -- session_manager,
    -- display_manager,

    dotfile_manager.stow,
    font.noto.noto_fonts,
    font.noto.noto_fonts_cjk,
    font.noto.noto_fonts_emoji,
    font.tff.tff_fira_code,
    font.tff.tff_jetbrains_mono_nerd,

    shell.shell.nushell,
    shell.history.atuin,
    shell.prompt.starship,

    terminal.emulator.foot,
    terminal.multiplexer.tmux,
}

local EXPECTED = 100
for i = 1, EXPECTED do
    assert(c[i] ~= nil, "element at index " .. i .. " is nil")
end
