local core = require("core")

local packages={}
local configs={}
local units={}
local groups={}
local env_variables={}
local auto_start={}


-- workflow
-- package
-- groups
-- env ? not know how uwsm
-- auto_start? not know how, hyprland
-- clean old file if conflic
-- sub_recipes config
-- big reripes config

local function print_packages()
    for _, pkg in ipairs(packages) do
        print(pkg[1])
    end
end

local function print_configs()
    for _, config in ipairs(configs) do
        for _, tmp in ipairs(config) do
            if type(tmp) == "string" then
                print(tmp)
            else
                for _, x in ipairs(tmp) do
                    io.write(x, " ")
                end
                io.write("\n")
            end
        end
    end
end

local function extract(t)
    if t.package ~= nil then
        table.insert(packages, t.package)
    end

    if t.units ~= nil then
        table.insert(units, t.units)
    end

    if t.multi_user_config ~= nil then
        table.insert(configs, t.multi_user_config)
    end

    if t.single_user_config ~= nil then
        table.insert(configs, t.single_user_config)
    end

    if t.groups ~= nil then
        table.insert(groups, t.groups)
    end

    if t.env ~= nil then
        table.insert(env_variables, t.env)
    end

    if t.auto_start ~= nil then
        table.insert(auto_start, t.auto_start)
    end

end

local function tmp(t)
    print("Hello world!\n");

    local stack_1 = {t}
    local stack_2 = {}

    while #stack_1>0 do
        local e=table.remove(stack_1)

        for key, value in pairs(e) do
            if type(key)=="string" then
                table.insert(stack_1, value)
            else
                table.insert(stack_2, value)
            end
        end
    end

    -- care to the execution order
    while #stack_2>0 do
        local v=table.remove(stack_2);

        extract(v)
        if v.sub_recipes ~= nil then
            for _, item in ipairs(v.sub_recipes) do
                extract(item)
            end
        end
    end
end

tmp(core[2])

print_packages()
-- print_configs()
