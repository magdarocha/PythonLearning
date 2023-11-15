#Escrever cinco valores numéricos e colocar numa lista, já na posição correta de inserçao sem usar o sort
# No fim mostrar a lista ordenada no ecrã

lista = []

for i in range(0,5):
    numero = int(input(' Escreve um número: '))

    if len(lista) == 0:
        lista.append(numero)

    else:
        for i,n in enumerate(lista):
            if n > numero:
                lista.insert(i,numero)
                break
        if lista[-1] <= numero:
            lista.append(numero)
        

print(lista)
           
