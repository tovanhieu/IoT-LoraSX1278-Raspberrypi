# IoT LoRa transmission project 📡
## Author: Hieu (Toni)
## Contributor: Trung, Khanh.
_**This IoT project uses LoRa transmission technology for studying and researching purpose. You can modify and contribute to my code as long as you include the original copyright notice and disclaimer.**_
#### Nedded python packages for the project:
Install it using pip or pip3, but I recommend using pip3
</br>
</br>
![License](https://img.shields.io/badge/license-MIT_License-purple)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Pip or Pip3](https://img.shields.io/badge/pip-23.2.1-green)
![Python dev tools](https://img.shields.io/badge/python_dev_tools-2023.3.24-yellow)
![MySQL python](https://img.shields.io/badge/MySQL_python-1.2.5-orange)
![Mysql connector python](https://img.shields.io/badge/mysql_connector_python-8.1.0-purple)
![RPi.GPIO](https://img.shields.io/badge/RPi.GPIO-0.7.1-pink)
![Brown](https://img.shields.io/badge/spidev-3.6-brown)
![PyLoRa](https://img.shields.io/badge/pyLoRa-0.3.1-white)
![Pycryptodom](https://img.shields.io/badge/pycryptodome-3.18.0-cyan)
![Pycrypto](https://img.shields.io/badge/pycrypto-2.6.1-teal)
![Message](https://img.shields.io/badge/Clone_the_project_and_follow_my_guides_step_by_step_%F0%9F%A7%90-8A2BE2)
### Use cases for the project
There are two use cases I use for this project: **_Forest fire warning system_** and **_Smart railway transmission_**.
This is the proposal architecture:
![SmartRaillWay-Ar](https://github.com/tovanhieu/LoraSX1278-Raspberrypi/assets/26000753/db29cfce-e03b-4f91-b2c6-8f8bd13932bb)

### The project contains two properties:
1. **Node**: I use Raspberry Pi Zero integrated with module Lora-Ra 02 SX1278 and sensors: [LDR](https://www.electronicaembajadores.com/en/Productos/Detalle/SSLDR67/sensors/color-light-sensors/ldr-resistance-5-9-x-7-mm-light-sensor/), [DHT22](https://www.cytrontech.vn/p-dht22-temperature-and-humidity-sensor?currency=VND&gad=1&gclid=CjwKCAjwgZCoBhBnEiwAz35RwhM8Gy4RZTgACKgCrHPCX7Fv3yhTXUskpHNxDMKpxeUEgw8sGi9hShoCt6oQAvD_BwE), [MQ135](https://hshop.vn/products/cam-bien-chat-luong-khong-khi-mq-139), [Buzzer 5v 2505A](https://shopee.vn/C%C3%B2i-Xung-5V-12x25MM-USP-2505A-i.151571719.9926169242). The node will collect data from sensors include: temperature, humidity, percentage CO of smophere,.... and sends to the Gateway. Source code of two nodes in this implementation of the project here [Node 1](https://github.com/tovanhieu/LoraProject/blob/master/Raspberrypi%20Zero-Node/LORA_NODE_01_encrypted.py) and [Node 2](https://github.com/tovanhieu/LoraProject/blob/master/Raspberrypi%20Zero-Node/LORA_NODE_02_encrypted.py)
 ![Screenshot 2023-09-15 153852](https://github.com/tovanhieu/LoraSX1278-Raspberrypi/assets/26000753/d05df0bf-b602-43f0-b2c6-11e40e0fce68)

2. **Gateway**: I use Raspberry Pi 3 B+ integrated with module Lora-Ra 02 SX1278, after receiving data from nodes, gateway will send data to the Web Server in Cloud, I use Firebase and Googlecloud to store and share datas with the monitor Web Application and the Mobie Application via API.
##### https://github.com/tovanhieu/LoraProject/blob/master/RaspberryPi-Gateway/LORA_Gateway-01_encrypted.py
##### https://github.com/tovanhieu/LoraProject/blob/master/RaspberryPi-Gateway/LORA_Gateway-02_encypted.py
3. **Web server**: 

### Last Update 
08/2023
## Referencece Links
#### https://github.com/rpsreal/pySX127x
#### https://pypi.org/project/pyLoRa/
#### https://github.com/rpsreal/LoRa_Ra-02_Arduino
#### https://console.firebase.google.com
#### https://www.e-gizmo.net/oc/kits%20documents/LORA%20Module%20RA-02%20V.1/LORA%20Module%20RA-02%20V.1.pdf
#### https://cloud.google.com/
