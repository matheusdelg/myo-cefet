import time
import os
import serial
 
# Espera-se que o valor seja alterado
# depois da execucao de setupConn em
# onPeriodic apenas na primeira chamada
connSerial = None
 
def emgHandler (emg, moving):
    time.sleep(0.01)
 
def setupConn (pn, br):
 
   # Callback do EMG:
   myo.onEMG = emgHandler
 
   # Trocar portas USB e detectar Arduino na porta desejada:
   print "Delay de 10s para conectar Arduino..."
   time.sleep(10)
 
   print "Verificando existencia de ", pn, " na lista a seguir:\n"
   print os.system("ls /dev/tty*"), "\n"
   
   try:
      # Conexao serial:
      temp = serial.Serial(pn, br)
      print "Conexao realizado com sucesso."
      return temp
     
   except SerialException:
      print "Erro ao conectar-se a ", pn, "com baud-rate = ", br
     
def onPeriodic ():
     
     # Primeira chamada ou em caso de falha na conexao:
     if connSerial is None:
        connSerial = setupConn ("/dev/ttyUSB0", 9600)
     # Se ja existe conexao, mostrar dados recebidos:  
     else:
       print connSerial.readline()
