from dataclasses import dataclass, field

USER="user"
CORE="core"
EXTRA="extra"

@dataclass
class Recipe:
    pkg: list[list] = field(default_factory=list)
    config: list[str | list] = field(default_factory=list)
    data: list = field(default_factory=list)
    env: list = field(default_factory=list)
    group: list = field(default_factory=list)
    auto_start: list = field(default_factory=list)
    update: list = field(default_factory=list)
    manual: bool = False
