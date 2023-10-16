#Programa que leia um número inteiro e mostre no ecrã o seu sucessor e o antecessor

numero = int(input('Escreve um número: '))
antecessor = numero - 1 
sucessor = numero + 1
print('O número anterior é: {} e o número posterior é: {}'.format(antecessor , sucessor))