# config.nu
#
# Installed by:
# version = "0.110.0"
#
# This file is used to override default Nushell settings, define
# (or import) custom commands, or run any other startup tasks.
# See https://www.nushell.sh/book/configuration.html
#
# Nushell sets "sensible defaults" for most configuration settings,
# so your `config.nu` only needs to override these defaults if desired.
#
# You can open this file in your default editor using:
#     config nu
#
# You can also pretty-print and page through the documentation for configuration
# options using:
#     config nu --doc | nu-highlight | less -R

if $nu.is-interactive { fastfetch }

mkdir ($nu.data-dir | path join "vendor/autoload")
starship init nu | save -f ($nu.data-dir | path join "vendor/autoload/starship.nu")

source ~/.zoxide.nu
source ~/.local/share/atuin/init.nu

# Copy outputs of the last N commands to clipboard
# def cc [number: int]
# {
#     # Get the last N commands from history, excluding 'cc' commands
#     let cmds = (history | where command !~ '^cc ' | last $number)
#
#     if ($cmds | is-empty)
#     {
#         print "No commands in history"
#     }
#     else
#     {
#         # Execute each command and collect outputs
#         let outputs = ($cmds | each { |cmd|
#             let output = (nu -c $cmd.command | into string)
#             $"Command: ($cmd.command)\nOutput: ($output)\n"
#         } | str join "\n---\n")
#
#         $outputs | wl-copy
#         print $"Copied outputs of last ($number) commands"
#     }
# }
