#Ler um ângulo qualquer e mostrar o valor do seno, cosseno e tangente desse ângulo

import math 
angulo = float(input('Qual o ângulo?'))
angulo = math.radians(angulo)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O valor do seno é {} , o valor do cosseno é {:.3f} e o valor da tangente é {}'.format(seno , cosseno , tangente))