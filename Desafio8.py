#Ler um valor em metro e mostrar o resultado em centimetros e milimetros
valor = float(input('Qual é o valor em metros? '))
centimetros = int(valor * 100)
milimetros = int(valor * 1000)
print('O valor em centimetros é: {} e o valor em milimetros é: {}'.format( centimetros , milimetros))