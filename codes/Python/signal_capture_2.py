import os, time
import numpy as np

scriptTitle = "Captura de sinais"
scriptUrl   = "cefet.ger.myo.signal_capture"

np.set_printoptions(suppress = True)
path = "input/"

if not os.path.exists (path):
   os.makedirs (path)

dc = open("dataCounter", "r")
dataCounter = int(dc.read())
dc.close()

dc = open("dataCounter", "w")
dc.write(str(dataCounter + 1))
dc.close()

t0     = time.time()
fname  = path + str(dataCounter) + ".myodata"
dtmx   = np.zeros ((1, 8))  

print "leitura iniciada"

def onEMG (emg, moving):
   global dtmx

   emg  = np.reshape(emg, (1, 8))  
   dtmx = np.concatenate((dtmx, emg))

def onPeriodic ():
   global t0

   tf = time.time()

   if (tf - t0 > 0.05):
      t0 = tf
      np.savetxt(fname, dtmx)
