# IoT LoRa transmission project 📡
## Author: Hieu (Toni)
## Contributor: Trung.
_**This IoT project uses LoRa transmission technology only for studying and researching purpose. You can modify and contribute to my code as long as you include the original copyright notice and disclaimer.**_
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

### The project contains three properties:
1. **Node**: I use Raspberry Pi Zero integrated with module Lora-Ra 02 SX1278 and sensors: [LDR](https://www.electronicaembajadores.com/en/Productos/Detalle/SSLDR67/sensors/color-light-sensors/ldr-resistance-5-9-x-7-mm-light-sensor/), [DHT22](https://www.cytrontech.vn/p-dht22-temperature-and-humidity-sensor?currency=VND&gad=1&gclid=CjwKCAjwgZCoBhBnEiwAz35RwhM8Gy4RZTgACKgCrHPCX7Fv3yhTXUskpHNxDMKpxeUEgw8sGi9hShoCt6oQAvD_BwE), [MQ135](https://hshop.vn/products/cam-bien-chat-luong-khong-khi-mq-139), [Buzzer 5v 2505A](https://shopee.vn/C%C3%B2i-Xung-5V-12x25MM-USP-2505A-i.151571719.9926169242). The node will collect data from sensors include: temperature, humidity, percentage CO of smophere,.... and sends to the Gateway. Source code of the nodes implementation in this project you can find [here](https://github.com/tovanhieu/LoraProject/blob/master/Raspberrypi%20Zero-Node/LORA_NODE_01_encrypted.py)<br>
#### Block diagram
![Screenshot 2023-09-20 152042](https://github.com/tovanhieu/LoraSX1278-Raspberrypi/assets/26000753/7314a3fa-8923-4f38-abfd-eb6f5166c908)

![Screenshot 2023-09-15 153852](https://github.com/tovanhieu/LoraSX1278-Raspberrypi/assets/26000753/d05df0bf-b602-43f0-b2c6-11e40e0fce68)

2. **Gateway**: I use Raspberry Pi 3 B+ integrated with module Lora-Ra 02 SX1278, after receiving data from nodes, gateway will send data to the Web Server in running in Cloud, I use Firebase and GoogleCloud to store and share datas with the monitor Web Application and the Mobie Application via API. Source code of the gateway implementation in this project you can find [here](https://github.com/tovanhieu/LoraSX1278-Raspberrypi/blob/master/RaspberryPi-Gateway/LORA_Gateway-01_encrypted.py)<br>
#### Block diagram
![Screenshot 2023-09-20 152458](https://github.com/tovanhieu/LoraSX1278-Raspberrypi/assets/26000753/b6f740de-5876-41ba-b84b-e633b73199c5)

![Screenshot 2023-09-20 152600](https://github.com/tovanhieu/LoraSX1278-Raspberrypi/assets/26000753/c2462c20-ad09-46a0-82a1-a62fbf7feb8b)<br>
3. **Web server**: Web server will recieve data from gateway and share with Mobile Application via API. The datas are showed and monitored in json format integrated with Firebase database.


### Last Update 
09/2023
## Referencece Links
#### https://github.com/rpsreal/pySX127x
#### https://pypi.org/project/pyLoRa/
#### https://github.com/rpsreal/LoRa_Ra-02_Arduino
#### https://console.firebase.google.com
#### https://cloud.google.com/
