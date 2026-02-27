from src.schema.enumeration import Scope, Repo, Shell

from typing import Optional
from pydantic import BaseModel


class Package(BaseModel):
    name: str
    repo: Repo
    version: Optional[str]=None

class Unit(BaseModel):
    name: str
    scope: Scope

    def __init__(self, name: str, scope: Scope):
        super().__init__(
            name=name,
            scope=scope
        )

class Script(BaseModel):
    shell: Shell
    apply: list[list[str]] # ["systemctl", "--user", "enable", "pipewire.service"]
    remove: list[list[str]] # ["systemctl", "--user", "disable", "pipewire.service"]
    # disable may not true since it initial state of it(preset) may "enable"
    description: Optional[str]=None
    success_state: list # eg: some file exist
