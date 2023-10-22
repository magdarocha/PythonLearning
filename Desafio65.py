#Ler vários numeros inteiros
# Mostrar a média entre todos e qual o maior e menor
# O programa deve perguntar À pessoa se quer continuar a escrever numeros

numero = 0
media = 0
contagem = 0
soma = 0
maior_numero = 0
menor_numero = 9999999
pergunta = ''

while pergunta != 'N':
    numero = int(input(' Escreve um número: '))
    pergunta = input(' Quer continuar? [S/N] ').upper()

    contagem = contagem + 1
    soma = soma + numero 

    if numero > maior_numero:
        maior_numero = numero
    
    if numero < menor_numero:
        menor_numero = numero

    
    
media = soma / contagem

print(' A média dos numeros é {} '.format(int(media)))

print(' O maior numero é {} '.format(maior_numero))

print('O menor numero é {} '.format(menor_numero))