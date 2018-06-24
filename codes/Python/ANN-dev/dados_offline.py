import numpy  as np
import pandas as pd
from NeuralNetClass import NeuralNet

def normalize (v):
    min_v = np.min(v);
    max_v = np.max(v);

    y = v - min_v;
    y = y / max_v;

    return y;


header = ['EXP', 'ACT1', 'ACT2', 'ACT3', 'ACT4', 'ACT5', 'ACT6', 'ACT7', 'ACT8',
		 'ORD1', 'ORD2', 'ORD3', 'ORD4', 'ORD5', 'ORD6', 'ORD7', 'ORD8',  
		 'SST1', 'SST2', 'SST3', 'SST4', 'SST5', 'SST6', 'SST7', 'SST8']

dataframe = pd.read_csv ("dados.csv", names=header);
matrix = dataframe.values;

t_act = np.reshape (matrix [:22,   1:9], (22, 8));
t_exp = np.reshape (matrix [:22,     0], (22, 1)) / 2;
t_ord = np.reshape (matrix [:22,  9:17], (22, 8)) / 8;
t_sta = np.reshape (matrix [:22, 17:25], (22, 8));

v_act = matrix [22:24,   1:9];
v_exp = matrix [22:24,     0] / 2;
v_ord = matrix [22:24,  9:17] / 8;
v_sta = matrix [22:24, 17:25];

specs = {
         'nInputs'  : 8,
	 'nOutputs' : 1,
	 'nLayers'   : 3,
}

nn_act = NeuralNet (specs);
nn_ord = NeuralNet (specs);
#nn_sta = NeuralNet (specs);

nn_act.importW ('act.w');
nn_ord.importW ('ord.w');
#nn_sta.importW ('sta.w');

nn_act.train (t_act, t_exp);
nn_ord.train (t_ord, t_exp);
#nn_sta.train (t_sta, t_exp);

print "ACT: Calculado: ", nn_act.test (np.reshape (v_act[0], (1, 8))), "Esperado: ", v_exp[0];
print "ORD: Calculado: ", nn_ord.test (np.reshape (v_ord[0], (1, 8))), "Esperado: ", v_exp[0];
#print "STA: Calculado: ", nn_sta.test (np.reshape (v_act[0], (1, 8))), "Esperado: ", v_exp[0];

print "ACT: Calculado: ", nn_act.test (np.reshape (v_act[1], (1, 8))), "Esperado: ", v_exp[1];
print "ORD: Calculado: ", nn_ord.test (np.reshape (v_ord[1], (1, 8))), "Esperado: ", v_exp[1];
#print "STA: Calculado: ", nn_sta.test (np.reshape (v_act[1], (1, 8))), "Esperado: ", v_exp[1];

print
print "ACT: erro = ", nn_act.erro();
print "ORD: erro = ", nn_ord.erro();
#print "STA: erro = ", nn_sta.erro();

op = input ("Salvar pesos? (1/0)")

if (op == 1):
   nn_act.exportW ('act.w');
   nn_ord.exportW ('ord.w');
   #nn_sta.exportW ('sta.w');
