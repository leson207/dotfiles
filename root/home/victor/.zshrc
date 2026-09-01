# zmodload zsh/zprof

HISTSIZE=1000
SAVEHIST=1000
HISTFILE="$HOME/.zsh_history"

setopt APPEND_HISTORY           # Append instead of overwriting

setopt HIST_IGNORE_ALL_DUPS     # Remove older duplicates

setopt HIST_VERIFY              # Don't execute history expansion immediately
setopt HIST_REDUCE_BLANKS       # Remove extra spaces

setopt HIST_FCNTL_LOCK
setopt EXTENDED_HISTORY         # Store timestamps and duration

source ~/.local/share/zinit/zinit.git/zinit.zsh

ZSH_AUTOSUGGEST_STRATEGY=(history)
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main)

zinit ice wait lucid
zinit light zsh-users/zsh-autosuggestions

zinit ice wait lucid
zinit light zsh-users/zsh-syntax-highlighting

# source ~/.local/share/zsh-autosuggestions/zsh-autosuggestions.zsh
# source ~/.local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Evals
eval "$(atuin init zsh)"
eval "$(zoxide init zsh)"
# eval "$(direnv hook zsh)"
eval "$(starship init zsh)"

# Aliases
alias ls='eza --icons'

# menuselect bindings
bindkey '^I' autosuggest-accept

typeset -U path PATH

path=(
    "$HOME/.local/bin"
    "$HOME/.config/emacs/bin"
    $path
)

[[ -n "$TERM" ]] && fastfetch

# zprof
