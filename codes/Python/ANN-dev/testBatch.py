from BatcherClass import Batcher
from NeuralNetClass import NeuralNet

import matplotlib.pyplot as plt
import numpy as np
import os, time

# Especificacoes:

specs = {
         'nInputs'  : 32,
	 'nOutputs' : 5,
	 'nLayers'   : 3,
         'fin'  : 'pesos.w'
         }

poses = {
         'fist'         : np.reshape ([1, 0, 0, 0, 0], (1,5)),
	 'fingerSpread' : np.reshape ([0, 1, 0, 0, 0], (1,5)),
	 'waveIn'       : np.reshape ([0, 0, 1, 0, 0], (1,5)),
	 'waveOut'      : np.reshape ([0, 0, 0, 1, 0], (1,5)),
	 'rest'         : np.reshape ([0, 0, 0, 0, 1], (1,5))
        }

#### Inicio ####

print "Importando dados..."

path = 'input/'
fnames = []

for fn in os.listdir(path):
    if fn.endswith ('.myodata'):
       fnames.append (path + fn)

fnames = sorted (fnames, key = lambda x : int(x.split('/')[1].split('.')[0]))
print len(fnames), "arquivos encontrados."

print "Calculando resultados..."

batcher   = Batcher (fnames)
neuralNet = NeuralNet (specs)

print "Treinando rede..."

train = np.reshape(batcher.netInp, (len(batcher.stats), neuralNet.nInputs))

# 250 testes em diferentes poses foram feitos nesta etapa. a variavel "respx"
# corresponde a uma N-upla com N diferentes testes, especificadas a partir do
# dicionario "poses", declarado anteriormente

#respx = ([poses ['fist']] * 12) + ([poses ['rest']] * 10) + ([poses ['fist']] * 14) + ([poses ['rest']] * 6) + ([poses ['fingerSpread']] * 5) + ([poses ['fist']] * 20) + ([poses ['rest']] * 15) + ([poses ['fist']] * 22) + ([poses ['rest']] * 11) + ([poses ['fist']] * 17) + ([poses ['rest']] * 14) + ([poses ['fist']] * 32) + ([poses ['rest']] * 22) + ([poses ['fist']]) + ([poses ['rest']] * 3) + ([poses ['fist']]) + ([poses ['fingerSpread']] * 34) + ([poses ['fist']] * 10) 
            

respx = np.reshape(respx, (len(batcher.stats), neuralNet.nOutputs)) 

start = time.time()
neuralNet.train (train, respx)

print "tempo decorrido: ", (time.time() - start) / 3600, "horas"

neuralNet.exportW ('pesos.w')

print "Teste: "
for i in range (len(fnames)):
   print neuralNet.test (batcher.netInp[i])
