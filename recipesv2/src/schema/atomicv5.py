from src.schema.enumeration import Relationship, Scope, Repo, Shell

from typing import Optional
from pydantic import BaseModel, Field


class Unit(BaseModel):
    name: str
    scope: Scope

class Script(BaseModel):
    shell: Shell
    apply: list[list[str]]
    remove: list[list[str]]
    description: Optional[str]=None
    succress_state: Optional[str]=None

class Leaf(BaseModel):
    # topic or core package
    name: str

    repo: Optional[Repo]=None
    version: Optional[str]=None

    units: list[Unit] = Field(default_factory=list)
    scripts: list[Script] = Field(default_factory=list)
    multi_user_config: list[str] = Field(default_factory=list)
    single_user_config: list[str] = Field(default_factory=list)

    users: list[str] = Field(default_factory=list)
    groups: list[str] = Field(default_factory=list)
    environment_variable: list[str] = Field(default_factory=list)

    relationship: Relationship = Relationship.ALTERNATIVE
    recipes: Optional[list[Node]] = Field(default_factory=list)

class NodeTopic:
    name: str

class Node:
    name: str

class Edge(BaseModel):
    relationship: Relationship
    nodes: list[Node]
