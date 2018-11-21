# Hướng dẫn
## Kết nối phần cứng:
![capture2](https://user-images.githubusercontent.com/26000753/48856223-6f483980-ede8-11e8-8653-3bf599061107.PNG)
\
![gw](https://user-images.githubusercontent.com/26000753/48851590-04920080-edde-11e8-9475-ce73f5579403.PNG)
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
## Cấu hình SPI cho Raspberry Pi:
### Refrence
- https://github.com/rpsreal/pySX127x
