sudo nano /etc/modprobe.d/raspi-blacklist.conf
# Remova o caracter '#' na linha '#blacklist i2c-bcm2708'
# Pressione Ctrl+X para sair, Y para salvar as alterações
# e enter para confirmar.
 
sudo nano /etc/modules
# Digite 'i2c-dev' na última linha do arquivo. Salve as
# alterações e encerre o programa.
 
sudo apt-get install i2c-tools
sudo adduser pi i2c
 
ls -a /dev/i2c*
i2cdetect -y 0
# Troque '0' por '1' se é a segunda versão do RPi. A saída
# esperada para o comando será:
#
#      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
# 00:          -- -- -- -- -- -- -- -- -- -- -- -- --
# 10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 70: -- -- -- -- -- -- -- --
 
sudo apt-get install python-smbus
