#Ler o ano de de nascimento de sete pessoas. No final mostrar quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
menores = 0
maiores = 0

for i in range(1,8): 
    ano = int(input(' Escreva o seu ano de nascimento? '))
    idade = 2023 - ano
    if idade < 18:
        menores = menores + 1
    elif idade >= 18:
        maiores = maiores + 1
print(' {} pessoas ainda não atingiram a maioridade, {} pessoas já atingiram'.format( menores , maiores))
