// Inicialização: Cria uma comunicação de Baud Rate = 9600
void setup (void)
{
  Serial.begin(9600);
}
 
// Loop: Envia mensagens via USB a cada 1s:
void loop (void)
{
    Serial.println("Ola, Rasp!");
    delay(1000);
}
