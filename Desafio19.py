# Um professor quer sortear um dos 4 alunos para apagar o quadro. Fazer um programa que ajude, a escolher um nome aleatoriamente

import random
nome1 = input('Escreve um nome')
nome2 = input('Escreve outro nome')
nome3 = input('Escreve mais um nome')
nome4 = input('Escreve o último nome')
lista = [nome1 , nome2 , nome3 , nome4]

print(random.choice(lista))