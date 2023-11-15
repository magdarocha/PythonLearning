# Criar um programa que vai ler vários números e colocar numa lista
# Depois disso mostrar quantos numeros foram escritos
# A lista de valores ordenada de forma decrescente
# Se o valor 5 foi escrito e está ou nao na lista

lista = []

while True:
    numero = int(input(' Escreve um número: '))
    if numero < 0:
        break
    lista.append(numero)

print (f'Foram escritos {len(lista)} numeros')

lista.sort(reverse=True)

print (f' Os número da lista por ordem descrescente são {lista}')

conta_5 = lista.count(5)

print (f' O número 5 apareceu {conta_5} vez')