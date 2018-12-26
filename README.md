# LoraProject
This is Lora project for study purpose.
The project contain two properties:
+ Node: Using arduio with Lora-Ra 02 - SX1278, the node collect data including: temperature, humidity, percentage CO atsmophere,.... and send to the gateway node, code can be viewed in the file LORA_NODE.ino folowing LoraProject/Lora Ra-02/Arduino/LORA_NODE.ino
##### https://github.com/tovanhieu/LoraProject/blob/master/Lora%20Ra-02/Arduino/LORA_NODE.ino 
+ Gateway: Using raspberry Pi 3 B+, after collect data from node gateway analyze data and send to the cloud, we use Firebase to save data in the cloud and share with web and mobie app via API, code can be viewed in the file LORA_NODE.ino folowing LoraProject/RaspberryPi-Gatewayo
##### https://github.com/tovanhieu/LoraProject/blob/master/RaspberryPi-Gateway/rx_cont.py

### Author 
To Van Hieu
### Update 
11/2018
## Referencece Links
##### https://github.com/rpsreal/pySX127x
##### https://pypi.org/project/pyLoRa/
##### https://github.com/rpsreal/LoRa_Ra-02_Arduino
##### https://console.firebase.google.com
##### https://www.e-gizmo.net/oc/kits%20documents/LORA%20Module%20RA-02%20V.1/LORA%20Module%20RA-02%20V.1.pdf
