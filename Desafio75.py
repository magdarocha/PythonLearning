#Ler 4 valores e colocar numa tupla
#Quantas x apareceu o numero 9
#Em que posição foi digitado o primeiro numero 3
# Quais foram os numeros pares


valor1 = int(input('Escreve um número: '))
valor2 = int(input('Escreve um número: '))
valor3 = int(input('Escreve um número: '))
valor4 = int(input('Escreve um número: '))


tupla = (valor1 , valor2, valor3, valor4)

print(tupla)

print(f'O número 9 apareceu {tupla.count(9)} vezes')

print(f' O número 3 foi escrito na posição {tupla.index(3)+1}')

print('Os números pares são: ', end= "")
for i in tupla:
    if i%2 == 0:
        print (i, end=", ")
