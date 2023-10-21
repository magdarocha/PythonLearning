#Refazer o exercício 9 com a função for
#Ler um número inteiro e mostrar a sua tabuada

numero = int(input(' Escreve um número: '))

for i in range( 1, 11):
    tabuada = numero * i
    print('{} x {} = {}'.format( numero, i , tabuada))