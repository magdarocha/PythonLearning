#Ler numero inteiro e pedir ao utilizados para escolher a base de conversão
# 1 para binário, 2 para octal, 3 para hexadecimal

numero = int(input(' Digite um número '))
conversao = int(input( ' Escolha a base de conversão, sabendo que 1 é binário, 2 é octal, 3 é hexadecimal '))

if conversao == 1:
    binario = bin(numero)
    print(binario)
elif conversao == 2:
    octal = oct(numero)
    print(octal)
elif conversao == 3:
    hexadecimal = hex(numero)
    print(hexadecimal)
else:
    print(' Opção não reconhecida ')
    
