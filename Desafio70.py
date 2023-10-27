#Ler o nome e preço de vários produtos
#Perguntar se quer continuar
# Qual o total gasto na compra
#Quantos produtos custam mais de 1000€
# Qual é o nome do produto mais barato

soma = 0
contagem = 0
mais_barato = 9999
nome_mais_barato = ''

while True:
    nome = str(input(' Escreve o nome de um produto: ' ))
    preco = float(input(' Qual é o preço: '))
    continuar = input((' Quer continuar?[S/N]')).upper()

    soma = soma + preco

    if preco > 1000:
        contagem += 1
    
    if preco < mais_barato:
        mais_barato = preco 
        nome_mais_barato = nome

    if continuar == 'N':
        break
   
    


     
print(f' A soma dos produtos é {soma}. {contagem} produtos custam mais de 1000€. O mais barato é {nome_mais_barato} ')