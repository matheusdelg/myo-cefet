# Título a aparecer no PyoConnect:
scriptTitle = "Leitor de EMG"
# Descrição da aplicação:
scriptDescription = "Leitura do EMG do Myo Armband"
# URL do script:
scriptURL = "cefet.ger.myo.teste"
 
# Processar os dados do EMG. A variável emg é do tipo Tuple
def lerEMG(emg, moving):
   file_emg = open("myo.emg.emg", "w")
   for data in emg:
     file_emg.write(str(data) + "\n")
    file_emg.close()
 
#Chamado ao destravar o Armband:
def onUnlock():
    # Seleciona a função anterior como Callback na entrada
    # de dados do EMG. Feita originalmente em <https://github.com/dzhu/myo-raw>
    myo.add_emg_handler(lerEMG)
    # Evita o travamento automático para não sobrecarregar
    # a lista de Handlers de EMG do PyoConnect
    myo.unlock("hold")
