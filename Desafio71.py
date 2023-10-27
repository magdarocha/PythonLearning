# Simular um ATM
# Perguntar o valor a levantar
#O programa deve informar quantas notas de cada vão ser levantadas
#Só existem notas de 50 , 20, 10 e 1

notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0 


valor = int(input(' Quanto quer levantar? '))

while valor != 0:
    if valor >= 50:
        notas_50 += 1
        valor = valor - 50
    elif valor >= 20:
        notas_20 += 1
        valor = valor - 20
    elif valor >= 10:
        notas_10 += 1
        valor = valor - 10
    elif valor >= 1:
        notas_1 += 1
        valor = valor - 1

print(f' Vão-lhe ser dadas {notas_50} notas de 50, {notas_20} notas de 20, {notas_10} notas de 10 e {notas_1} notas de 1')
