from src.v2.enumeration import Repo, Scope, Tag
from dataclasses import dataclass, field


@dataclass
class Unit:
    name: str
    scope: Scope

@dataclass
class PkgSpec:
    name: str
    repo: Repo
    tags: list[Tag]

    units: dict[str, Unit] = field(default_factory=dict)
    configs: dict[str, list[str]] = field(default_factory=dict)
    env_vars: list[list[str]] = field(default_factory=list)
    auto_start: list[list[str]] = field(default_factory=list)

@dataclass
class PkgVar:
    pkg: PkgSpec
    units: list[Unit] = field(default_factory=list)
    configs: list[str] = field(default_factory=list)

@dataclass
class PkgRecipe:
    core: PkgVar
    enhancer: list[PkgRecipe] = field(default_factory=list)
    # installation: list[list[str]] = field(default_factory=list)
    # core package with it extended/support/optional package

@dataclass
class UsageRecipe:
    recipes: list[PkgRecipe]
    # configs: list[str] = field(default_factory=list)
    # installation: list[list[str]] = field(default_factory=list)
