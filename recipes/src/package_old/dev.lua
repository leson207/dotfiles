dofile("utils.lua")

local M={
    version_control_system={
        {
            sub_recipes={
                {
                    package={"git", Repo.AOR},
                    single_user_config={"~/.gitconfig"},
                },
                {
                    package={"less", Repo.AOR}
                },
                {
                    package={"delta", Repo.AOR}
                },
            }
        },
        -- {
        --     sub_recipes={
        --         {
        --             package={"jujutsu", Repo.AOR}
        --         }
        --     }
        -- }
    },

    editor={
        tui={
            {
                sub_recipes={
                    {
                        package={"neovim", Repo.AOR}
                    },
                    {
                        package={"luarocks", Repo.AOR}
                    }
                }
            },
        },
    },


    virtual_machine={
        {
            sub_recipes={
                {
                    package={"libvirt", Repo.AOR},
                    units={"libvirtd.service", scope=Scope.MULTI_USER},
                },
                {
                    package={"qemu-desktop", Repo.AOR}
                },
                {
                    package={"dnsmasq", Repo.AOR}
                },
                {
                    package={"virt-manager", Repo.AOR}
                },
                {
                    package={"virt-viewer", Repo.AOR}
                },
            }
        }
    },

    -- download={
    --     {
    --         sub_recipes={
    --             {
    --                 package={"aria2", Repo.AOR},
    --                 single_user_config={"~/.config/aria2"}
    --             },
    --             {
    --                 package={"yt-dlp", Repo.AOR},
    --                 single_user_config={"~/.config/yt-dlp"}
    --             }
    --         }
    --     }
    -- },

    common={
        {
            sub_recipes={
                {
                    package={"tree", Repo.AOR},
                },
                {
                    package={"rsync", Repo.AOR},
                },
                {
                    package={"fastfetch", Repo.AOR},
                },
                {
                    package={"fd", Repo.AOR},
                },
                {
                    package={"fzf", Repo.AOR},
                },
                {
                    package={"ripgrep", Repo.AOR},
                },
                {
                    package={"bat", Repo.AOR},
                },
                -- {
                --     package={"eza", Repo.AOR},
                -- },
                -- {
                --     package={"zoxide", Repo.AOR},
                -- },
            }
        }
    },
}

return M
