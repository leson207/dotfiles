from box import Box
from src.recipe.schema import Recipe, EXTRA

base=Box()

base.sdk=Recipe(
    pkg=[
        ["git", EXTRA],

        ["make", EXTRA],
        ["gcc", EXTRA],
        ["gdb", EXTRA],
        ["bear", EXTRA],

        ["man-db", EXTRA],
        ["man-pages", EXTRA],

        ["uv", EXTRA],
    ],
)
