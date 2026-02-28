from enum import Enum


# class Source(str, Enum):
class Repo(str, Enum):
    AOR = "arch official repo"
    AUR = "arch user repo"
    UNKNOWN = "unknown"
    GITHUB = "github"
    GITLAB = "gitlab"
    CODEBERG = "codeberg"

class Scope(str, Enum):
    # Maybe shared and instance
    MULTI_USER = "multi-user"
    SINGLE_USER = "single-user"
    UNKNOWN = "unknown"

class Shell(str, Enum):
    ZSH = "zsh"
    FISH = "fish"
    BASH = "bash"
    NUSHELL = "nushell"

class Relationship(str, Enum):
    NONE = "none"
    ALTERNATIVE = "alternative"
    ASSOCIATED = "associated" # related, counterpart, facet
    SUPPORT = "support"

    # depend_on, optional, provides, variant_of, integrated_with, conflicts_with, replaces

    # interchange
