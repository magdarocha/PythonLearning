#Programa para aprovar um empréstimo bancário para comprar uma casa
# O programa deve perguntar o valor da casa, salário e em quantos anos vai pagar
# Calcular o valor da prestação mensal, sabendo que não pode exceder 30% do salário, caso contrário o empréstimo é recusado

valor = float(input(' Qual o valor da casa? '))
salario = float(input(' Qual é o teu salário? '))
anos = int(input(' Em quantos anos vais pagar? '))

prestacao = valor / (12 * anos)
limite = salario * 0.30

print( ' A sua prestação é de {:.2f} euros'.format(prestacao))

if prestacao > limite:
    print(' O empréstimo foi recusado ')

else:
    print(' O empréstimo foi aceite ')