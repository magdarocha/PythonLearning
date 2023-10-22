#Ler varios numeros inteiros. O programa só para quando escrever o valor 999.
#No fim mostrar quantos numero foram escritos e qual foi a soma entre eles(sem contar o 999)

numero = 0
contagem = 0
soma = 0

while numero != 999:
    numero = int(input(' Escreva um número: '))

    contagem = contagem + 1
    soma = soma + numero

contagem = contagem - 1
soma = soma - 999

print(' Escreveste {} números. '.format(contagem))

print(' A soma dos números é {}. '.format(soma))
