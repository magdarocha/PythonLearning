#Jogar par ou impar com o computador, o jogo é interrompido quando o jogador perder
#Mostra o total de vitórias consecutivas no final do jogo

import random

vitoria = 0

while True:
    numero = int(input('Escreve um número: '))
    par_impar = str(input(' Par ou impar? [P/I] ')).upper()

    numero_computador = random.randrange(1,11)
    print(f' O computador escolheu {numero_computador}')
    soma = numero + numero_computador

    if soma%2 == 0:
        if par_impar == 'P':
            print(' Ganhaste! ')
            vitoria += 1
        else:
            print(' Perdeste ')

            break
    elif soma%2 == 1:
        if par_impar == 'I':
            print(' Ganhaste! ')
            vitoria += 1
        else:
            print(' Perdeste ')

            break

print(f'Venceu {vitoria} vezes')   





