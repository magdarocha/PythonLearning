#Ler o comprimento do cateto adjacente de um triângulo retângulo e calcular o mostrar o comprimento da hipotenusa

import math
catetooposto = float(input('Qual o comprimento do cateto oposto?'))
catetoadjacente = float(input('Qual é o comprimento do cateto adjacente?'))
hipotenusa = math.hypot(catetooposto , catetoadjacente)
print('O comprimento da hipotenusa é: {}'.format(math.trunc(hipotenusa)))