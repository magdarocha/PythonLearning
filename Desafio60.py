# Ler um número qualquer e mostrar o seu fatorial

numero = int(input(' Escreve um número: '))

fatorial = numero 

while numero != 1:
    numero = numero - 1
    fatorial = fatorial * numero

print (' O fatorial é {}. '.format(fatorial))


