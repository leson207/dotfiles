from box import Box
from src.v5.schema import Recipe, CORE, EXTRA, USER

base=Box()

base.sdk=Box(
    pkg=[
        ["git", EXTRA],

        ["make", EXTRA],
        ["gcc", EXTRA],
        ["gdb", EXTRA],

        ["uv", EXTRA],
    ],
)
