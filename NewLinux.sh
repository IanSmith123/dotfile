#!/bin/bash
# author: Les1ie
# email: iansmith@qq.com
# date: 2017-5-27 23:58:27



# base 
sudo apt install python-pip python3-pip zsh figlet exuberant-ctags autojump sl tree -y

mkdir ~/.pip
echo "[global]">~/.pip/pip.conf
echo "index-url = https://pypi.douban.com/simple/">> ~/.pip/pip.conf
sudo pip install -U pip setuptools
sudo pip install requests shadowsocks ipython xlrd flask virtulenv
sudo pip3 install -U pip setuptools
sudo pip3 install requests shadowsocks ipython xlrd flask virtulenv

# for desktop
sudo apt install shutter netease-cloud-music okular filezilla -y

# for base github file
mkdir ~/forgit
cd ~/forgit
git clone --depth=1 https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone --depth=1 https://github.com/IanSmith123/Les1ie-conf.git
cp Les1ie-conf/vimrc ~/.vimrc
# Todo: PluginInstall

git clone https://github.com/IanSmith123/iansmith123.github.io.git

git clone --depth=1 https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
echo "socks5 127.0.0.1 1080 " >>/etc/proxychains.conf
cd ..


# for cyber security
git clone --depth=1 https://github.com/sqlmapproject/sqlmap.git
git clone --depth=1 https://github.com/lijiejie/subDomainsBrute.git
cd 




sudo apt install libssl-dev -y
wget https://nmap.org/dist/nmap-7.40.tar.bz2
tar -xvf nmap-7.40.tar.bz2
cd nmap-7.40
./configure
make
sudo make install
cd ..




#echo "http://www.rapid7.com/products/metasploit/metasploit-community-thank-you.jsp is the download msf link"
#cho "https://www.rapid7.com/products/metasploit/download/community/thank-you/"
#cho "Your License Key:   8TD3-KQ09-HLP0-EVJR"
#get https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run


# for oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"                                                  
