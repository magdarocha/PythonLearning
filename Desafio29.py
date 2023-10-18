#Ler a velocidade de um carro, se ultrapassar 80 km/h mostrar mensagem a dizer que foi multado. 
#A multa custa 7 euros por cada km acima do limite.

velocidade = int(input('Qual a velocidade do carro?'))

if velocidade > 80:
    print('Foi multado')
    dif = velocidade - 80
    multa = 7 * dif
    print(' Tem que pagar {} euros '.format(multa))
else:
    print('Não foi multado')
      