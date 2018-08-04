#!/bin/bash

# init color


set_color() {
	if which tput >/dev/null 2>&1; then
		ncolors=$(tput colors)
	fi
	if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
		RED="$(tput setaf 1)"
		GREEN="$(tput setaf 2)"
		YELLOW="$(tput setaf 3)"
		BLUE="$(tput setaf 4)"
		BOLD="$(tput bold)"
		NORMAL="$(tput sgr0)"

	else
		RED=""
		GREEN=""
		YELLOW=""
		BLUE=""
		BOLD=""
		NORMAL=""
	fi
}
# 添加颜色
# set_color
printf "${GREEN} $#\n"
if [ $# -eq 0 ]
then
	printf "${BLUE}update,curl,wget,vim,zsh,tmux,docker"
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
		"git")
			sudo apt install git -y
			;;
		"ssh")
			sudo apt install openssh-server -y
			;;

		"vim")
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
			echo '{\n"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]\n}'>/etc/docker/daemon.json 
			printf "${BLUE} set docker mirror.."
			;;

		"proxychains4")
			cd /tmp
			git clone --depth=1 https://github.com/rofl0r/proxychains-ng.git
			cd proxychains-ng
			./configure --prefix=/usr --sysconfdir=/etc
			make
			sudo make install
			sudo make install-config
			echo "socks5 127.0.0.1 1080 " >>/etc/proxychains.conf
			cd 
			;;

		"pip")
			sudo apt install python3-pip
			mkdir -p ~/.config/pip/ && echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple"> ~/.config/pip/pip.conf
			printf "${BLUE} set pip mirror"
			;;
		"base_pip")
			sudo pip3 install requests docker-compose ipython jupyter
            ;;

		esac

	done
	echo "All done"
