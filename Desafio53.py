#Ler uma frase qualquer e dizer se é um palíndromo, desconsiderando os espaços.

frase = str(input(' Escreva uma frase '))

semespaco = frase.replace(' ' , '')
semespaco = semespaco.upper()

aocontrario = ""
for i in range(len(semespaco)-1, -1, -1):
    aocontrario = aocontrario + semespaco[i]
print(aocontrario)
if semespaco == aocontrario:
    print(' É polindromo')
