## Easy setup on Raspberry Pi:
```bash
sudo raspi-config
-- Interfacing Options
--- enable SPI
sudo apt-get install python-dev python3-dev
```

### Installation:
For **Install with pip** perform the following installation steps:
```bash
sudo apt-get install python-pip python3-pip
pip install RPi.GPIO
pip install spidev
pip install pyLoRa
```

For **encrypted versions only** it is necessary to perform the following installation step:
```bash
pip install pycryptodome
pip install pycrypto
```

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

### Register naming convention
The register addresses are defined in class `SX127x.constants.REG` and we use a specific naming convention which 
is best illustrated by a few examples:

| Register | Modem | Semtech doc.      | pySX127x                   |
|----------|-------|-------------------| ---------------------------|
| 0x0E     | LoRa  | RegFifoTxBaseAddr | REG.LORA.FIFO_TX_BASE_ADDR |
| 0x0E     | FSK   | RegRssiCOnfig     | REG.FSK.RSSI_CONFIG        |
| 0x1D     | LoRa  | RegModemConfig1   | REG.LORA.MODEM_CONFIG_1    |
| etc.     |       |                   |                            |

