vim.keymap.set('i', 'jk', '<Esc>', { noremap = true, silent = true })
vim.keymap.set({ "i", "x", "n", "s" }, "<C-s>", "<cmd>w<cr><esc>", { desc = "Save File" })
