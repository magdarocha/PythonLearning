#Ler 6 números inteiro e mostrar a soma daqueles que forem pares. Se o valor for impar desconsiderar.

soma = 0
for i in range(1,7):
    numero = int(input(' Escreva um número '))
    if numero%2 == 0:
        soma = soma + numero
print (soma)