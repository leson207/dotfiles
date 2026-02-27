from src.schema.enumeration import Repo
from src.schema.atomic import Package
from src.schema.recipe import Recipe

package=[
    Package(name="linux", repo=Repo.OFFICIAL),
    Package(name="linux-headers", repo=Repo.OFFICIAL),
    Package(name="linux-zen", repo=Repo.OFFICIAL),
    Package(name="linux-zen-headers", repo=Repo.OFFICIAL),
    Package(name="intel-ucode", repo=Repo.OFFICIAL),
]

files=[
    "/boot/loader/entries/arch.conf",
    "/boot/loader/entries/arch-zen.conf",
]
