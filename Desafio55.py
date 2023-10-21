#Ler o pesos de cinco pessoas. Mostrar qual foi o maior e o menor peso lido.

maior = 0
menor = 200


for i in range(1, 6):
    peso = float(input(' Escreve o teu peso: '))
    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso

print(' O peso maior é {}, o peso menor é {}: '.format(maior , menor))
