#Ler um numero real qualquer pelo teclado e mostrar a sua porçao inteira
import math
numero = float(input('Escreve um número '))
inteira = math.trunc(numero)
print('A parte inteira do número é {}'.format(inteira))
