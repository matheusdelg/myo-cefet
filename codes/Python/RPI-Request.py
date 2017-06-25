import serial   # Para a comunicacao USB
import time     # Para o comando sleep
 
# Inicia a comunicacao com a porta ttyUSB0 do Raspberry.
# Com o Arduino desligado, digite "ls /dev/tty*" no terminal.
# Em seguida, conecte o MCU e repita o comando acima. O novo
# valor aparecido corresponde a porta USB na qual o Arduino
# esta conectado.
commSerial = serial.Serial('/dev/ttyUSB0', 9600)
led = 0
 
while True:
   print "acendendo o LED ", led, ": "
   commSerial.write(str(led))
   # Repete o valor de 0 a 7
   led = (led + 1) & 7
   # Delay de 1 segundo
   time.sleep(1)
