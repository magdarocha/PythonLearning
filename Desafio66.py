# Ler vários numeros inteiros. O programa só para quando escrever 999.
# No fim mostrar quantos numeros foram digitados e qual foi a soma entre eles.

numero = 0
contagem = 0
soma = 0

while True:
    numero = int(input(' Escreva um número: '))
    if numero == 999:
        break
    contagem += 1
    soma += numero

print (f' Foram escritos {contagem} números e a soma deles é {soma}.')
