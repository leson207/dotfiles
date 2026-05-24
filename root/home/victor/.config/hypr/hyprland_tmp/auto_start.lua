-------------------
---- AUTOSTART ----
-------------------

-- See https://wiki.hypr.land/Configuring/Basics/Autostart/

-- Autostart necessary processes (like notifications daemons, status bars, etc.)
-- Or execute your favorite apps at launch like this:
--
-- hl.on("hyprland.start", function ()
--   hl.exec_cmd(terminal)
--   hl.exec_cmd("nm-applet")
--   hl.exec_cmd("waybar & hyprpaper & firefox")
-- end)

hl.on("hyprland.start", function ()
  hl.exec_cmd("app2unit -- udiskie &")
  hl.exec_cmd("app2unit -- foot --server")
  hl.exec_cmd("app2unit -- thunar --daemon")
  hl.exec_cmd("app2unit -- atuin daemon start")
  -- hl.exec_cmd("app2unit -- hyprlauncher -d")
  hl.exec_cmd("app2unit -- fuzzel --launch-prefix='app2unit --'")
  hl.exec_cmd("app2unit -- wl-clip-persist --clipboard regular")
  hl.exec_cmd("app2unit -- wl-paste --type text --watch cliphist store") -- Stores only text data
  hl.exec_cmd("exec-once = app2unit -- wl-paste --type image --watch cliphist store") -- Stores only image data
  hl.exec_cmd("app2unit -- dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP")
end)

