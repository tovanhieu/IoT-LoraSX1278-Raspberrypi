## Easy setup on Raspberry Pi Node:
```bash
sudo raspi-config
-- Interfacing Options
--- enable SPI
--- enable I2C
--- enable SSH
sudo apt-get install python-dev python3-dev
sudo apt-get install xrdp
sudo apt-get install python-mysqldb
sudo pip3 install mysql
sudo pip3 install adafruit-circuitpython-ads1x15 
sudo pip3 install Adafruit_DHT
```

### Installation:
For **Install with pip3** perform the following installation steps:
```bash
sudo apt-get install python-pip python3-pip
pip3 install RPi.GPIO
pip3 install spidev
pip3 install pyLoRa
```

For **encrypted versions only** it is necessary to perform the following installation step:
```bash
pip3 install pycryptodome
pip3 install pycrypto
```

# Class Reference

The interface to the SX127x LoRa modem is implemented in the class `SX127x.LoRa.LoRa`.
The most important modem configuration parameters are:
 
| Function         | Description                                 |
|------------------|---------------------------------------------|
| set_mode         | Change OpMode, use the constants.MODE class |
| set_freq         | Set the frequency                           |
| set_bw           | Set the bandwidth 7.8kHz ... 500kHz         |
| set_coding_rate  | Set the coding rate 4/5, 4/6, 4/7, 4/8      |
| | |
| @todo            |                              |


