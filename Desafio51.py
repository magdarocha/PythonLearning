#Ler o primeiro termo e a razão de uma progressão aritmética
# No final mostrar os 10 primeiros termos dessa progressão

termo = int(input(' Diga-me o primeiro termo da PA '))
razao = int(input(' Diga-me a razão da PA '))

soma = termo
for i in range(1 , 11):
    soma = soma + razao
print(soma)