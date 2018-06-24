clc; close all;
%1 = fist, 2 = fs, 3 = rest

T = 0.15;

ativo  = [];
inicio = [];
ordem  = [];
esperado = [1 1 1 1 1 2 2 2 2 2 0 0 0 0 2 2 2 2 2 1 1 1 1 1]';
            
disp ('Processando...');

for i = 0:23
   file = importdata(strcat (num2str(i), '.csv'));
   data = file.data;
   
   act = [];
   sta = [];
   
   %figure (i+1);
   for j = 2:9
      %subplot (4, 2, j-1);      
      emg = data (:, j);
      emg = emg + 128;
      emg = emg / 256;
      emg = emg - 0.5;
      emg = emg * 2;
      %plot (emg)

      act = [act ton(emg, T)];
      sta = [sta tst(emg, T)];
   end
   
   [dummy, ord] = sort (sta);
   
   ativo  = [ativo;  act];
   inicio = [inicio; sta];
   ordem  = [ordem;  ord];
end

disp ('Pronto! Salvo em "dados.csv"');

csvwrite ('dados.csv', [esperado ativo ordem inicio]);
clear dummy ord act sta data file emg i j
    
