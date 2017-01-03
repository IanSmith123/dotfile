
" All system-wide defaults are set in $VIMRUNTIME/debian.vim and sourced by
" the call to :runtime you can find below.  If you wish to change any of those
" settings, you should do it in this file (/etc/vim/vimrc), since debian.vim
" will be overwritten everytime an upgrade of the vim packages is performed.
" It is recommended to make changes after sourcing debian.vim since it alters
" the value of the 'compatible' option.

" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages available in Debian.
runtime! debian.vim
""""""""""""""""""""
"NOTE:sign of by: Ian"
"Because the backspace can not work here, and guess it because of this 
"script is for My linux mint, cinnamon 18, and the version is vim 7.4,
"but in windows, version is vim8.0, compare with the vimrc in windowns,
"I find this difference, and add it to here.
if has('win32')
	source $VIMRUNTIME/vimrc_example.vim
	source $VIMRUNTIME/mswin.vim
	behave mswin
endif
" Uncomment the next line to make Vim more Vi-compatible
" NOTE: debian.vim sets 'nocompatible'.  Setting 'compatible' changes numerous
" options, so any other options should be set AFTER setting 'compatible'.
set nocompatible

" Vim5 and later versions support syntax highlighting. Uncommenting the next
" line enables syntax highlighting by default.
if has("syntax")
  syntax on
endif

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
"set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
"if has("autocmd")
"  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
"endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
"if has("autocmd")
"  filetype plugin indent on
"endif

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.
"set showcmd		" Show (partial) command in status line.
"set showmatch		" Show matching brackets.
"set ignorecase		" Do case insensitive matching
"set smartcase		" Do smart case matching
"set incsearch		" Incremental search
"set autowrite		" Automatically save before commands like :next and :make
"set hidden		" Hide buffers when they are abandoned
set mouse=a		" Enable mouse usage (all modes)

" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif


"for vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
"Plugin 'tpope/vim-fugitive'
"Plugin 'L9'
"Plugin 'git://git.wincent.com/command-t.git'
"Plugin 'rstacruz/sparkup', {'rtp':'vim/'}
"Plugin 'ascenator/L9', {'rtp':'newL9'}

"Plugin 'altercation/solarized'
Plugin 'ervandew/supertab'
"Plugin 'kien/rainbow_parentheses.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/nerdcommenter'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'tpope/vim-surround'
"Plugin 'scrooloose/syntastic'
Plugin 'luochen1990/rainbow'
Plugin 'vim-scripts/AutoClose'
"for vim markdown
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
"for snipmate
Plugin 'MarcWeber/vim-addon-mw-utils'
Plugin 'tomtom/tlib_vim'
Plugin 'garbas/vim-snipmate'
Plugin 'Solarized'
"vim chat of Tux
"Plugin 'wsdjeg/vim-chat'

call vundle#end() 
filetype plugin indent on

"set by ian

imap aa <esc>
imap jk <RIGHT>
set nu
set ci
set fencs=utf-8,gbk,gb2312,cp936
colo solarized
set ts=4
set softtabstop=4
set shiftwidth=4
set guifont=Ubuntu\ mono:h14
"set ai





"for nerdtree
map NE :NERDTreeToggle<cr>
autocmd bufenter * if(winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif


"for rainbow
let g:rainbow_active = 1

"for solarized"
let g:solarized_italic=0
"
function! ToggleBackground()
	if (w:solarized_style=="dark")
		let w:solarized_style="light"
	colorscheme solarized
else
	let w:solarized_style="dark"
	colorscheme solarized
endif
endfunction
command! Togbg call ToggleBackground()
nmap <F5> :call ToggleBackground()<CR>
imap <F5> <ESC>:call ToggleBackground()<CR>a
vnoremap <F5> <ESC>:call ToggleBackground()<CR>

""""""""""""""""""""""""""""""""
"for syntastic
""set statusline+=%#warningmsg#
""set statusline+=%{SyntasticStatuslineFlag()}
""set statusline+=%*

""let g:syntastic_always_populate_loc_list = 1
""let g:syntastic_auto_loc_list = 1
""let g:syntastic_check_on_open = 1
""let g:syntastic_check_on_wq = 0


"""""""""""""""""""""""""""""""""""
"for air line when there is only one window, replace buffer
""set laststatus=2


"""""""""""""""""""""""""""""""""""""""""""""
"for vim markdown
let g:vim_markdown_folding_disabled = 1

"for markdown preview plus"
"let g:table_mode_corner="|"
""nmap <Leader>ch :update<Bar>silent ! start %:p<CR>
"
""""""""""""""""""""""""""""""""""""
"for Airline-theme"
let g:airline_theme='bubblegum'

""""""""""""""""""""""""""
"for vim airline"
"let g:airline#extensions#tabline#enabled = 1



""""""""""""""""""""""""""""""""""""""
" for taglist.vim"
let Tlist_Inc_Winwidth=0
let Tlis_File_Fold_Auto_Close=1
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
map TG :TlistToggle<CR>

