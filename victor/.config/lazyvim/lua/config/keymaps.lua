-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

vim.keymap.set("i", "jk", "<Esc>", { noremap = true, silent = true })
-- Alt+h moves cursor left in insert mode
vim.keymap.set("i", "<A-h>", "<Left>", { desc = "Cursor Left", silent = true })
-- Alt+l moves cursor right in insert mode
vim.keymap.set("i", "<A-l>", "<Right>", { desc = "Cursor Rightj", silent = true })

vim.keymap.set('v', '<leader>y', function()
	local old_unnamed = vim.fn.getreg('"')
	vim.cmd('normal! "+y')
	vim.fn.setreg('"', old_unnamed)
end, { noremap = true, silent = true, desc = 'Copy to clipboard without affecting registers' })

vim.keymap.set('n', '<leader>cy', function()
	vim.diagnostic.open_float()
	vim.diagnostic.open_float()
	local win_id = vim.fn.win_getid()    -- get the window ID of the floating window
	vim.cmd("normal! j")                 -- move down one row
	vim.cmd("normal! VG")                -- select everything from that row down
	vim.cmd("normal! \"+y")                 -- yank selected text
	vim.api.nvim_win_close(win_id, true) -- close the floating window by its ID
	print("Copy diagnostics info to clipboard")
end, { noremap = true, silent = true, desc = "Copy diagnostics info to clipboard" })

vim.keymap.set('t', '<leader>ty', function ()
	local bufnr = vim.api.nvim_get_current_buf()
	local lines = vim.api.nvim_buf_get_lines(bufnr, 0, -1, false)
	local start_line = 1

	-- adjust this pattern to your shell prompt
	for i = #lines-4, 1, -1 do
		if string.match(lines[i], " ~") then
		start_line = i
		break
		end
	end
	local output = table.concat(vim.list_slice(lines, start_line, #lines-4), "\n")
	vim.fn.setreg('+', output)
	print("Copy last command output to clipboard")
end, { noremap = true, silent = true, desc = "Copy last command output to clipboard"})
