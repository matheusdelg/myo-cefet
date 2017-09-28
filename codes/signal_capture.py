import os, time
import numpy as np

scriptTitle = "Captura de sinais"
scriptUrl   = "cefet.ger.myo.signal_capture"

if not os.path.exists ("logs/"):
   os.makedirs ("logs/")

t0     = time.time()
fname  = "logs/" + str(time.asctime())
dtmx   = np.zeros ((1, 8))  


def onEMG (emg, moving):
   global dtmx

   emg  = np.reshape(emg, (1, 8))
   print emg    
   dtmx = np.concatenate((dtmx, emg))

def onPeriodic ():
   global t0

   tf = time.time()

   print tf - t0
   if (tf - t0 > 30):
      t0 = tf
      np.savetxt(fname, dtmx)
