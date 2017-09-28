import numpy as np

class ANN (object):

   def __init__(self, nIn, nLay, nOut, Lambda):
      
       self.nIn  = nIn
       self.nOut = nOut
       self.nLay = nLay
       self.l    = Lambda
       self.W1   = np.random.randn(nIn, nLay)
       self.W2   = np.random.randn(nLay, nOut)

   def forward (self, x):    
	
       self.z2 = x.dot(self.W1)
       self.a2 = self.transf(self.z2)
       self.z3 = self.a2.dot(self.W2)
       self.yl = self.transf(self.z3)  

       return self.yl

   def J (self, x, y):

       self.yl = self.forward(x)
       erro    = (self.yl - y) ** 2
       w1s     = self.l * np.sum (self.W1 ** 2)
       w2s     = self.l * np.sum (self.W2 ** 2)

       ans = 0.5 * (sum (erro) + w1s + w2s) 

       return ans

   def dJ (self, x, y):

       self.yl = self.forward(x)

       delta3  = (self.yl - y) * self.dtransf(self.z3)
       delta2  = self.dtransf(self.z2)  * delta3.dot(self.W2.T)

       dJdW1   = np.dot(x.T, delta2) + self.l * (self.W1)
       dJdW2   = np.dot(self.a2.T, delta3) + self.l * (self.W2)    

       return dJdW1, dJdW2
                                                                                                            
   def transf (self, z):
       return 1 / (1 + np.exp(-z))

   def dtransf (self, z):
       return np.exp(-z) / ((1 + np.exp(-z)) ** 2)       

   def saveWeights (self, fname):
       data = np.concatenate ((self.W1.ravel(), self.W2.ravel()))
       np.savetxt(fname, data)

   def loadWeights (self, fname):
       data = np.loadtxt(fname)

       if data.shape != (0,0):
          W1_0 = 0
          W1_f =        int (self.nLay * self.nIn)
          W2_f = W1_f + int (self.nLay * self.nOut)

          self.W1 = np.reshape(data[W1_0 : W1_f], (self.nIn, self.nLay))
          self.W2 = np.reshape(data[W1_f : W2_f], (self.nLay, self.nOut))
       

