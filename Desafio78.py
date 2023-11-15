# Ler 5 valores numéricos e guardar numa lista
#No fim mostrar o maior e o menor valor e as susa respetivas posiçoes na lista

valores = list()

menor_numero = 999
maior_numero = 0

index_maior = 0
index_menor = 0

for i in range(0,5):
    valores.append(int(input(' Escreve um valor: ')))


    if valores[-1] > maior_numero:
        maior_numero = valores[-1]
        index_maior = i

    if valores[-1] < menor_numero:
        menor_numero = valores[-1]
        index_menor = i
        

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

print(f' O maior número é {maior_numero} e está na posição {index_maior}')

print(f' O menor número é {menor_numero} e está na posição {index_menor}')


