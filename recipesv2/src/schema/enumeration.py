from enum import Enum


class Repo(str, Enum):
    OFFICIAL = "official"
    AUR = "aur"
    UNKNOWN = "unknown"

class Scope(str, Enum):
    MULTI_USER = "multi-user"
    SINGLE_USER = "single-user"
    UNKNOWN = "unknown"

    # Maybe shared and instance

class Shell(str, Enum):
    BASH = "bash"
    ZSH = "zsh"
    FISH = "fish"
    NUSHELL = "nushell"
