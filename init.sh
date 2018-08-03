#!/bin/bash
if [$#==1];then
echo "update,curl,wget,vim,zsh,tmux,docker"
exit
fi

for cmd in $@
do
case $cmd in 
"update")
sudo apt update -y
;;

"curl")
sudo apt install curl -y
;;

"wget")
sudo apt install wget -y
;;

"vim")
echo "Vim"
#sudo apt install vim
curl -fsSL https://raw.githubusercontent.com/IanSmith123/dotfile/master/vimrc -o ~/.vimrc
vim -c 'PlugInstall' -c 'qa!'
;;

"zsh")
echo "oh-my-zsh"
sudo apt install zsh figlet -y
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
 
curl -fsSL https://raw.githubusercontent.com/IanSmith123/dotfile/master/vimrc -o /tmp/zshrc
sed -i "s@HOMEDIR@$HOME@g" /tmp/zshrc
mv /tmp/zshrc ~/.zshrc
;;

"tmux")
echo "tmux"
sudo apt install tmux -y
curl -fsSL https://raw.githubusercontent.com/IanSmith123/dotfile/master/tmux.conf -o ~/.tmux.conf
echo "tmux done"
;;

"docker")
curl -fsSL https://get.docker.com -o /tmp/docker.sh
sudo bash /tmp/docker.sh
sudo usermod -aG docker $USER
;;
esac

done
echo "All done"