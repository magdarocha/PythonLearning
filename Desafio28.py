#Fazer o computador pensar num número inteiro entre 0 e 5 e pedir para o utilizador tentar descobrir o numero escolhido pelo computador.
#O programa deve escrever na tela se o usuário venceu ou perdeu

numero = int(input('Pensei num número de 0 a 5. Qual foi?'))

if numero==3:
    print('Venceu')
else:
    print('Perdeu ')
    