dofile("utils.lua")

local M={
    keylogger={
        {
            sub_recipes={
                {
                    package={"logkeys", Repo.AUR}
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"whatpulse", Repo.AUR}
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"osa", Repo.AUR}
                }
            }
        },
        {
            sub_recipes={
                {
                    package={"keymouse-logger", Repo.AUR}
                }
            }
        },
    },

    misc={
        {
            sub_recipes={
                {
                    package={"broot", Repo.AOR},
                },
                {
                    package={"dust", Repo.AOR},
                },
                {
                    package={"dua-cli", Repo.AOR},
                },
                {
                    package={"progress", Repo.AOR},
                },
                {
                    package={"broot", Repo.AOR},
                },
            }
        }
    }
}
