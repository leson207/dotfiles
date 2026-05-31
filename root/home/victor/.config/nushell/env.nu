# env.nu
#
# Installed by:
# version = "0.110.0"
#
# Previously, environment variables were typically configured in `env.nu`.
# In general, most configuration can and should be performed in `config.nu`
# or one of the autoload directories.
#
# This file is generated for backwards compatibility for now.
# It is loaded before config.nu and login.nu
#
# See https://www.nushell.sh/book/configuration.html
#
# Also see `help config env` for more options.
#
# You can remove these comments if you want or leave
# them for future reference.

$env.PATH = ($env.PATH | prepend $"($env.HOME)/.config/emacs/bin")
$env.config.show_banner = false
$env.EDITOR = 'nvim'
$env.NVIM_APPNAME = 'lazyvim'
$env.config.history = {
    max_size: 100_000
    sync_on_enter: true
    file_format: "sqlite"
    isolation: true
}

$env.config.keybindings ++= [
    {
      name: accept_autosuggestion
      modifier: none
      keycode: tab
      mode: [emacs vi_normal vi_insert]
      event: { send: HistoryHintComplete }
    }
]
