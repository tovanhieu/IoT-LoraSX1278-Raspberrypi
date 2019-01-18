# Hướng dẫn
## Kết nối phần cứng:
![capture2](https://user-images.githubusercontent.com/26000753/48856223-6f483980-ede8-11e8-8653-3bf599061107.PNG)
\
![lora-rpi-gwpin-out](https://user-images.githubusercontent.com/26000753/51383622-87200d80-1b4c-11e9-8330-122aed92a09c.PNG)
\
## Cấu hình SPI cho Raspberry Pi:
```bash
sudo raspi-config
-- Interfacing Options
--- enable SPI
sudo apt-get install python-dev python3-dev
```
### Cài đặt thư viện python:
 **Install with pip**:
```bash
sudo apt-get install python-pip python3-pip
pip install RPi.GPIO
pip install spidev
pip install pyLoRa
```

 **encrypted versions only** :
```bash
pip install pycryptodome
pip install pycrypto
```
### Refrence
- https://github.com/rpsreal/pySX127x
- https://pypi.org/project/pyLoRa/
