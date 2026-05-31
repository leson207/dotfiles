Repo={
    AOR = "Arch official repo",
    AUR = "Arch user repo",
    UNKNOWN = "Unknown",
    GITHUB = "Github",
    GITLAB = "Gitlab",
    CODEBERG = "Codeberg"
}

Scope={
    MULTI_USER = "multi-user",
    SINGLE_USER = "single-user",
    UNKNOWN = "unknown"
}

Relationship={
    NONE = "none",
    ALTERNATIVE = "alternative",
    ASSOCIATED = "associated",
    SUPPORT = "support"
}

-- local function format_name(s)
--     local map = {
--         seven_zip    = "7-zip",
--         libcpp       = "libc++",
--         libcppabi    = "libc++abi",
--         libcstdpp    = "libcstd++",
--         libcstdppabi = "libcstd++abi",
--     }
--
--     return map[s] or s:gsub("_", "-")
-- end
--
-- local function inject_names(tbl)
--     for k, v in pairs(tbl) do
--         if type(v) == "table" and v.repo then
--             v.name = k
--         end
--
--         if type(v) == "table" then
--             inject_names(v)
--         end
--     end
-- end

