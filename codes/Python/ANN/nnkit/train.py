from scipy import optimize
from compare import *
from network import ANN
import numpy as np


class Trainer (object):

    def __init__(self, arg):
	self.N = arg

    def wrap (self, params, x, y):

	self.setParams (params)	

	custo = self.N.J(x, y)
	grad  = numericalGrad(self.N, x, y)
 	
	return custo, grad

    def callbackFunction (self, params):
	
	self.setParams(params)
	self.J.append(self.N.J(self.X, self.y))
	#self.testJ.append(self.N.J(self.testX, self.testy))

    def train (self, trainX, trainy, testX = 0, testy = 0):

	self.X = trainX
	self.y = trainy
#	self.testX = testX
#	self.testy = testy
	self.J = []
#	self.testJ = []

	params0 = self.getParams ()
	options = {'maxiter' : 900, 'disp' : True}

	_res = optimize.minimize (self.wrap, params0, jac = True, method = 'BFGS', args = (trainX, trainy), options = options, callback = self.callbackFunction)
	self.setParams(_res.x)
	self.optRes = _res

    def getParams (self):
        temp1 = np.array(self.N.W1.ravel())
        temp2 = np.array(self.N.W2.ravel())

        return np.concatenate((temp1, temp2))

    def setParams (self, params):
        w1_0 = 0
        w1_f =        int(self.N.nLay * self.N.nIn)
        w2_f = w1_f + int(self.N.nLay * self.N.nOut)

        self.N.W1 = np.reshape (params[w1_0 : w1_f], (self.N.nIn,  self.N.nLay))
        self.N.W2 = np.reshape (params[w1_f : w2_f], (self.N.nLay, self.N.nOut))
	
	

