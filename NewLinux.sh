#!/bin/bash
git clone --depth=1 https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone --depth=1 https://github.com/rofl0r/proxychains-ng.git
git clone --depth=1 https://github.com/sqlmapproject/sqlmap.git
git clone --depth=1 https://github.com/lijiejie/subDomainsBrute.git
git clone --depth=1 https://github.com/IanSmith123/vimrc-of-ian.git
git clone --depth=1 https://github.com/powerline/fonts.git
wget https://nmap.org/dist/nmap-7.40.tar.bz2
echo "http://www.rapid7.com/products/metasploit/metasploit-community-thank-you.jsp is the download msf link"
echo "Your License Key:   8TD3-KQ09-HLP0-EVJR"
wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run
sudo apt install python-pip -y

sudo apt install figlet -y
sudo apt install nmap -y
sudo pip install requests -i https://pypi.douban.com/simpel
sudo pip install shadowsocks -i https://pypi.douban.com/simpel
sudo pip install ipython -i https://pypi.douban.com/simpel
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"                                                  
