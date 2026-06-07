from typing import Optional
from src.v4.enumeration import Scope
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Unit:
    name: str
    scope: Scope

# @dataclass(frozen=True)
# class Config:
#     source: str
#     content: str
#     destination: str

@dataclass(frozen=True)
class PackageManager:
    name: str
    install_cmd: tuple[str, ...]

@dataclass(frozen=True)
class Install:
    source: str
    package_manager: Optional[PackageManager] = None
    bootstrap: list[list[str]] = field(default_factory=list)

@dataclass(frozen=True)
class PkgRecipe:
    name: str
    installation: Install

    # extra=helper + extension
    extra: list[PkgRecipe] = field(default_factory=list)

    configs: list[str] = field(default_factory=list)
    units: list[Unit] = field(default_factory=list)
    groups: list[str] = field(default_factory=list)
    env_vars: list[list[str]] = field(default_factory=list)
    auto_start: list[list[str]] = field(default_factory=list)
    bootstrap: list[list[str]] = field(default_factory=list)

@dataclass(frozen=True)
class UsageRecipe:
    recipes: list[PkgRecipe]
    # configs: list[str] = field(default_factory=list)
    installation: list[list[str]] = field(default_factory=list)

