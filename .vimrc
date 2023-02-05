syntax on

call plug#begin()

Plug 'preservim/NERDTree'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'doums/darcula'
Plug 'gpanders/vim-oldfiles'
Plug 'tpope/vim-fugitive'
Plug 'junegunn/fzf'
Plug 'dense-analysis/ale'
Plug 'mbbill/undotree'
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'vim-syntastic/syntastic'
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/nvim-cmp' 
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'williamboman/nvim-lsp-installer'
Plug 'puremourning/vimspector'
Plug 'mfussenegger/nvim-jdtls'
Plug 'artur-shaik/jc.nvim'

call plug#end()

colorscheme darcula

augroup oldfiles
	    autocmd!
	        autocmd FileType qf if get(w:, 'quickfix_title') =~# 'Oldfiles' | nnoremap <buffer> <CR> <CR>:cclose<CR> | endif
augroup END

" <tab> to trigger completion and navigate to the next complete item
function! CheckBackspace() abort
	  let col = col('.') - 1
	    return !col || getline('.')[col - 1]  =~# '\s'

endfunction

lua require('jc').setup{}

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

" Toggle NerdTree
nmap <F1> :NERDTreeToggle<CR>
nmap <F2> :NERDTreeFocus<CR>
" Toggle UndoTree 
nmap <F3> :UndotreeToggle<CR>
" Open a Terminal within the current working directory.
nmap <F4> :let $VIM_DIR=expand('%:p:h')<CR>:term ++close<CR>cd $VIM_DIR<CR>
" Run the RunFile Function (Java and Python)
nmap <F5> :call RunFile()<CR>
" Compile Java Files
nmap <F6> :call CompileJavaFile()<CR>


func! RunFile()
exec "w"
if &filetype == "java"
	exec "!java %"
elseif &filetype == "python"
	exec "!python3 %"
elseif &filetype == "sh"
	exec "!time bash %"
elseif &filetype == "c"
	exec "!gcc % -o %<"
	exec "!time ./%<"
endif
endfunction

func! CompileJavaFile()
exec "w"
if &filetype == "java"
	exec "!echo Compiling Java File... | javac % | echo Compiled Java File Successfully"
endif
endfunction 


set number
set scrolloff=8
set termwinsize=12x200
let g:airline_theme='transparent'

inoremap <silent><expr> <Tab>
      \ coc#pum#visible() ? coc#pum#next(1) :
            \ CheckBackspace() ? "\<Tab>" :
	          \ coc#refresh()
