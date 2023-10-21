#Mostrar todos os números pares que estão no intervalo entre 1 e 50

for i in range(1,51):
    resto = i%2
    if resto == 0:
        print(i)