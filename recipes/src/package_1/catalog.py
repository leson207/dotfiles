from enum import Enum
from types import SimpleNamespace
from dataclasses import dataclass, field


class Repo(Enum):
    AOR="arch official repository"
    AUR="arch user repository"
    GITHUB="github"

class Scope(Enum):
    MULTI_USER="multi user"
    SINGLE_USER="single user"

class PackageManager(Enum):
    SYSTEM="system package manager"

class Tag(Enum):
    C_LIBRARY="c library"
    INIT_SYSTEM="init system"
    AUTHENTICATOR="authenticator"
    PACKAGE_MANAGER=PackageManager
    MIRROR_FILTER="mirror filter"
    KERNEL="kernel"
    HEADERS="headers"

@dataclass()
class Package:
    name: str
    repo: Repo
    tags: list[Tag]
    configs: dict[str, list[str]] = field(default_factory=Dict)


configs=SimpleNamespace(
    default=["/etc/sudoers.d/10-foo"]
)

# db = SimpleNamespace(
#     sudo=Package(
#         name="sudo",
#         repo=Repo.AOR,
#         tags=[Tag.AUTHENTICATOR],
#         configs={"default": ["/etc/sudoers.d/10-foo"]}
#     )
# )

db = SimpleNamespace(
    sudo=Package(
        name="sudo",
        repo=Repo.AOR,
        tags=[Tag.AUTHENTICATOR],
        configs=SimpleNamespace(default=["/etc/sudoers.d/10-foo"])
    )
)
they say python and lua is flexible and then when coding the hint is as much as the code
