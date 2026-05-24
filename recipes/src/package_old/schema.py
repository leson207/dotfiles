from .enumeration import Relationship, Scope, Repo

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

class Package(BaseModel):
    name: str
    repo: Repo
    version: Optional[str]=None

    units: list[Unit] = Field(default_factory=list)

    # separate shared and owned file?
    # separate config and data file?
    multi_user_config: list[str] = Field(default_factory=list)
    single_user_config: list[str] = Field(default_factory=list)

    users: list[str] = Field(default_factory=list)
    groups: list[str] = Field(default_factory=list)
    environment_variable: list[str] = Field(default_factory=list)

    supporters: Optional[list[Package]] = Field(default_factory=list)

class Module(BaseModel):
    name: str
    relationship: Relationship = Relationship.ALTERNATIVE
    recipes: list[Package] | list[Module]
