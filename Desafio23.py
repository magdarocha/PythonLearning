#Ler um numero de 0 a 9999 e mostre cada um dos digitos separados

numero = input(' Escreve um número: ')
unidade = numero[len(numero)-1]
dezena = numero[2]
centena = numero[len(numero)-3]
milhar = numero[0]

print('A unidade é: {} , a dezena é {} , a centena é {} e o milhar é {}'.format( unidade , dezena , centena , milhar))

#TODO Com operadores matemáticos