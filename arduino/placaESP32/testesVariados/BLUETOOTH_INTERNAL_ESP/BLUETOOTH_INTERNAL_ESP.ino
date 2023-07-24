#include "BluetoothSerial.h"


BluetoothSerial SerialBT;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);
  SerialBT.begin("RedeESP32");
  Serial.println("The device started, now you can pair it with bluetooth");
}

void loop() {
  // put your main code here, to run repeatedly:

  if( Serial.available() ){
    SerialBT.write(Serial.read());
    }

  if(SerialBT.available()){

    char recebido = SerialBT.read();
    Serial.write(recebido);
    
    }

    delay(20);
}
