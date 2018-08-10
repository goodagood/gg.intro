d" the follow is for vim (different from gvim)
set nocompatible

set shiftwidth=4  tabstop=4   "this same as ms windows policy

set autoindent


""" Vundle is short for Vimbundle and is a Vim plugin manager.:
"set rtp+=~/.vim/bundle/vundle/
"call vundle#rc()
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle
"  " required! 
Plugin 'gmarik/Vundle.vim'
"Plugin 'jelera/vim-javascript-syntax'
Plugin 'https://github.com/jelera/vim-javascript-syntax.git'

"Plugin 'mru.vim'
"Plugin 'git@github.com:yegappan/mru.git'
"Only this works:
Plugin 'https://github.com/yegappan/mru.git'

Plugin 'vim-coffee-script'
Plugin 'SuperTab'
"Plugin 'TinyBufferExplorer'
Plugin 'bufexplorer.zip'

call vundle#end()
""" End of Vundle settings


" stop the warning msg when switch buffers, (and useless 20070718)
set autowriteall

if &t_Co > 2 || has('gui_running')
  set hlsearch
  set is
endif
syntax on
" some time the search or * give un-readable hl-search, so:
":hi search ctermfg=Red  ctermbg=LightBlue

set mouse=a    	  " mouse click change cursor position
set mousehide     " hide the mouse when typing

if has('vms')       "backup option
  set nobackup
else
  set backup
endif

set et

set backupdir-=~/tmp
set backupdir+=/tmp//
set backupdir-=.
set backupdir-=~/
"set backupdir-=.
" This for swp files, the double slash (//) is need for full path swap name.
" no full path name 2015 1008
set dir-=.
set dir-=~/
"set dir-=~/tmp
"set dir-=/var/tmp
set dir+=/tmp//
"set dir+=~/.vim/tmp//
set undodir=/tmp//
set directory=/tmp//


" For chinese formation:
set formatoptions+=m
set history=200

" Easy to BufExplorer
nmap ,b  :BufExplorer<CR>
nmap ,ro :set readonly<CR>
nmap ,nro :set noreadonly<CR>

"   Edit another file in the same directory as the current file
"   uses expression to extract path from current file's path
if has("unix")
    nmap ,e :e <C-R>=expand("%:p:h") . "/" <CR>
    nmap ,w :w <C-R>=expand("%:p:h") . "/" <CR>
else
    nmap ,e :e <C-R>=expand("%:p:h") . "\" <CR>
    nmap ,w :w <C-R>=expand("%:p:h") . "\" <CR>
endif

nmap P "+p
nmap Y "+y
nmap ,t :tabe <CR>
"for tabpage use ? useless?
hi TabLineSel ctermbg=2
highlight TabLine ctermbg=1

"to check dictionary:
nmap ,d  :!/home/za/bin/dict4vim 

"easy to change the current file's mode and run it in shell.
nmap ,c  :!chmod 755 %<CR> :e<CR> :! %<CR>''
"nmap ,p  :! %<CR>

" delete the current line and paste it to the end, 
" easy for vocabulary building
"map ,m  ddGp''

" These days, I prefer nowrap by default:
" set nowrap
set wrap
"easy to change to 'nowrap':
nmap ,nw :set nowrap<CR>

"for easy page-down and up
nmap <Space>   <C-f>
"nmap  ,k   <C-b>

"for comment and uncomment source code
map ,# :s/^/#/<CR><Esc>:nohlsearch<CR><Esc>
map ,/ :s/^/\/\//<CR><Esc>:nohlsearch<CR><Esc>
"map ,c :s/^\/\/\\|^--\\|^> \\|^[#"%!;]//<CR><Esc>:nohlsearch<CR><Esc>

"for taglist toggle
nnoremap <silent> <Leader>t  :TlistToggle<CR><Esc>

":colorscheme  delek
":colorscheme  morning
:colorscheme  elflord
":colorscheme  evening
":colorscheme  peaksea
":colorscheme  astronaut
":colorscheme  brookstream
":colorscheme  darkblue



:filetype plugin indent on

"to turn-off high-light searching words
map ,h :noh <CR>

" Jump to next window tab
nmap  ,,   gt
" for easy command history:
nmap  ,q   q:

" Don't do folding less than 3 lines: 
set foldminlines=3

":cnoremap <C-A> <Home>   " conflict with screen
:cnoremap <C-F> <Right>
:cnoremap <C-B> <Left>


" ``showbreak`` make wrapped long line clear, it's better to use
" together with ``set nu``  ``set cpo+=n``
"
" as an example:  showbreak=>>>>> will use ">>>>>" for the wrapped lines,
" \ \ \ \  will add 4 space. 
" as indicator for long line break on screen
" This is good for bad, vim don't know 'hanging indent'
set showbreak=\ \ 
" This will not break in word when wrapping:
set linebreak

" If you want line number shown: set nu
" See more:  'nu' 'number' 'nonumber' 'nonu' 'nuw'
" If you want a large width of line number, < 10 : set nuw=10
set nu  cpo+=n


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" SETTINGS FOR Python (20081221) :
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Replace tabs with the equivalent number of spaces, 
" text-width = 78 chars, do folding according indent levels:
au BufNewFile,BufRead *.py,*.pyw  setlocal expandtab
au BufNewFile,BufRead *.py,*.pyw  setlocal tw=78
au BufNewFile,BufRead *.py,*.pyw  setlocal foldmethod=indent

" Use the below highlight group when displaying bad whitespace is desired
highlight BadWhitespace ctermbg=red guibg=red

" Display tabs at the beginning of a line in Python mode as bad.
au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /^\t\+/
" Make trailing whitespace be flagged as bad.
"au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" For full syntax highlighting:
let python_highlight_all=1
"``syntax on``

" Automatically indent based on file type: ``filetype indent on``
" Keep indentation level from previous line: ``set autoindent``

" ? python.vim in ~/.vim/  is useless? :: 
" there is a syntax file with the name: python.vim
"
" for Python, from python.org (20081215)
" If you want do everything according python.org:
"source  /home/za/.vim/vimrc_python_c


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" SETTINGS FOR HTML (20090122) :
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" HTML gets too much indent levels, make indent small:
au BufNewFile, BufRead *.html,*.htm  setlocal tabstop=2  shiftwidth=2

" for psql editor 200903
au BufRead /tmp/psql.edit.*  setlocal ft=sql

" for gsp of grails:
au BufRead *.gsp  setlocal ft=html


let MRU_File = '/home/za/.vim/.vim_mru_files'
let MRU_Max_Entries = 800
nmap ,f  :MRU<ENTER>

" to add <UL> <LI> </LI> <LI> </LI> </UL> with ,ul
"nmap ,u  o<DIV CLASS="flashcard"><ENTER><DIV CLASS="front"><ENTER></DIV><ENTER><DIV CLASS="back"><ENTER></DIV><ENTER></DIV><ESC>
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" THIS IS THE MAGIC: ""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
" mruex.vim , this make a lot trouble
" syntax highlighting losting
" This troubled me for a year. syntax highlighting  
" The following is accumulated during more than a year's
" history:
"
"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

" for vim-latex:
"" REQUIRED. This makes vim invoke Latex-Suite when you open a tex file.
" filetype plugin on

" IMPORTANT: win32 users will need to have 'shellslash' set so that latex
" can be called correctly.
" set shellslash

" IMPORTANT: grep will sometimes skip displaying the file name if you
" search in a singe file. This will confuse Latex-Suite. Set your grep
" program to always generate a file-name.
"set grepprg=grep\ -nH\ $*
set grepprg=ack-grep

" OPTIONAL: This enables automatic indentation as you type.
" filetype indent on

" OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
" 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
" The following changes the default filetype back to 'tex':
let g:tex_flavor='latex'
" SmartkeyQuote will change " to ``, annoying 
let g:Tex_SmartKeyQuote=0
" END vim-latex setting
"


"for comment and uncomment source code
" , #perl # comments
map ,# :s/^/#/<CR><Esc>:nohlsearch<CR><Esc>
" ,/ C/C++/C#/Java // comments
map ,/ :s/^/\/\//<CR><Esc>:nohlsearch<CR><Esc>
"map ,c :s/^\/\/\\|^--\\|^> \\|^[#"%!;]//<CR><Esc>:nohlsearch<CR><Esc>

" ,< HTML comment
map ,< :s/^\(.*\)$/<!--\1-->/<CR><Esc>:nohlsearch<CR>
map  ,>  :s/^\s*<!--\(.*\)-->\s*$/\1/<CR><Esc>:nohlsearch<CR>

" c++ java style comments
map ,* :s/^\(.*\)$/\/\* \1 \*\//<CR><Esc>:nohlsearch<CR>

" for easy past from clipboard:
nmap P "+p

imap kk <Esc>

" open a new line
nmap ,p  :set paste<ENTER>o
nmap ,o  :set nopaste<ENTER>
