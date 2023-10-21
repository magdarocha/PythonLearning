#Fazer o computador jogar o jogo "Pedra papel tesoura"


import random

jogo = str(input(' Escolhe pedra, papel ou tesoura: '))

lista = ['pedra' , 'papel' , 'tesoura']
escolha = random.choice(lista)

print(' O computador escolheu {}'.format(escolha))

if jogo == escolha:
    print (' Empatou')
elif jogo == 'pedra' and escolha == 'papel':
    print (' Você perdeu')
elif jogo == 'pedra' and escolha == ' tesoura':
    print (' Você ganhou')
elif jogo == 'papel' and escolha == 'pedra':
    print (' Você ganhou')
elif jogo == 'papel' and escolha == 'tesoura':
    print (' Você perdeu')
elif jogo == 'tesoura' and escolha == 'pedra':
    print (' Você perdeu')
elif jogo == 'tesoura' and escolha == 'papel':
    print ('Você ganhou')

