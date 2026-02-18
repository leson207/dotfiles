# class Unit:
from _typeshed import structseq

from schema.atomic import TopicRecipe


class Script:
    shell: str
    desc: str
    apply: str
    remove: str
    success_state: list # eg: some file exist

class PackageConfig:
    name: str
    repo: str
    units: list
    scripts: list

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
