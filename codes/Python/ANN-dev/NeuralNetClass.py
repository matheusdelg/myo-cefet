import numpy as np
import neurolab as nl

class NeuralNet:

   def __init__ (self, specs):

       self.nInputs  = specs ['nInputs']
       self.nOutputs = specs ['nOutputs']
       self.layers   = specs ['nLayers']

       self.inp = [[0,1]] * self.nInputs
       self.out = ([self.nInputs] * self.layers) + [self.nOutputs]

       self.nn = nl.net.newff (self.inp, self.out)
       self.nn.trainf = nl.train.train_gd

       self.err = np.array ([])

       if 'fin' in specs.keys():
          self.fin = specs ['fin']
          self.importW (self.fin)

       if 'fout' in specs.keys():
          self.fout = specs ['fout']

   def importW (self, fin):
 	self.nn = nl.load (fin)

   def exportW (self, fout):
        self.nn.save (fout)

   def train (self, inp, out):
       self.err = np.array (self.nn.train (inp,
			    out, epochs = 3e5,
                            goal = 1e-2, show = 1e2))
   def test (self, inp):
       return self.nn.sim (inp)
