# First time setup:	# This fork - pyLoRa
### Easy setup essential python packet on Raspberry Pi Gateway:	This fork is an adaptation of the original mayeranalytic configured to work with Ai-Thinker Ra-02 Modules This module uses SX1278 IC and works on a 433MHz frequency. The examples in this library LORA_SERVER and LORA_CLIENT can be used to communicate with the Arduino through the RADIOHEAD library, for more information see these examples -> [rpsreal/LoRa_Ra-02_Arduino](https://github.com/rpsreal/LoRa_Ra-02_Arduino). 

 **Update 05/2018 - Added encrypted versions** 
For security reasons it is advisable to use the encrypted versions that use [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) (AES). You can also use them to communicate with the Arduino.


 **Update 08/2018 - Added support for 2 modules at the same time** Now it is possible to use 2 radio modules at the same time in Raspberry Pi. To do this, simply use the BOARD2 settings like this:
```python
# Use BOARD 2 (you can use BOARD1 and BOARD2 at the same time just give another name)
from SX127x.LoRa import LoRa2 as LoRa
from SX127x.board_config import BOARD2 as BOARD
```


 It supports Python 3 or newer and PyPy. https://pypi.org/project/pyLoRa/

 ## Easy setup on Raspberry Pi:
```bash	```bash
sudo raspi-config	sudo raspi-config
-- Interfacing Options	-- Interfacing Options
--- enable SPI	--- enable SPI
--- enable I2C	
--- enable SSH	
sudo apt-get install python-dev python3-dev	sudo apt-get install python-dev python3-dev
sudo apt-get install xrdp	
sudo apt-get install python-mysqldb	
sudo pip3 install mysql	
sudo pip3 install adafruit-circuitpython-ads1x15 	
sudo pip3 install Adafruit_DHT	
```	```


 ### Installation:	### Installation:
For **Install with pip3** perform the following installation steps:	For **Install with pip** perform the following installation steps:
```bash	```bash
sudo apt-get install python-pip python3-pip	sudo apt-get install python-pip python3-pip
pip3 install RPi.GPIO	pip install RPi.GPIO
pip3 install spidev	pip install spidev
pip3 install pyLoRa	pip install pyLoRa
```	```


 For **encrypted versions only** it is necessary to perform the following installation step:	For **encrypted versions only** it is necessary to perform the following installation step:
```bash	```bash
pip3 install pycryptodome	pip install pycryptodome
pip3 install pycrypto	pip install pycrypto
```


 ### Hardware
Make the connections as shown below.
If it is necessary to change edit the file board_config.py

 | Ra-02 LoRa BOARD1 |  RaspPi GPIO  | Ra-02 LoRa BOARD2 |  RaspPi GPIO  |
|:------------------|:--------------|:------------------|:-------------:|
|        MOSI       | GPIO 10       |        MOSI       | GPIO 10       |
|        MISO       | GPIO 9        |        MISO       | GPIO 9        |
|     SCK (SCLK)    | GPIO 11       |     SCK (SCLK)    | GPIO 11       |
|        NSS        | GPIO 8 (CE0)  |        NSS        | GPIO 7 (CE1)  |
|     DIO0 (IRQ)    | GPIO 4        |     DIO0 (IRQ)    | GPIO 23       |
|        DIO1       | GPIO 17       |        DIO1       | GPIO 24       |
|        DIO2       | GPIO 18       |        DIO2       | GPIO 25       |
|        DIO3       | GPIO 27       |        DIO3       | GPIO 5        |
|     RST (Reset)   | GPIO 22       |     RST (Reset)   | GPIO 6        |
|        LED        | GPIO 13       |        LED        | GPIO 19       |

 LED external with 1k ohm or 330ohm (optional)

 ### How to Use
View the sample files. 
If you downloaded the library and sample files, now you can start LORA_SERVER or LORA_CLIENT (encrypted or non-encripted).
To work, there must be another LORA_SERVER or LORA_CLIENT running on another device (Raspberry Pi or Arduino)

 For example, if you are running on an [Arduino the LORA_CLIENT](https://github.com/rpsreal/LoRa_Ra-02_Arduino/blob/master/LORA_CLIENT.ino) then start the [LORA_SERVER.py on Raspberry Pi](https://github.com/rpsreal/pySX127x/blob/master/LORA_SERVER.py) like this:
```bash
cd pySX127x
python3 ./LORA_SERVER.py
```

 ### Extra 
If you do not need to install the library you can use it simply in the same directory.
To **Download library and example files**:
```bash
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo apt-get install python-spidev python3-spidev
sudo apt-get install git
sudo git clone https://github.com/rpsreal/pySX127x
```

 If it is necessary to run the library from anywhere:
```bash
nano ~/.bashrc
```
Put this at the end of the file: 
> export PYTHONPATH=/home/pi/pySX127x/
 And then:
```bash
source ~/.bashrc
```

 Developed by Rui Silva, Porto, Portugal



 # Forked from mayeranalytics/pySX127x
# Overview

 This is a python interface to the [Semtech SX1276/7/8/9](http://www.semtech.com/wireless-rf/rf-transceivers/) 
long range, low power transceiver family.

 The SX127x have both LoRa and FSK capabilities. Here the focus lies on the
LoRa spread spectrum modulation hence only the LoRa modem interface is implemented so far 
(but see the [roadmap](#roadmap) below for future plans).

 Spread spectrum modulation has a number of intriguing features:
* High interference immunity
* Up to 20dBm link budget advantage (for the SX1276/7/8/9)
* High Doppler shift immunity

 More information about LoRa can be found on the [LoRa Alliance website](https://lora-alliance.org).
Links to some LoRa performance reports can be found in the [references](#references) section below.


 # Motivation

 Transceiver modules are usually interfaced with microcontroller boards such as the 
Arduino and there are already many fine C/C++ libraries for the SX127x family available on 
[github](https://github.com/search?q=sx127x) and [mbed.org](https://developer.mbed.org/search/?q=sx127x).

 Although C/C++ is the de facto standard for development on microcontrollers, [python](https://www.python.org)
running on a Raspberry Pi is becoming a viable alternative for rapid prototyping.

 High level programming languages like python require a full-blown OS such as Linux. (There are some exceptions like
[PyMite](https://wiki.python.org/moin/PyMite) and most notably [MicroPython](https://micropython.org).)
But using hardware capable of running Linux contradicts, to some extent, the low power specification of the SX127x family.
Therefore it is clear that this approach aims mostly at prototyping and technology testing.

 Prototyping on a full-blown OS using high level programming languages has several clear advantages:
* Working prototypes can be built quickly 
* Technology testing ist faster
* Proof of concept is easier to achieve
* The application development phase is reached quicker 


 # Hardware

 The transceiver module is a SX1276 based Modtronix [inAir9B](http://modtronix.com/inair9.html). 
It is mounted on a prototyping board to a Raspberry Pi rev 2 model B.

 | Proto board pin | RaspPi GPIO | Direction |
|:----------------|:-----------:|:---------:|
| inAir9B DIO0    | GPIO 22     |    IN     |
| inAir9B DIO1    | GPIO 23     |    IN     |
| inAir9B DIO2    | GPIO 24     |    IN     |
| inAir9B DIO3    | GPIO 25     |    IN     |
| inAir9b Reset   | GPIO ?      |    OUT    |
| LED             | GPIO 18     |    OUT    |
| Switch          | GPIO 4      |    IN     |

 Todo:
- [ ] Add picture(s)
- [ ] Wire the SX127x reset to a GPIO?


 # Code Examples

 ### Overview
First import the modules 
```python
from SX127x.LoRa import *
from SX127x.board_config import BOARD
```
then set up the board GPIOs
```python
BOARD.setup()
```
The LoRa object is instantiated and put into the standby mode
```python
lora = LoRa()
lora.set_mode(MODE.STDBY)
```
Registers are queried like so:
```python
print lora.version()        # this prints the sx127x chip version
print lora.get_freq()       # this prints the frequency setting 
```
and setting registers is easy, too
```python
lora.set_freq(433.0)       # Set the frequency to 433 MHz 
```
In applications the `LoRa` class should be subclassed while overriding one or more of the callback functions that
are invoked on successful RX or TX operations, for example.
```python
class MyLoRa(LoRa):
   def __init__(self, verbose=False):
    super(MyLoRa, self).__init__(verbose)
    # setup registers etc.
   def on_rx_done(self):
    payload = self.read_payload(nocheck=True) 
    # etc.
```

 In the end the resources should be freed properly
```python
BOARD.teardown()
```

 ### More details
Most functions of `SX127x.Lora` are setter and getter functions. For example, the setter and getter for 
the coding rate are demonstrated here
```python 
print lora.get_coding_rate()                # print the current coding rate
lora.set_coding_rate(CODING_RATE.CR4_6)     # set it to CR4_6
```

 @todo


 # Installation

 Make sure SPI is activated on you RaspberryPi: [SPI](https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md)
**pySX127x** requires these two python packages:
* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO") for accessing the GPIOs, it should be already installed on
  a standard Raspian Linux image
* [spidev](https://pypi.python.org/pypi/spidev) for controlling SPI

 In order to install spidev download the source code and run setup.py manually:
```bash
wget https://pypi.python.org/packages/source/s/spidev/spidev-3.1.tar.gz
tar xfvz  spidev-3.1.tar.gz
cd spidev-3.1
sudo python setup.py install
```	```


 At this point you may want to confirm that the unit tests pass. See the section [Tests](#tests) below.

 You can now run the scripts. For example dump the registers with `lora_util.py`: 
```bash
rasp$ sudo ./lora_util.py
SX127x LoRa registers:
 mode               SLEEP
 freq               434.000000 MHz
 coding_rate        CR4_5
 bw                 BW125
 spreading_factor   128 chips/symb
 implicit_hdr_mode  OFF
 ... and so on ....
```


 # Class Reference	# Class Reference


 The interface to the SX127x LoRa modem is implemented in the class `SX127x.LoRa.LoRa`.	The interface to the SX127x LoRa modem is implemented in the class `SX127x.LoRa.LoRa`.
@@ -43,40 +257,156 @@ The most important modem configuration parameters are:
| | |	| | |
| @todo            |                              |	| @todo            |                              |


 ## Config parameter file:	Most set_* functions have a mirror get_* function, but beware that the getter return types do not necessarily match 
Open file config.ini in the folder and config lora transmission parameter for gateway 	the setter input types.
</br>	
 **Parameter configuration for node 1 and node 2 must be match up with parameter configuration in the file config.ini in node**	### Register naming convention
```bash	The register addresses are defined in class `SX127x.constants.REG` and we use a specific naming convention which 
#Google could parameters config	is best illustrated by a few examples:
[Google cloud MySQL]	
 host: 35.220.202.217	| Register | Modem | Semtech doc.      | pySX127x                   |
user: root	|----------|-------|-------------------| ---------------------------|
passwd: 1234	| 0x0E     | LoRa  | RegFifoTxBaseAddr | REG.LORA.FIFO_TX_BASE_ADDR |
database: project_loraweb	| 0x0E     | FSK   | RegRssiCOnfig     | REG.FSK.RSSI_CONFIG        |
######################	| 0x1D     | LoRa  | RegModemConfig1   | REG.LORA.MODEM_CONFIG_1    |
#Parameters config for node:	| etc.     |       |                   |                            |
# frequency: 430 - 510 MHz	
 # band_width: [ BW.BW7_8 , BW.BW10_4, BW.BW15_6, BW.BW20_8, BW.BW31_15, BW.BW41_7, BW.BW62_5, BW.BW125, BW.BW250, BW.BW500]	### Hardware
# coding_rate: [CODING_RATE.CR4_5, CODING_RATE.CR4_6, CODING_RATE.CR4_7, CODING_RATE.CR4_8]	Hardware related definition and initialisation are located in `SX127x.board_config.BOARD`.
# spreading_factor: 7 - 12	If you use a SBC other than the Raspberry Pi you'll have to adapt the BOARD class.
######################	
 #Gateway node 1 config	
 [Node1]	# Script references
frequency: 434.0	
 band_width: BW.BW250	### Continuous receiver `rx_cont.py`
coding_rate: CODING_RATE.CR4_8	The SX127x is put in RXCONT mode and continuously waits for transmissions. Upon a successful read the
spreading_factor: 12	payload and the irq flags are printed to screen.
#Gateway node 2 config	```
[Node2]	usage: rx_cont.py [-h] [--ocp OCP] [--sf SF] [--freq FREQ] [--bw BW]
frequency: 440.0	                  [--cr CODING_RATE] [--preamble PREAMBLE]
band_width: BW.BW250	
coding_rate: CODING_RATE.CR4_8	Continous LoRa receiver
spreading_factor: 12	
```	optional arguments:
## Start gateway	  -h, --help            show this help message and exit
```bash	  --ocp OCP, -c OCP     Over current protection in mA (45 .. 240 mA)
sudo python3 LORA_Gateway-01_encrypted.py (for node 1)	  --sf SF, -s SF        Spreading factor (6...12). Default is 7.
sudo python3 LORA_Gateway-02_encrypted.py (for node 2)
