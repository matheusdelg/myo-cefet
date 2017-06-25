void setup (void)
{
   // Inicia a comunicaçao com Baud-Rate = 9600
   Serial.begin(9600);
   // Seta os pinos 2,3 e 4 como saida e os pinos
   // 0 e 1 como entrada (RX e TX)
   DDRD = 0x28;
}
 
void loop (void)
{
   if(Serial.available())
   {
     // Soma com o complemento de 2
     // do caracter - '0'
     byte x = Serial.read() + 0xD0;
     
     // Coloca o valor de x nos pinos 3,4
     // e 5 do Arduino UNO. Ignorar RX e
     // TX implica em multiplicar a entrada
     // x por 4, ou deslocar 2 bits
     PORTD = x << 2;
   }
}
