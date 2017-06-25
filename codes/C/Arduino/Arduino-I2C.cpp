#include <Wire.h>
 
#define ADDR 0x04
int x = 0;
 
void setup (void)
{
   pinMode (13, OUTPUT);
   Serial.begin (9600);
   Wire.begin (ADDR);
 
   // Define callbacks para a comunicacao i2c:
   Wire.onReceive (receiveData);
   Wire.onRequest (sendData);
}
 
void loop (void)
{
   delay (100);
}
 
// callback chamado ao receber dados:
void receiveData (int byteCount)
{
 
   while(Wire.available())
   {
      x = Wire.read();
      Serial.print("Recebido: ");
      Serial.println(x);
   }
}
 
// callback usado ao enviar dados:
void sendData(void)
{
   Wire.write(number);
}
