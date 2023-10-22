# Ler um número n inteiro qualquer e mostrar no ecrã os n primeiros elementos de uma sequÊncia fibonacci

numero = int(input(' Escreve um número: '))

fibonacci = [0,1]

while numero != len(fibonacci):
    proximo_elemento = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_elemento)

print(fibonacci)