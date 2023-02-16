sudo apt-get install gcc  
sudo apt-get install dpkg-dev  
sudo dpkg --add-architecture i386; sudo apt-get update
sudo apt-get install libc6:i386 libx11-6:i386 libdbus-1-dev:i386
sudo apt-get install sharutils  
sudo apt-get install ncompress  

sudo apt-get install p7zip-full p7zip-rar  
解壓縮檔案  
7z e SEP_LINUX.7z

sudo chmod +x install.sh  
sudo ./install.sh -i
