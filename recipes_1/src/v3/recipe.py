from box import Box

from src.v3.schema import Unit, PkgRecipe, UsageRecipe
from src.v3.enumeration import Scope
from src.v3.catalog import db


app=Box(
    # shell=UsageRecipe(
    #     [
    #         PkgRecipe(db.zsh, configs=["~/.zsh"]),
    #         PkgRecipe(db.starship, configs=["~/.config/starship.toml"]),
    #         PkgRecipe(db.fd),
    #         PkgRecipe(db.fzf),
    #         PkgRecipe(db.skim),
    #         PkgRecipe(db.ripgrep),
    #         PkgRecipe(db.bat),
    #         PkgRecipe(db.git_delta),
    #         PkgRecipe(db.diffstatic),
    #         PkgRecipe(db.eza),
    #         PkgRecipe(db.zoxide),
    #         PkgRecipe(db.duf),
    #         PkgRecipe(db.dust),
    #         PkgRecipe(db.broot),
    #
    #         PkgRecipe(db.gping),
    #         PkgRecipe(db.rustscan),
    #         PkgRecipe(db.jq),
    #         PkgRecipe(db.yq),
    #         PkgRecipe(db.hyperfind),
    #         PkgRecipe(db.navi),
    #         PkgRecipe(db.direnv),
    #         PkgRecipe(db.nnn),
    #     ]
    # ),
)
