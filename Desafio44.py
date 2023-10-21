#Calcular o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# Dinheiro/cheque: 10% de desconto
# Cartão:5% de desconto
# 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input( ' Qual o preço do produto? '))
condicao = str(input( ' Qual a condição de pagamento? '))

if condicao == 'dinheiro' or condicao == 'cheque':
    pagamento = preco - (preco * 0.10)
    print(' Tens que pagar {} euros'.format(pagamento))

elif condicao == 'cartão':
    pagamento1 = preco - (preco * 0.05)
    print (' Tens que pagar {} euros '.format(pagamento1))

elif condicao == '2x':
    print( preco )

elif condicao == '3x':
    pagamento3 = preco + (preco * 0.20)
    print (' Tens que pagar {} euros '.format(pagamento3))

    

