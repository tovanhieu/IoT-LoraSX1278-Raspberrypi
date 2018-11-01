//Woon Jun Shen
//UM402 (433 MHz UART)
#include <SoftwareSerial.h>
#include "dht.h"
#define dht_apin A0// Analog Pin sensor is connected to
#define dht_type DHT11
dht DHT;
SoftwareSerial mySerial(2, 3); //TX, RX
// gnd SET_A and SET_B for Normal Mode (Send and Receive)
void setup() {
  Serial.begin(115200);
  mySerial.begin(115200);
  Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000);//Wait before accessing Sensor
}
void writeString(String stringData){
  for(int i =0; i < stringData.length();i++)
  {
    Serial.write(stringData[1]);
    }
  }
void loop() {
    DHT.read11(dht_apin);
    Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(DHT.temperature);
    Serial.println("C  ");
  //Fastest should be once every two seconds.
  if(Serial.available() > 0){//Read from serial monitor and send over UM402
    String input = Serial.readString();
    mySerial.println(input); 
  }
  if(mySerial.available() > 1){//Read from UM402 and send to serial monitor
    String input = mySerial.readString();
    Serial.println(input);    
  }
    mySerial.write((byte)DHT.humidity);
    mySerial.write((byte)DHT.temperature);
  delay(2000);
}
