source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
behave mswin

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      if empty(&shellxquote)
        let l:shxq_sav = ''
        set shellxquote&
      endif
      let cmd = '"' . $VIMRUNTIME . '\diff"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3
  if exists('l:shxq_sav')
    let &shellxquote=l:shxq_sav
  endif
endfunction

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"edit by iansmith
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
    nnoremap <F5> :call ToggleBackground()<CR>
    inoremap <F5> <ESC>:call ToggleBackground()<CR>a
    vnoremap <F5> <ESC>:call ToggleBackground()<CR>



imap ff <esc>
imap jk <right>
set ts=4
colo solarized
set guifont=Ubuntu\ mono:h14
set ci
set sw=4
set ts=4
set nu
set fileencodings=utf-8,GBK,gb2312,cp936
set termencoding=utf-8
"set encoding=utf-8
"
""""""""""""""""""""""""""""""""""
"for pathogen
call pathogen#infect()
call pathogen#helptags()

"""""""""""""""""""""""""""
"for indentline
" Vim
let g:indentLine_color_term = 239

"GVim
"let g:indentLine_color_gui = '#176361'
""""""""""""""""""""""""""""""""
"for rainbow
let g:rainbow_active = 1

"""""""""""""""""""""""""""""""""""
"for nerd tree
"close nerd tree if this is the last window
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") &&b:NERDTree.isTabTree()) | q | endif

" open nerd tree automatically when vim starts up
" comment bellow because I add winManager
map NE :NERDTreeToggle<CR>
"autocmd vimenter * NERDTree

""""""""""""""""""""""""""""""
"for syntastic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
"let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

""""""""""""""""""""""""""""

""""""""""""""""""""""""""
"for WinManger
"let g:winManagerWindowLayout = 'NERDTree'
"g:winManagerWindowLayout =
"let g:winManagerWindowLayout = 'FileExplorer,nerdtree|TagsExplorer'
"let g:winManagerWindowLayout = 'FileExplorer,BufExplorer|TagsExplorer'
"exit when it is the last window
"let g:persistentBehaviour:
