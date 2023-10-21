#Ler um numero inteiro e dizer se é ou não primo

numero = int(input(' Digite um número: '))
contagem = 0
for i in range( 1 , numero+1):
    resto = numero%i
    if resto == 0:
        contagem = contagem +  1

if contagem <= 2:
    print(' é um número primo ')

else:
    print (' não é um número primo ')