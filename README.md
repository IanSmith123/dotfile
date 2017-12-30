## about 
Les1ie's dotfiles :)


## dot files 
- [x] `vimrc` vim config, path`~/.vimrc`
- [x] `zshrc` oh-my-zsh config, path`~/.zshrc`
- [x] `tmux.conf` tmux config, path`~/.tmux.conf` 
- [ ] `env-ng.sh` for new installed linux server
- [ ] `NewLinux.sh` for new installed linux server(Deprecated)


## config for `vim`
1. install vim
2. install vundle
```bash
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```
3. configure 
```bash
$ cp vimrc ~/.vimrc
$ vim -c 'PluginInstall' -c 'qa!'
$ test -d ~/.vim/color || mkdir ~/.vim/color && cp ~/.vim/bundle/vim-colors-solarized/colors/solarized.vim ~/.vim/color/
```
4. functions

- `autoheader` auto add comment header about author when user create new file like `.py .cpp .c and etc`
- `Taglist`
- `NerdTree` 
- **solarized** color scheme (I think this is color scheme for human)
- `vim airline`
- auto close bracket and rainbow color bracket
- `markdown` highlight support
- alias `aa` as `esc`, `jk` as `<RIGHT>`
- auto check file encoding 

## config for  `oh-my-zsh`
1. install zsh, figlet(show banner)
2. install [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) script
```bash
$ sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```
3. configure

```bash
$ sed -i "s@HOMEDIR@$HOME@g" zshrc
$ cp zshrc ~/.zshrc && . ~/.zshrc
```
4. functions

- show the online users and last login users
- `docker` auto complete container name
- double click `esc` to add  `sudo`
- `z` do what`autojump`  do, without additional configure
- `alias` for `tmux`, `git`, `docker-compose`

## config for `tmux`
1. install tmux
2. configure
```bash
$ cp tmux.conf ~/.tmux.conf
```
3. functions
- `vim like`for the change of `pane`
- use `h j k l` to change focus
- use `H J K L` to resize `pane`
- use  `<` and `>` to swap position of `pane`
- both `C-b` and `C-x` work as prefix
- prefix + `r` reload config
- use `|` and `-` for vertical or horizontal split for screen

