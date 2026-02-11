#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

export NVIM_APPNAME=lazyvim
export HISTCONTROL=ignoredups:erasedups

eval "$(starship init bash)"
eval "$(zoxide init bash)"
# # ┌────────────────────────────────────────────────────────────┐
# # │ Source system-wide settings                                │
# # └────────────────────────────────────────────────────────────┘
# if [ -f /etc/bashrc ]; then
#     . /etc/bashrc
# fi

# # ┌────────────────────────────────────────────────────────────┐
# # │ User PATH setup                                            │
# # └────────────────────────────────────────────────────────────┘
# if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
#     export PATH="$HOME/.local/bin:$HOME/bin:$PATH"
# fi
# export PATH=/usr/lib64/openmpi/bin:$PATH
# export FONTCONFIG_PATH=/etc/fonts

# # ┌────────────────────────────────────────────────────────────┐
# # │ Load custom config files from ~/.bashrc.d/                 │
# # └────────────────────────────────────────────────────────────┘
# if [ -d ~/.bashrc.d ]; then
#     for rc in ~/.bashrc.d/*; do
#         [ -f "$rc" ] && . "$rc"
#     done
# fi
# unset rc

# # ┌────────────────────────────────────────────────────────────┐
# # │ Environment fixes                                          │
# # └────────────────────────────────────────────────────────────┘
# unset GTK_IM_MODULE
# unset QT_IM_MODULE
