# Mostrar uma contagem regressiva para o estourar de fogos de artifico andando de 10 até 0 com uma pausa de 1 segundo entre eles.

import time 

for i in range(10 , -1, -1):
    print(i)
    time.sleep(1)
print(' PUM PUM PUM')