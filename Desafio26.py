#Ler uma frase e mostrar:
#Quantas vezes aparece a letra A
#Em que posição apareçe pela primeira vez
#Em que posição aparece pela ultima vez

frase = input(' Escreve uma frase ')
conta = frase.count('A')

print(conta)

#Posição 1 vez

encontrar = frase.find('A')

print(encontrar)

#Posiçao ultima vez

encontrar1 = frase.rfind('A')

print(encontrar1)