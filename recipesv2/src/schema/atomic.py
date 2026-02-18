from src.schema.enumeration import Scope, Repo, Shell

from typing import Literal, Optional
from pydantic import BaseModel, Field


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
    # should we use list[list[str]] instead of list[str]
    apply: list[list[str]] # ["systemctl", "--user", "enable", "pipewire.service"]
    remove: list[list[str]] # ["systemctl", "--user", "disable", "pipewire.service"]
    # disable may not true since it initial state of it(preset) may "enable"
    description: Optional[str]=None

# package in action
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


class PackageRecipe(BaseModel):
    name: str
    repo: Repo
    version: Optional[str]=None

    units: list[Unit] = Field(default_factory=list)
    scripts: list[Script] = Field(default_factory=list)
    multi_user_config: list[str] = Field(default_factory=list)
    single_user_config: list[str] = Field(default_factory=list)

    supporters: Optional[list[PackageRecipe]] = Field(default_factory=list)

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
        supporters: Optional[list[PackageRecipe]] = None
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

class TopicRecipe(BaseModel):
    name: str
    recipes: list[PackageRecipe] | list[TopicRecipe]
    # relationship: Optional[Literal["alternative", "coexist"]]

    # list[PackageRecipe] show alternative relationship, recipes of same use case, only 1 have effect at a time
    # list[TopicRecipe] show equal relationship, recipes that can coexist

    # @field_validator("recipes")
    # def unique_recipes(cls, v: list["PackageRecipe"]) -> list["PackageRecipe"]:
    #     seen = set()
    #     for recipe in v:
    #         name = recipe.core.package.name
    #         if name in seen:
    #             raise ValueError(f"Duplicate PackageRecipe for package: {name}")
    #         seen.add(name)
    #     return v

