# First time setup:	
#### Gateway schematic: pin-out on Raspberry Pi B+
<br>

![Gateway_1](https://github.com/tovanhieu/IoT-LoraSX1278-Raspberrypi/assets/26000753/f9804baa-093d-4147-820a-ed0ba44301c8)
<br>

#### Gateway schematic: pin-out on Lora SX1278
<br>

![Gateway_2](https://github.com/tovanhieu/IoT-LoraSX1278-Raspberrypi/assets/26000753/5f7618e9-2d96-4c02-bc38-dcc68afde1c5)
<br>
### Easy setup essential python packet on Raspberry Pi Gateway:	
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
```	


 ### Installation:	
For **Install with pip3** perform the following installation steps:	ollowing installation steps:
```bash
sudo apt-get install 
pip3 install RPi.GPIO	
pip3 install spidev	
pip3 install pyLoRa
```
For **encrypted versions only** it is necessary to perform the following installation step:	
```bash	
pip3 install pycryptodome	
pip3 install pycrypto	
```
 ## Config parameter file:	
Open file config.ini in the folder and config lora transmission parameter for gateway 	
</br>	
 **Parameter configuration for node 1 and node 2 must be match up with parameter configuration in the file config.ini in node**	
```bash	
#Google could parameters config
[Google cloud MySQL]
host: 35.220.202.217
user: root
passwd: 1234
database: project_loraweb
######################
#Parameters config for node:
# frequency: 430 - 510 MHz
# band_width: 
    ; BW7_8   = 0
    ; BW10_4  = 1
    ; BW15_6  = 2
    ; BW20_8  = 3
    ; BW31_25 = 4
    ; BW41_7  = 5
    ; BW62_5  = 6
    ; BW125   = 7
    ; BW250   = 8
    ; BW500   = 9
# coding_rate: [CODING_RATE.CR4_5, CODING_RATE.CR4_6, CODING_RATE.CR4_7, CODING_RATE.CR4_8]
;     CR4_5 = 1
;     CR4_6 = 2
;     CR4_7 = 3
;     CR4_8 = 4
# spreading_factor: 7 - 12
######################
#Gateway node 1 config
[Node1]
frequency: 434.0
band_width: 8
coding_rate: 4
spreading_factor: 12
#Gateway node 2 config
[Node2]
frequency: 440.0
band_width: 8
coding_rate: 4
spreading_factor: 12
```
## Start gateway	
```bash	 
sudo python3 LORA_Gateway-01_encrypted.py (for node 1)	 
sudo python3 LORA_Gateway-02_encrypted.py (for node 2)
```
