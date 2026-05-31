local function readOnly(t)
    return setmetatable(t, {
        __index = function(_, key)
            error(key .. " does not exist", 2)
        end,
        __newindex = function(_, key, _)
            error("read-only, cannot set " .. key, 2)
        end
    })
end


---@enum Repo
local Repo={
    AOR="arch official repository",
    AUR="arch user repository",
    GITHUB="github",
}

---@enum Scope
local Scope={
    MULTI_USER="multi user",
    SINGLE_USER="single user",
}

---@class Tag: { [string]: string|table }
local Tag={
    C_LIBRARY="c library",
    INIT_SYSTEM="init system",
    AUTHENTICATOR="authenticator",
    PACKAGE_MANAGER={
        SYSTEM="system package manager"
    },
    MIRROR_FILTER="mirror filter",
    KERNEL="kernel",
    HEADERS="headers",
}


---@class Package
---@field name string
---@field repo Repo
---@field tags string[]
---@field configs? { [string]:  string[] }

---@class Catalog
---@class PackageCatalog: { [string]: Package }

---@type PackageCatalog
local db=readOnly({
-- Configuration model/ Feature model/ Schema
    sudo={
        name="sudo",
        repo=Repo.AOR,
        tags={Tag.AUTHENTICATOR},
        configs={
            default={"/etc/sudoers.d/10-foo"}
        }
    },
    glibc={
        name="glibc",
        repo=Repo.AOR,
        tags={Tag.C_LIBRARY},
    },
    systemd={
        name="systemd",
        repo=Repo.AOR,
        tags={Tag.INIT_SYSTEM},
        configs={
            default={
                "~/.config/systemd",
            },
        },
        units={ systemd_timesyncd_service={name="systemd-timesyncd.service", scope=Scope.MULTI_USER}, }
    },

    nix={
        name="nix",
        repo=Repo.AOR,
        tags={Tag.PACKAGE_MANAGER.SYSTEM},
    },
    pacman={
        name="pacman",
        repo=Repo.AOR,
        tags={Tag.PACKAGE_MANAGER.SYSTEM},
        -- configs={
        --     default={"/etc/pacman.conf"}
        -- },
        configs={
            "/etc/pacman.conf",
            "~/.makepkg.conf"
        }
    },
    yay={
        name="yay",
        repo=Repo.GITHUB,
        tags={Tag.PACKAGE_MANAGER.SYSTEM},
    },
    paru={
        name="paru",
        repo=Repo.GITHUB,
        tags={Tag.PACKAGE_MANAGER.SYSTEM},
    },
    reflector={
        name="reflector",
        repo=Repo.AOR,
        tags={Tag.MIRROR_FILTER},
        units={ reflector_timer={name="reflector.timer", scope=Scope.MULTI_USER}, }
    },
    linux={
        name="linux",
        repo=Repo.AOR,
        tags={Tag.KERNEL},
    },
    linux_cachyos_bore={
        name="linux-cachyos-bore",
        repo=Repo.AUR,
        tags={Tag.KERNEL},
    },
    linux_headers={
        name="linux-headers",
        repo=Repo.AOR,
        tags={Tag.HEADERS},
    },
    linux_cachyos_bore_headers={
        name="linux-cachyos-bore-headers",
        repo=Repo.AUR,
        tags={Tag.HEADERS},
    },
})

return db
