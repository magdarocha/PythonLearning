#Ler o nome, idade e sexo de 4 pessoas
# Mostrar a média de idade do grupo
# O nome do homem mais velhor
# Quantas mulheres têm menos de 20 anos
idades = 0
idade_mais_velha = 0
nome_do_mais_velho = ''
contagem_mulheres_abaixo_vinte = 0

for i in range(1,5):
    nome = str(input(' Escreve o teu nome: '))
    idade = int(input(' Diz-me a tua idade: '))
    sexo = str(input(' Qual é o teu sexo?: '))

    idades = idade + idades
    if sexo == 'masculino':
        if idade > idade_mais_velha:
            idade_mais_velha = idade
            nome_do_mais_velho = nome

    if sexo == 'feminino':
        if idade < 20:
            contagem_mulheres_abaixo_vinte = contagem_mulheres_abaixo_vinte + 1 


media = idades/4 

print( ' A média de idade do grupo é {} '.format(media))

print(' O nome do homem mais velho é {} '.format (nome_do_mais_velho))

print(' O número de mulheres com menos de 20 anos é {}'.format(contagem_mulheres_abaixo_vinte))

