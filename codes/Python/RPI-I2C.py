import smbus, time
bus = smbus.SMBus(0) # Para a segunda versao, use 1

arduino = 0x04 # Endereco do Arduino (slave)

def writeI2c(sent):
   bus.write_byte(arduino, sent)
   return -1

def readI2c():
   received = bus.read_byte(arduino)
   return received

while True:
   var = input("1 - 9: ")
   if not var:
      continue
   
   writeI2c(var)
   print "Enviado ao Arduino: ", var
   time.sleep(1)

   var = readI2c()
   print "Recebido do Arduino: ", var
