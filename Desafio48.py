#Soma entre todos os números impares que são múltiplos de 3 e que se encontram no intervalo de 1 ate 500

soma=0
for i in range(1,501):
    resto = i%2
    if resto == 1:
        multiplo = i%3
        if multiplo == 0:
            soma = soma + i
              
print(soma)