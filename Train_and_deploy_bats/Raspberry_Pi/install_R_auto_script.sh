#!/bin/bash

# Firstly:
# manually download bzip2-1.0.6 from soundforge website:
# https://sourceforge.net/projects/bzip2/files/latest/download
# It should now be in the downloads folder.

# To run this script, type following 2 lines into command line:
# cd /home/pi/Desktop/Bioacoustics
# bash install_R_auto_script.sh

RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "${GREEN}Here we go ..... Fingers crossed! ${NC}\n"

sudo apt-get update
sudo apt-get upgrade -y

printf "${GREEN}Update and upgrade done! ${NC}\n"

# If necessary, check the version of bzip is as below:
cd && cd /home/pi/Downloads/
tar zxvf bzip2-1.0.6.tar.gz 
cd bzip2-1.0.6
sudo make install

printf "${GREEN}bzip2 installed! ${NC}\n"

sudo apt-get install liblzma-dev
sudo apt-get install cmake -y
sudo apt-get install sox libsox-fmt-all
sudo apt-get install audacity
sudo apt-get install bc
sudo apt-get install build-essential libgtk-3-dev
sudo pip3 install jupyter
sudo apt install python3-cairo 
sudo apt install libcairo2
pip3 install playsound
sudo apt-get install -y gir1.2-appindicator3-0.1
#sudo apt-get install libasound-dev
#sudo apt-get install portaudio19-dev
#pip3 install pyaudio
#sudo apt-get install python3-pyaudio
#sudo apt-get install parallel
#pip3 install pyAudioAnalysis
pip3 install pydub
pip3 install pathlib2

sudo apt-get install python-dev libatlas-base-dev
pip3 install numpy
pip3 install matplotlib
pip3 install DateTimeRange
pip3 install pandas

# pip3 install py2exe
# pip3 install timerange
#sudo pip3 install --upgrade matplotlib

curl -O https://www.omzlo.com/downloads/pivoyager.tar.gz
tar xvf pivoyager.tar.gz
sudo mv pivoyager /usr/local/bin/

sudo apt install -y python3-scipy
#pip3 install scipy

# pip3 install sklearn
# pip3 install hmmlearn
# pip3 install simplejson
# pip3 install eyed3
# The script eyeD3 is installed in '/home/pi/.local/bin' which is not on PATH.
# pip3 install psrecord
bash <(curl -Ss https://my-netdata.io/kickstart.sh)

sudo apt-get install -y gfortran libreadline6-dev libx11-dev libxt-dev libpng-dev libjpeg-dev libcairo2-dev xvfb libcurl4-openssl-dev texinfo

printf "${GREEN}Start to install R! ${NC}\n"

cd /home/pi/
mkdir R_HOME
cd R_HOME
wget http://cran.rstudio.com/src/base/R-3/R-3.6.1.tar.gz
tar zxvf R-3.6.1.tar.gz 
cd && cd R_HOME/R-3.6.1/
./configure --enable-R-shlib #--with-blas --with-lapack #optional
make
sudo make install

R --version

printf "${GREEN}R 3.6.1 installed! ${NC}\n"

sudo chmod -R 777 /usr/local/lib/R/library
sudo chmod -R 777 /usr/local/lib/R/
sudo chmod -R 777 /home/pi/Desktop/deploy_classifier/run.desktop
sudo chmod -R 775 /home/pi/Desktop/deploy_classifier/

printf "${GREEN} Now the R packages need to be manually installed eg run R and use: install.packages("audio") ${NC}\n"
printf "${GREEN} Don't forget to enable I2C in settings !${NC}\n"





