#Mostrar a tabuada de vários numeros um de cada vez, para cada valor escrito pelo utilizador.
# O programa é interrompido quando o numero solicitado for negativo



while True:
    numero = int(input(' Escreve um número: '))
    if numero < 0:
        break
    for i in range(1,11):
        tabuada = numero * i

        print (f' {numero} x {i} = {tabuada}')
                 