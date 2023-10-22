#Melhorar o jogo do desafio 28, onde o computador vai pensar num número entre 0 e 10.
# O jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

import random

numero_computador = random.randrange(1,10)

escolha_do_jogador = int(input(' Adivinhe que número o computador pensou: '))

tentativas = 1

while escolha_do_jogador != numero_computador:
    escolha_do_jogador = int(input(' Erraste! Escolhe de novo: '))

    tentativas = tentativas + 1

print (' Finalmente acertaste!')

print (' Precisaste de {} tentativas '.format(tentativas))


