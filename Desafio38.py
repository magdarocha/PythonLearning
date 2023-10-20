#Ler dois numero inteiros, comparar e mostrar uma mensagem no ecrã:
#O primeiro valo é maior, o segundo valor é maior, não existe valor maior, são os dois iguais

numero1 = int(input(' Escreve um número '))
numero2 = int(input(' Escreve outro número '))

if numero1 > numero2:
    print(' O primeiro valor é maior')
elif numero1 < numero2:
    print( ' O segundo valor é maior ')
elif numero1 == numero2:
    print(' Não existe valor maior, os dois são iguais')
    