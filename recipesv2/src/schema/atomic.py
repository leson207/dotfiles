from src.schema.enumeration import Relationship, Scope, Repo, Shell

from typing import Optional
from pydantic import BaseModel, Field


class Unit(BaseModel):
    name: str
    scope: Scope

    def __init__(self, name: str, scope: Scope):
        super().__init__(
            name=name,
            scope=scope
        )

class Script(BaseModel):
    # do we need this or just save all kind of find
    shell: Shell
    # should we use list[list[str]] instead of list[str]
    apply: list[list[str]] # ["systemctl", "--user", "enable", "pipewire.service"]
    remove: list[list[str]] # ["systemctl", "--user", "disable", "pipewire.service"]
    # disable may not true since it initial state of it(preset) may "enable"
    description: Optional[str]=None
    succress_state: Optional[str]=None

class Package(BaseModel):
    name: str
    repo: Repo
    version: Optional[str]=None

    units: list[Unit] = Field(default_factory=list)
    scripts: list[Script] = Field(default_factory=list)

    # separate shared and owned file?
    multi_user_config: list[str] = Field(default_factory=list)
    single_user_config: list[str] = Field(default_factory=list)

    users: list[str] = Field(default_factory=list)
    groups: list[str] = Field(default_factory=list)
    environment_variable: list[str] = Field(default_factory=list)

    supporters: Optional[list[Package]] = Field(default_factory=list)

    def __init__(
        self,
        name: str,
        repo: Repo,
        version: Optional[str] = None,
        *,
        units: Optional[list[Unit]] = None,
        scripts: Optional[list[Script]] = None,
        multi_user_config: Optional[list[str]] = None,
        single_user_config: Optional[list[str]] = None,
        supporters: Optional[list[Package]] = None
    ):
        super().__init__(
            name=name,
            repo=repo,
            version=version,
            units=units or [],
            scripts=scripts or [],
            multi_user_config=multi_user_config or [],
            single_user_config=single_user_config or [],
            supporters=supporters or []
        )

class Topic(BaseModel):
    name: str
    relationship: Relationship = Relationship.ALTERNATIVE
    recipes: list[Package] | list[Topic]

class Module(BaseModel):
    name: str
    relationship: Relationship = Relationship.ALTERNATIVE
    recipes: list[Package] | list[Topic]
