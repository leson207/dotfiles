let mapleader = " "

function! s:CopyVisualToClipboard()
  let old_reg = getreg('"')
  let old_regtype = getregtype('"')
  normal! gv"+y
  call setreg('"', old_reg, old_regtype)
endfunction

vnoremap <silent> <leader>y :<C-u>call <SID>CopyVisualToClipboard()<CR>

nnoremap q :q<CR>
inoremap jk <Esc>
set clipboard=unnamedplus

let &t_SI = "\e[6 q"
let &t_EI = "\e[2 q"
