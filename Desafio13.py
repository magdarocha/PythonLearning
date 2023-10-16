#Ler o salário de um funcionário e mostrar o novo salário com 15% de aumento

salario = float(input(' Qual é o teu salário?'))
novosalario = salario * (1+0.15)
print('O salário com aumento é: {}'.format(novosalario))