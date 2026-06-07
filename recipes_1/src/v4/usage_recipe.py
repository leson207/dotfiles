from box import Box

from src.v4.schema import Unit, Install, PkgRecipe, UsageRecipe
from src.v4.enumeration import Scope
from src.v4.package_recipe import x


base=Box(
    package_manager=UsageRecipe(
        [
            x.systemd_boot,
            x.linux
        ]
    ),
)
#
# x.git=PkgRecipe(
#     "git",
#     CommonInstaller.AER,
#     [
#         PkgRecipe("bat", CommonInstaller.AER),
#         PkgRecipe("git-delta", CommonInstaller.AER)
#     ],
#     configs=["~/.gitconifig"],
#     bootstrap=[
#         ["git", "config", "--global", "user.name", "leson207"],
#         ["git", "config", "--global", "user.email", "sonthaile2002"],
#         ["git", "config", "--global", "core.pager", "bat --paging=always"],
#         ["git", "config", "--global", "interactive.diffFilter", "delta --color-only"],
#         ["git", "config", "--global", "delta.navigate", "true"],
#         ["git", "config", "--global", "delta.dark", "true"],
#         ["git", "config", "--global", "merge.conflictStyle", "zdiff3"],
#         ["git", "config", "--global", "--list"],
#     ]
# )
