#Criar um programa que leia vários numeros e coloque numa lista
#Criar duas listas extra que vão conter numeros pares e impares escritos, respetivamente
#No final mostrar o conteudo das três listas geradas

lista = []

while True:
    numero = int(input(' Escreve um número: '))

    if numero < 0:
        break
    lista.append (numero)

lista_par = []
lista_impar = []

for i in lista:
    if i%2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print (lista, lista_par, lista_impar)

