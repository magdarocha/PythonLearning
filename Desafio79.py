#Escrever varios valores numericos numa lista
#Caso ja existe o numero não é adicionado
# No fim são exibidos todos os valores unicos escritos, em ordem crescente

lista = []

numero = 0

while True:
    numero = int(input(' Escreve um número: '))
    
    if numero in lista:
        print('O número já existe na lista ')
    else:
        lista.append(numero)
   
    if numero == 0:
        break

lista.sort()

print(f' A lista ordenada é {lista}')