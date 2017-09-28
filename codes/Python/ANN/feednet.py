from nnkit.network import ANN
from nnkit.train   import Trainer
from nnkit.compare import *
import numpy as np
import sys

def active (a, b):
   if a > b:
     return 1
   else:
     return 0

def main (arg1, arg2):

   Lambda  = 1e-5
   minAtiv = 80

   data = np.loadtxt(arg1)
   (nData, dSize) = data.shape

   # Entrada: media (mean),
   #          dp (sd),
   #          RMS (rms),
   #          maximo absoluto (peak),
   #          ativacao (ativ)   
 
   mean = np.zeros ((dSize, 1))
   sd   = np.zeros ((dSize, 1))
   rms  = np.zeros ((dSize, 1))
   peak = np.zeros ((dSize, 1))
   ativ = np.zeros ((dSize, nData))  

  # print data.shape

   for col in range (0, dSize):

      mean[col] = np.mean(data[:,col])
      sd[col]   =  np.std(data[:,col])
      peak[col] = np.amax(data[:,col])
      rms[col]  = np.sqrt (np.mean(np.square(data[:,col])))
      ativ[col] = map (lambda x : 1 if (x > minAtiv) else 0, list(data[:, col]))

   nInput  = np.concatenate((mean, sd, rms, peak))
   nOutput = np.zeros((dSize * 4, 1))

   nInput = nInput / np.amax(nInput)

   N = ANN (1, dSize * 4, 1, Lambda)
   N.loadWeights(arg2)

   T = Trainer (N)   
   T.train (nInput, nOutput)
  
   N.saveWeights(arg2)
   print N.forward(nInput).shape

  
if __name__ == "__main__":
   main (sys.argv[1], sys.argv[2])
