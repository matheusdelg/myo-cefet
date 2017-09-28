from network import ANN
import numpy as np

def analyticalGrad (N, x, y):
   dJdW1, dJdW2 = N.dJ(x, y)

   return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))

def numericalGrad (N, x, y):
  
   vW1   = N.W1.ravel()
   vW2   = N.W2.ravel()
   tam   = len (vW1) + len (vW2)

   ngrad1 = np.zeros((len(vW1), ))
   ngrad2 = np.zeros((len(vW2), ))
   ptb1  = np.zeros(N.W1.shape)
   ptb2  = np.zeros(N.W2.shape)

   N0 = N

   for i in range (len(vW1)):

      ptb1.ravel()[i] = 1e-4
      N.W1 = N0.W1 + ptb1
      err1 = N.J(x,y)

      N.W1 = N0.W1 - ptb1
      err2 = N.J(x,y)
  
      ngrad1[i] = (err1 - err2) / 2e-4
      ptb1.ravel()[i]   = 0

   for i in range (len(vW2)):

      ptb2.ravel()[i] = 1e-4
      N.W2 = N0.W2 + ptb2
      err1 = N.J(x,y)

      N.W2 = N0.W2 - ptb2
      err2 = N.J(x,y)
  
      ngrad2[i] = (err1 - err2) / 2e-4
      ptb2[i] = 0
     
   N = N0
   ngrad = np.concatenate((ngrad1, ngrad2))
   return ngrad.ravel()
