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

class Recipe(BaseModel):
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
    recipes: Optional[list[Recipe]] = Field(default_factory=list)

Recipe(
    name="kernel",
    relationship=Relationship.ALTERNATIVE,
    recipes=[
        Recipe(
            name="linux",
            repo=Repo.OFFICIAL,
            multi_user_config=["/boot/loader/entries/arch.conf"],
            relationship=Relationship.SUPPORT,
            recipes=[Recipe(name="linux-headers", repo=Repo.OFFICIAL)]
        ),
        Recipe(
            name="linux",
            repo=Repo.OFFICIAL,
            multi_user_config=["/boot/loader/entries/arch.conf"],
            relationship=Relationship.SUPPORT,
            recipes=[Recipe(name="linux-headers", repo=Repo.OFFICIAL)]
        )
    ]
)

Recipe(
    name="graphic",
    recipes=[
        Recipe(
            name="driver",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Recipe(
                    name="mesa",
                    repo=Repo.OFFICIAL,
                    recipes=[Recipe(name="mesa-utils", repo=Repo.OFFICIAL)]
                ),
                Recipe(name="intel-media-driver", repo=Repo.OFFICIAL),

                Recipe(
                    name="video acceleration",
                    relationship=Relationship.ASSOCIATED,
                    recipes=[
                        Recipe(
                            name="libva",
                            repo=Repo.OFFICIAL,
                            recipes=[Recipe(name="libva-utils", repo=Repo.OFFICIAL)]
                        ),
                        Recipe(name="libva-intel-driver", repo=Repo.OFFICIAL),
                    ]
                )
            ]
        ),
        Recipe(
            name="rendering",
            relationship=Relationship.ASSOCIATED,
            recipes=[
                Recipe(name="vulkan-intel", repo=Repo.OFFICIAL),
                Recipe(name="vulkan-radeon", repo=Repo.OFFICIAL),
                Recipe(name="vulkan-mesa-implicit-layers", repo=Repo.OFFICIAL),
            ]
        ),

    ]
)
