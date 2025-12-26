return {
	"stevearc/conform.nvim",
	optional = true,
	---@module "conform"
	---@type conform.formatopts
	opts = {
    	formatters_by_ft = {
    		lua = {},
    		-- * matches all filetypes
    		["*"] = { "trim_whitespace" },
		},
	},
}
