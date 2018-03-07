import numpy as np

# Transforma as informacoes contidas nos arquivos em matrizes
# o campo "self.data" contem uma lista de matrizes (n,8) que
# representam a leitura feita pelo EMG. O campo "self.stats"
# contem uma lista de matrizes (4,8) processada contendo as
# estatisticas de cada entrada de "self.data". O ultimo campo 
# "self.netInp" contem uma lista de vetores (1,32), os valores 
# redimensionados de "self.stats" para entrada da rede neural.
#
# Tamanhos:
#	fnames      = l
#	self.data   = [l * (n x 8)]
#       self.stats  = [l * (4 x 8)]
#	self.netInp = [l * (1 x 32)]
#

class Batcher:

   def __init__ (self, fnl):
   # Construtor da classe:

       self.fnames = fnl   # Lista com nome dos arquivos
       self.data   = []    # Lista de matriz dos dados brutos
       self.stats  = []    # Lista de matriz dos dados processados
       self.netInp = []    # Lista de entrada para a ANN

       # Inicia o processamento:
       self.start ()

   def readFile (self, fname):
   # Importa dados do arquivo em parametro:

	with open (fname) as fread:
             self.data.append (np.loadtxt (fread))

   def start (self):
   # Faz a leitura e processamento dos dados:

       # Importa dados brutos para cada arquivo listado:
       for fname in self.fnames:
           self.readFile (fname)

       # Normaliza dados de acordo com os valores
       # maximos e minimos obtidos:
       unpckd = np.array ([[],[],[],[],[],[],[],[]]).T

       for elem in self.data:
         unpckd = np.concatenate ((unpckd, elem), axis = 0)
      
       absMax = max (unpckd.flat)
       absMin = min (unpckd.flat)
        
       # Processa os dados brutos em cada ocorrencia de "data":
       for subdata in self.data:
           self.getStat (subdata, absMax, absMin)

       self.nInputs = len (self.stats)

   def printData (self):
   # Mostra na tela os dados brutos:

       for subdata in self.data:
           print "Data: "
           print np.round (subdata * 100, 2), "\n"


   def printStats (self):
   # Mostra na tela os dados processados:

       for substats in self.stats:
           print "Stats: "
           print np.round (substats * 100, 2), "\n"

   def getStat (self, paramData, absMax, absMin):
   # Calcula as informacoes dos dados em parametro:

       medData = []  # Media das amostras
       stdData = []  # Desvio-padrao das amostras
       ampData = []  # Amplitude da onda
       rmsData = []  # raiz da media quadrada

       # Normalizado:
       normData = paramData - absMin
       normData = normData / absMax 

       for i in range (0, 8):

	   # Valores por coluna:
           sensorData = normData[:, i];
 
           # Calcula media, dp, amplitude e rms:
           medData.append (np.mean (sensorData))
           stdData.append (np.std  (sensorData))
           ampData.append (max (sensorData) - min (sensorData))
           rmsData.append (np.sqrt (np.mean (sensorData ** 2)))

       # Transforma as informacoes:
       dataList = np.reshape ([medData, stdData, ampData, rmsData], (4, 8))
       neurList = np.reshape ([medData, stdData, ampData, rmsData], (1, 32))

       # Adiciona a lista:
       self.stats.append  (dataList)
       self.netInp.append (neurList)
