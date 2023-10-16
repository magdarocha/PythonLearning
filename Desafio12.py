# Ler o preço de um produto e mostrar o seu novo preço com 5% de desconto

preco = float(input(' Qual é o preço do produto?'))
desconto = preco * 0.95
print('O preço do produto é {} e com desconto de 5pc fica a {}'.format( preco , desconto))