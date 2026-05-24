--------------------------------
---- WINDOWS AND WORKSPACES ----
--------------------------------

-- See https://wiki.hypr.land/Configuring/Basics/Window-Rules/
-- and https://wiki.hypr.land/Configuring/Basics/Workspace-Rules/

-- Example window rules that are useful

local suppressMaximizeRule = hl.window_rule({
    -- Ignore maximize requests from all apps. You'll probably like this.
    name  = "suppress-maximize-events",
    match = { class = ".*" },

    suppress_event = "maximize",
})
-- suppressMaximizeRule:set_enabled(false)

hl.window_rule({
    -- Fix some dragging issues with XWayland
    name  = "fix-xwayland-drags",
    match = {
        class      = "^$",
        title      = "^$",
        xwayland   = true,
        float      = true,
        fullscreen = false,
        pin        = false,
    },

    no_focus = true,
})

-- Layer rules also return a handle.
-- local overlayLayerRule = hl.layer_rule({
--     name  = "no-anim-overlay",
--     match = { namespace = "^my-overlay$" },
--     no_anim = true,
-- })
-- overlayLayerRule:set_enabled(false)

-- Hyprland-run windowrule
hl.window_rule({
    name  = "move-hyprland-run",
    match = { class = "hyprland-run" },

    move  = "20 monitor_h-120",
    float = true,
})

hl.window_rule({
    name  = "xdg-rule",
    match = { class = "^(xdg-desktop-portal-gtk)$" },

    size  = {900, 600},
    float = true,
    center = true
})

hl.window_rule({
    name  = "vlc-rule",
    match = { class = "vlc" },

    size  = {900, 600},
    float = true,
    center = true
})

hl.window_rule({
    name  = "mpv-rule",
    match = { class = "mpv" },

    size  = {900, 600},
    float = true,
    center = true
})

hl.window_rule({
    name  = "zathura-rule",
    match = { class = "org.pwmt.zathura" },

    size  = {900, 600},
    float = true,
    center = true
})

hl.window_rule({
    name  = "featherpad-rule",
    match = { class = "featherpad" },

    size  = {900, 600},
    float = true,
    center = true
})

hl.window_rule({
    name  = "onlyoffice-rule",
    match = { class = "ONLYOFFICE" },

    size  = {900, 600},
    float = true,
    center = true
})

hl.window_rule({
    name  = "libreoffice-rule",
    match = { class = "libreoffice-.*" },

    size  = {900, 600},
    float = true,
    center = true
})

