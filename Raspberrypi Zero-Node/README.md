# First time setup:
### Easy setup essential python packet on Raspberry Pi Node:
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

## Config parameter file:
Open file config.ini in the folder and config lora transmission parameter for node **Parameter configuration for node 1 and node 2 must be match up with parameter configuration in the file config.ini in gateway**
```bash
config.ini
######################
#Parameters config for node:
# frequency: 430 - 510 MHz
# band_width: [ BW.BW7_8 , BW.BW10_4, BW.BW15_6, BW.BW20_8, BW.BW31_15, BW.BW41_7, BW.BW62_5, BW.BW125, BW.BW250, BW.BW500]
# coding_rate: [CODING_RATE.CR4_5, CODING_RATE.CR4_6, CODING_RATE.CR4_7, CODING_RATE.CR4_8]
# spreading_factor: 7 - 12
######################
#Gateway node 1 config
[Node1]
frequency: 434.0
band_width: BW.BW250
coding_rate: CODING_RATE.CR4_8
spreading_factor: 12
#Gateway node 2 config
[Node2]
frequency: 440.0
band_width: BW.BW250
coding_rate: CODING_RATE.CR4_8
spreading_factor: 12
```
## Start monitor and transmitssion from node:
```bash
sudo python3 LORA_NODE_01_encrypted.py (for node 1)
sudo python3 LORA_NODE_02_encrypted.py (for node 2)
```

