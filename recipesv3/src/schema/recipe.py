from src.schema.enumeration import Repo
from schema.atomic import Unit, Script, Package

from pydantic import BaseModel, Field

class PackageConfig(BaseModel):
    package: Package
    units: list[Unit] = Field(default_factory=list)
    scripts: list[Script] = Field(default_factory=list)
    multi_user_config: list[str] = Field(default_factory=list)
    single_user_config: list[str] = Field(default_factory=list)

    @classmethod
    def short(
        cls,
        name: str,
        repo: Repo,
    ) -> "PackageConfig":

        return cls(package=Package(name=name, repo=repo))

class Recipe:
    # name: str
    packages: list # tree separate for topic here
    units: list
    scripts: list
    users: list
    groups: list
    files: list
    env_variable: list
    modify: list #like ucode wil modify 1 line on entry file

class PackageTopic:
    name: str
    l: list

class Topic:
    name: str
    l: list[Recipe] | list[Topic]

# Relationship:
# - support: recipe
# - different aspect: recipe
# - altenative: ?
# boudary between what topic represent and what packageconfig represent stilll vague
# say zenity
#
# package in action

