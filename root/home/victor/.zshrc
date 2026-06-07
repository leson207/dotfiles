# =============================================================================
# ~/.zshrc — minimal, polished zsh setup
# Stack: Zinit · Starship · tmux · fzf · zoxide
# =============================================================================


# -----------------------------------------------------------------------------
# 0. INSTANT PROMPT (keep at very top — Starship variant)
# -----------------------------------------------------------------------------
# Nothing above this except env vars that must be set before shell init


# -----------------------------------------------------------------------------
# 1. ENVIRONMENT
# -----------------------------------------------------------------------------
export EDITOR=nvim
export VISUAL=nvim
export PAGER=less
export LESS='-RFX'

export PATH="$HOME/.local/bin:$HOME/bin:$PATH"

# XDG base dirs (good hygiene — keeps ~ clean)
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_STATE_HOME="$HOME/.local/state"


# -----------------------------------------------------------------------------
# 2. ZSH OPTIONS
# -----------------------------------------------------------------------------

# History
HISTFILE="$XDG_STATE_HOME/zsh/history"
HISTSIZE=100000
SAVEHIST=100000
setopt HIST_IGNORE_DUPS        # don't record duplicate consecutive entries
setopt HIST_IGNORE_ALL_DUPS    # remove older duplicate entries
setopt HIST_FIND_NO_DUPS       # skip dupes when searching
setopt HIST_SAVE_NO_DUPS
setopt HIST_REDUCE_BLANKS      # strip extra blanks
setopt INC_APPEND_HISTORY      # write to histfile immediately, not on exit
setopt SHARE_HISTORY           # share history across sessions

# Navigation
setopt AUTO_CD                 # type a dir name to cd into it
setopt AUTO_PUSHD              # cd pushes to dir stack automatically
setopt PUSHD_IGNORE_DUPS       # no duplicates in dir stack
setopt PUSHD_SILENT            # no dir stack output on cd

# Completion
setopt ALWAYS_TO_END           # move cursor to end after completion
setopt AUTO_MENU               # show menu on second tab
setopt COMPLETE_IN_WORD        # complete from both ends of a word
setopt MENU_COMPLETE

# Misc
setopt CORRECT                 # suggest corrections for mistyped commands
setopt INTERACTIVE_COMMENTS    # allow # comments in interactive shell
setopt NO_BEEP


# -----------------------------------------------------------------------------
# 3. COMPLETION SYSTEM
# -----------------------------------------------------------------------------
# Must be initialized before plugins that extend it

autoload -Uz compinit

# Only regenerate .zcompdump once per day (speeds up startup)
if [[ -n "$XDG_CACHE_HOME/zsh/zcompdump"(#qN.mh+20) ]]; then
  compinit -d "$XDG_CACHE_HOME/zsh/zcompdump"
else
  compinit -C -d "$XDG_CACHE_HOME/zsh/zcompdump"
fi

# Completion styling
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'   # case-insensitive
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*:descriptions' format '[%d]'
zstyle ':completion:*:warnings' format 'no matches for: %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' squeeze-slashes true

# Cache completions (speeds up slow completions like docker, kubectl)
zstyle ':completion:*' use-cache yes
zstyle ':completion:*' cache-path "$XDG_CACHE_HOME/zsh/zcompcache"

# Create required dirs
mkdir -p "$XDG_STATE_HOME/zsh" "$XDG_CACHE_HOME/zsh"


# -----------------------------------------------------------------------------
# 4. ZINIT — plugin manager
# -----------------------------------------------------------------------------
ZINIT_HOME="$XDG_DATA_HOME/zinit/zinit.git"

# Auto-install zinit if not present
if [[ ! -d "$ZINIT_HOME" ]]; then
  mkdir -p "$(dirname $ZINIT_HOME)"
  git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

source "$ZINIT_HOME/zinit.zsh"


# --- Plugins ---

# Fish-style inline autosuggestions — load immediately (affects every keystroke)
zinit ice wait
zinit light zsh-users/zsh-autosuggestions

# Syntax highlighting — must be loaded LAST among the three
zinit ice wait
zinit light zsh-users/zsh-syntax-highlighting

# Extended completions (adds definitions for many CLIs)
# lucid + wait = async, doesn't block startup
zinit ice lucid wait'0'
zinit light zsh-users/zsh-completions

# Better history search with arrow keys (up/down filters by prefix)
zinit ice lucid wait'0'
zinit light zsh-users/zsh-history-substring-search

# fzf-tab: replaces zsh's completion menu with fzf popup
zinit ice lucid wait'0'
zinit light Aloxaf/fzf-tab


# --- Autosuggestions config ---
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#555577'
ZSH_AUTOSUGGEST_STRATEGY=(history completion)
ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=20


# -----------------------------------------------------------------------------
# 5. KEY BINDINGS
# -----------------------------------------------------------------------------
bindkey -e   # emacs keybindings (Ctrl+A, Ctrl+E, Ctrl+W, etc.)
             # swap to -v if you prefer vi mode

# History substring search (arrow keys)
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

# Accept autosuggestion with Ctrl+Space or right arrow
bindkey '^ ' autosuggest-accept
bindkey '^[[C' autosuggest-accept   # right arrow only if at end of line

# bindkey '^I' autosuggest-accept
# bindkey '^F' expand-or-complete

# Word navigation (Ctrl+Left / Ctrl+Right)
bindkey '^[[1;5C' forward-word
bindkey '^[[1;5D' backward-word


# -----------------------------------------------------------------------------
# 6. ALIASES
# -----------------------------------------------------------------------------

# Modern replacements (install: pacman -S eza bat ripgrep fd git-delta)
alias ls='eza --icons --group-directories-first'
alias ll='eza -lah --icons --group-directories-first --git'
alias lt='eza --tree --level=2 --icons'
alias cat='bat --style=plain'
alias grep='rg'
alias find='fd'

# Git shortcuts
alias g='git'
alias gs='git status -sb'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git pull'
alias glog='git log --oneline --graph --decorate -20'
alias gd='git diff'

# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias -- -='cd -'           # go back to previous dir

# Safety
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Misc
alias reload='source ~/.zshrc'
alias path='echo $PATH | tr ":" "\n"'
alias ports='ss -tulnp'
alias myip='curl -s ifconfig.me'


# -----------------------------------------------------------------------------
# 7. FZF — fuzzy finder
# -----------------------------------------------------------------------------
# Install: pacman -S fzf

if command -v fzf &>/dev/null; then
  # Use fd as the file finder (faster, respects .gitignore)
  export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git'
  export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
  export FZF_ALT_C_COMMAND='fd --type d --hidden --follow --exclude .git'

  # Minimal dark theme
  export FZF_DEFAULT_OPTS='
    --height 40%
    --layout=reverse
    --border=sharp
    --color=bg+:#1e1e2e,bg:#13131a,spinner:#e8ff47,hl:#47d7ff
    --color=fg:#e8e8f0,header:#5a5a72,info:#e8ff47,pointer:#e8ff47
    --color=marker:#e8ff47,fg+:#e8e8f0,prompt:#e8ff47,hl+:#47d7ff
    --prompt="  " --pointer="▶" --marker="✓"
  '

  # Shell keybindings: Ctrl+T (files), Ctrl+R (history), Alt+C (dirs)
  source <(fzf --zsh)

  # fzf-tab config (preview for files/dirs)
  zstyle ':fzf-tab:complete:cd:*' fzf-preview 'eza --tree --level=1 --color=always $realpath'
  zstyle ':fzf-tab:complete:cat:*' fzf-preview 'bat --color=always $realpath'
fi


# -----------------------------------------------------------------------------
# 8. ZOXIDE — smart cd
# -----------------------------------------------------------------------------
# Install: pacman -S zoxide

if command -v zoxide &>/dev/null; then
  eval "$(zoxide init zsh)"
  # Now use: z <partial-name>   instead of cd ~/long/path/to/dir
fi


# -----------------------------------------------------------------------------
# 9. DIRENV — per-project env vars
# -----------------------------------------------------------------------------
# Install: pacman -S direnv
# Usage: echo 'export FOO=bar' > .envrc && direnv allow

# if command -v direnv &>/dev/null; then
#   eval "$(direnv hook zsh)"
# fi


# -----------------------------------------------------------------------------
# 10. TMUX — auto-attach on terminal open
# -----------------------------------------------------------------------------
# Uncomment to auto-start/attach tmux when opening a terminal
# (Skip if you launch tmux manually)

# if command -v tmux &>/dev/null && [[ -z "$TMUX" ]]; then
#   tmux attach-session 2>/dev/null || tmux new-session -s main
# fi


# -----------------------------------------------------------------------------
# 11. STARSHIP PROMPT
# -----------------------------------------------------------------------------
# Install: pacman -S starship
# Config:  ~/.config/starship.toml  (see companion file)

if command -v starship &>/dev/null; then
  eval "$(starship init zsh)"
fi

# -----------------------------------------------------------------------------
# 12. ATUIN SHELL HISTORY
# -----------------------------------------------------------------------------
# Install: pacman -S atuin
# Config:  ~/.config/atuin  (see companion file)

# if command -v atuin &>/dev/null; then
#   eval "$(atuin init zsh)"
# fi

# =============================================================================
# End of ~/.zshrc
# =============================================================================
