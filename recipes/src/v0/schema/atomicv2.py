from src.schema.enumeration import Relationship, Scope, Repo, Shell

from typing import Optional
from pydantic import BaseModel, Field


class Package(BaseModel):
    name: str
    repo: Repo
    version: Optional[str]=None

class Unit(BaseModel):
    name: str
    scope: Scope

class Script(BaseModel):
    shell: Shell
    # should we use list[list[str]] instead of list[str]
    apply: list[list[str]] # ["systemctl", "--user", "enable", "pipewire.service"]
    remove: list[list[str]] # ["systemctl", "--user", "disable", "pipewire.service"]
    # disable may not true since it initial state of it(preset) may "enable"
    description: Optional[str]=None
    success_state: Optional[str]=None

class PackageConfig(BaseModel):
    # should i add package direct in here
    package: Package

    units: list[Unit] = Field(default_factory=list)
    scripts: list[Script] = Field(default_factory=list)
    multi_user_config: list[str] = Field(default_factory=list)
    single_user_config: list[str] = Field(default_factory=list)
    # users: list[str] = Field(default_factory=list)
    # groups: list[str] = Field(default_factory=list)
    # environment_variable: list[str] = Field(default_factory=list)
    # supporter: list[PackageConfig] = Field(default_factory=list)

class Recipe(BaseModel):
    name: str
    packages: list[PackageConfig]

class Bundle(BaseModel):
    name: str
    relationship: Relationship
    recipes: list[Recipe] | list[Bundle]


Recipe(
    name="boot",
    packages=[
        PackageConfig(
            package=Package(name="linux", repo=Repo.OFFICIAL),
            multi_user_config=["/boot/loader/entries/arch.conf"],
        )
    ]
)

# boot:
#     - kerner:
#         - linux, linux-headers, /boot/loader/entries/arch.conf
#         - linux-zen, linux-zen-headers, /boot/loader/entries/arch-zen.conf
#
#     - microcode:
#         - intel-ucode
#
#     - boot-manager:
#         - efibootmgr
