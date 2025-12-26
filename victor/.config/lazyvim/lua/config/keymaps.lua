-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

vim.keymap.set("i", "jk", "<Esc>", { noremap = true, silent = true })
-- Alt+h moves cursor left in insert mode
vim.keymap.set("i", "<A-h>", "<Left>", { desc = "Cursor Left", silent = true })
-- Alt+l moves cursor right in insert mode
vim.keymap.set("i", "<A-l>", "<Right>", { desc = "Cursor Rightj", silent = true })

--   vim.fn.setreg('"', saved_reg, saved_regtype)  -- restore unnamed register
-- end, { noremap = true, silent = true, desc = 'Copy to clipboard without affecting registers' })
-- vim.keymap.set('v', '<leader>y', function()
--   local saved_reg = vim.fn.getreg('"')
--   local saved_regtype = vim.fn.getregtype('"')
--
--   vim.cmd('normal! "+y')  -- yank to system clipboard
--
--   vim.fn.setreg('"', saved_reg, saved_regtype)  -- restore with type
-- end, { noremap = true, silent = true, desc = 'Copy to clipboard without affecting registers' })

vim.keymap.set('v', '<leader>y', function()
	local old_unnamed = vim.fn.getreg('"')
	vim.cmd('normal! "+y')
	vim.fn.setreg('"', old_unnamed)
end, { noremap = true, silent = true, desc = 'Copy to clipboard without affecting registers' })
--
-- vim.keymap.set({'n', 'i', 't'}, '<leader>p', function()
-- 	local old_unnamed = vim.fn.getreg('"')
--
-- 	local mode = vim.fn.mode()
-- 	if mode == 'n' or mode=='i' then
-- 		vim.cmd('normal! "+p')
-- 	elseif mode == 't' then
-- 		local clip = vim.fn.getreg('+')  -- system clipboard
-- 		vim.api.nvim_feedkeys(clip, 't', false)   -- sends text to terminal input
-- 	end
--
-- 	vim.fn.setreg('"', old_unnamed)  -- restore unnamed register
-- end, { noremap = true, silent = true, desc = 'Paste from system clipboard' })

