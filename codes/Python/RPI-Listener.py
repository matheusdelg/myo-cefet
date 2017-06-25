import serial
 
commSerial = serial.Serial('/dev/ttyUSB0', 9600)
 
print "Ouvindo..."
 
while True:
   print "Arduino diz: ", commSerial.readline()
