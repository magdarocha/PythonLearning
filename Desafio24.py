#Ler o nome de uma cidade e dizer se começa ou não com o nome "SANTO"

cidade = input('Escreve o nome de uma cidade ')
lista = cidade.split()
resultado = lista[0]

existe = 'SANTO' in resultado.upper()

print(existe)

#pedir uma lista da string e pedir a posição zero

