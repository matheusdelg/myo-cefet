from network import ANN
from compare import *
from train   import Trainer
import numpy as np

x = np.array([[4, 5.5], [4.5, 1], [9, 2.5], [6,2], [10, 10]], dtype = float)
y = np.array([[70], [89], [85], [75], [10]], dtype = float)
N = ANN(2, 5, 1, 0.000001)

x = x / np.amax(x)
y = y / np.amax(y)

print "y -> net(y)"
print y, "\n------------\n", N.forward(x)

ag = analyticalGrad(N, x, y)
ng = numericalGrad (N, x, y)

print "Analytical grad: ", sum(ag), ", ", ag.shape
print "Numerical grad: ",  sum(ng), ", ", ng.shape


T = Trainer(N)
T.train(x,y)

ag = analyticalGrad(N, x, y)
ng = numericalGrad (N, x, y)

print "Analytical grad: ", sum(ag), ", ", ag.shape
print "Numerical grad: ",  sum(ng), ", ", ng.shape

print "y -> net(y)"
print y, "\n------------\n", N.forward(x)


