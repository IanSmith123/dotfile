## about 
Les1ie's dotfiles :)


## dot files 
- [x] `vimrc` vim config, path`~/.vimrc`
- [x] `zshrc` oh-my-zsh config, path`~/.zshrc`
- [x] `tmux.conf` tmux config, path`~/.tmux.conf` 
- [ ] `env-ng.sh` for new installed linux server


## config for `vim`
1. install vim
2. install [vim-plug](https://github.com/junegunn/vim-plug)
Linux:

```bash
$ curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```
windows:

```powershell
md ~\vimfiles\autoload
$uri = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
(New-Object Net.WebClient).DownloadFile(
  $uri,
  $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath(
    "~\vimfiles\autoload\plug.vim"
  )
)
```



3. configure 

```bash
$ cp vimrc ~/.vimrc
$ vim -c 'PlugInstall' -c 'qa!'
```
4. functions

- enjoy **vim-plug** not **Vundle** , because vim-plug use shallow clone, and parallel download which much faster than Vundle
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

