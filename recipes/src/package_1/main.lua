local test = require("test")

local function leaf_process(t)
    print(t[1])
end

local function dfs(t)
    for key, val in pairs(t) do
        print(key)

        if(val[1]==nil) then
            dfs(val)
        else
            leaf_process(val)
        end
    end
end

dfs(test)
print(type(test.locale.systemd[1]))
