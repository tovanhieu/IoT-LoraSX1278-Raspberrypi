#!bin/bash
# Install mysql database
apt-get install python-mysqldb
pip3 install mysql
# Enable I2C, SPI communication on raspberry pi 
#sudo raspi-config
#-- Interfacing Options
#--- enable SPI
#--- enable I2C
# Install package for Lora
sudo apt-get install python-dev python3-dev
sudo apt-get install python-pip python3-pip
pip3 install RPi.GPIO
pip3 install spidev
pip3 install pyLoRa
pip3 install pycryptodome
pip3 install pycrypto
# Install package for ADS1115
sudo pip3 install adafruit-circuitpython-ads1x15 
# Install package for DHT
pip3 install Adafruit_DHT
