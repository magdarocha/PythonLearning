#Perguntar a distancia de uma viagem em Km.
#Calcular o preço da passagem, cobrando 50 centimos por km para viagens até 200 km
# Cobrar 45 centimos por km para viagens mais longas

distancia = float(input(' Qual a distância da viagem? '))

if distancia < 200:
    calculo = distancia * 0.50 
    print(' A viagem custa {} '.format(calculo))

else:
    calculo2 = distancia * 0.45
    print(' A viagem custa {} '.format(calculo2))
