# Hướng dẫn
## Kết nối phần cứng:
\
    | Ra-02 LoRa BOARD1 |  RaspPi GPIO  | Ra-02 LoRa BOARD2 |  RaspPi GPIO  |
    |:------------------|:--------------|:------------------|:-------------:|
    |        MOSI       | GPIO 10       |        MOSI       | GPIO 10       |
    |        MISO       | GPIO 9        |        MISO       | GPIO 9        |
    |     SCK (SCLK)    | GPIO 11       |     SCK (SCLK)    | GPIO 11       |
    |        NSS        | GPIO 7 (CE1)  |        NSS        | GPIO 8 (CE0)  |
    |     DIO0 (IRQ)    | GPIO 25       |     DIO0 (IRQ)    | GPIO 2        |
    |        DIO1       | GPIO 24       |        DIO1       | GPIO 3        |
    |        DIO2       | GPIO 23       |        DIO2       | GPIO 14       |
    |        DIO3       | GPIO 18       |        DIO3       | GPIO 15       |
    |     RST (Reset)   | GPIO 22       |     RST (Reset)   | GPIO 4        |
    |        LED        | GPIO 27       |        LED        | GPIO 17       |
\
\
![gw](https://user-images.githubusercontent.com/26000753/48851590-04920080-edde-11e8-9475-ce73f5579403.PNG)
\
### Refrence
- https://github.com/rpsreal/pySX127x
