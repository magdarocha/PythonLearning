#Ler o nome e peso de várias pessoas guardando numa lista. No fim mostrar
#Quantas pessoas foram inseridas
#Uma lista das pessoas mais pesadas
#Uma lista das pessoas mais leves

lista = []

while True:
    
    nome = str(input(' Nome: '))
    peso = float(input('Peso: '))

    continuar = input('Quer continuar? [S] ou [N]').upper()

    pequena_lista = [nome , peso]

    lista.append(pequena_lista[:])
    
    if continuar == 'N':
        break

print ( f'Foram inseridas {len(lista)} pessoas ')

mais_pesadas = [['' , 0],['' , 0]]

for p in lista:
    mais_pesadas = sorted(mais_pesadas, key= lambda x:x[1])
    if p[1] > mais_pesadas[0][1]:
        mais_pesadas[0] = p
    elif p[1] > mais_pesadas[1][1]:
        mais_pesadas[1] = p

print(f'As duas pessoas mais pesadas são estas {mais_pesadas}')

menos_pesadas = mais_pesadas

for p in lista:
    menos_pesadas = sorted(menos_pesadas, key= lambda x:x[1], reverse=True)
    if p[1] < menos_pesadas[0][1]:
        menos_pesadas[0] = p
    elif p[1] < menos_pesadas[1][1]:
        menos_pesadas[1] = p

print(f'As duas pessoas menos pesadas são estas {menos_pesadas}')