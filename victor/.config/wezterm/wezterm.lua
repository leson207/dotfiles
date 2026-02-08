local wezterm = require 'wezterm'

local config = wezterm.config_builder()

config.enable_wayland = true
config.hide_tab_bar_if_only_one_tab = true
config.window_background_opacity = 0.7
config.text_background_opacity = 0.5
config.window_close_confirmation = 'NeverPrompt'
config.window_content_alignment = {
  horizontal = 'Center',
  vertical = 'Center',
}

return config
