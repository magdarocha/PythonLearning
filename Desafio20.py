#O professor quer sortear a ordem de apresentação dos trabalhos dos alunos. Fazer um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
nome1 = input('Escreva nome ')
nome2 = input('Escreva outro nome ')
nome3 = input('Escreva outro ')
nome4 = input('Escreva o último ')

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print(lista)
