#Perguntar o salário de um funcionário e calcular o valor do seu aumento
# salarios superiores a 1250 euros calcular um aumento de 10%
# inferiores ou iguais o aumento é de 15%

salario = int(input( ' Escreve o teu salário '))

if salario > 1250:
   aumento = salario * 1.1
   print( ' O teu salário é {} '.format(aumento))

else:
   aumento1 = salario * 1.15
   print( ' O teu salário é {} '.format(aumento1))