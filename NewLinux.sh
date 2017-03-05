#!/bin/bash


mkdir ~/forgit
cd ~/forgit
git clone --depth=1 https://github.com/IanSmith123/vimrc-of-ian.git
git clone --depth=1 https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim


git clone --depth=1 https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
echo "socks5 127.0.0.1 1080 " >>/etc/proxychains.conf
cd ..

git clone --depth=1 https://github.com/sqlmapproject/sqlmap.git
git clone --depth=1 https://github.com/lijiejie/subDomainsBrute.git
git clone --depth=1 https://github.com/powerline/fonts.git

cd 



sudo apt install python-pip zsh -y
sudo apt install figlet sl tree python3-pip -y
sudo apt install libssl-dev zsh autojump exuberant-ctags sublime-text -y

wget https://nmap.org/dist/nmap-7.40.tar.bz2
tar -xvf nmap-7.40.tar.bz2
cd nmap-7.40
./configure
make
sudo make install
cd ..


mkdir ~/.pip
echo "[global]">~/.pip/pip.conf
echo "index-url = https://pypi.douban.com/simple/">> ~/.pip/pip.conf
sudo pip install --upgrade pip setuptools
sudo pip install requests shadowsocks ipython xlrd flask uwsgi virtulenv



echo "http://www.rapid7.com/products/metasploit/metasploit-community-thank-you.jsp is the download msf link"
echo "https://www.rapid7.com/products/metasploit/download/community/thank-you/"
echo "Your License Key:   8TD3-KQ09-HLP0-EVJR"
wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run


sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"                                                  
