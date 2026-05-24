------------------
---- MONITORS ----
------------------

-- See https://wiki.hypr.land/Configuring/Basics/Monitors/
hl.monitor({
    output   = "",
    mode     = "preferred",
    position = "auto",
    scale    = "auto",
})

hl.config({
    xwayland {
        force_zero_scaling = true,  -- Forces 1x scale for sharpness (apps may appear small; good for integer scales)
        use_nearest_neighbor = true  -- Switches to bilinear filtering for smoother (but potentially blurrier) rendering; default is true (pixelated)
    }
})
