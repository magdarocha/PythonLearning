#Ler o nome de uma pessoa e dizer se tem silva no nome

nome = input('Escreve o nome de uma pessoa')

existe = 'SILVA' in nome.upper() 

print(existe)