#Algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada

numero = int(input('Escreve um número'))
dobro = numero * 2
triplo = numero * 3
raizquadrada = numero **(1/2)
print('O dobro é: {}, o triplo é {} e a raiz quadrada é {:.3f}'.format(dobro, triplo, raizquadrada))