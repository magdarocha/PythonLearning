#Ler o peso e a altura de uma pessoa
#Calcular o IMC e mostrar o status de acordo coma  tabela
#Abaixo de 18.5: abaixo do peso
#Entre 18.5 e 25: Peso ideal
#Entre 25 e até 30: Sobrepeso
#30 Até 40: Obesidade
#Acima de 40: Obesidade mórbida

peso = float(input(' Quanto pesas? '))
altura = float(input(' Quanto medes? '))
IMC = peso / altura**2

if IMC < 18.5:
    print(' Abaixo do peso ')
elif 18.5 <= IMC <= 25:
    print( ' Peso ideal ')
elif 25 < IMC <= 30:
    print(' Sobrepeso ')
elif 30 < IMC <= 40:
    print(' Obesidade ')
elif IMC > 40:
    print( ' Obesidade Mórbida ')
    