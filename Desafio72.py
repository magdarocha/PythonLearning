# Fazer uma tupla com numeros de 0 a 10 por extenso
# O programa deve ler o numero e escrevê-lo

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')



while True:
    leitura = int(input(' Escreve um número de 0 a 10: '))
    if leitura > 10 or leitura < 0:
        print('Esse número não está na lista')
    else:
        break

print(f'Escreveste o número {numeros[leitura]}.')
