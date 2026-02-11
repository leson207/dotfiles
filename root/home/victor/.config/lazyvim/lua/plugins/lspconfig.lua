return {
    "neovim/nvim-lspconfig",
    opts = {
        servers = {
            harper_ls = {
                excludePatterns = {"*.cpp", "*.hpp", "*.c", "*.h"}
            },
        },
    },
}
