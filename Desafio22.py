# Ler o nome completo de uma pessoa e mostrar: o nome com todas as letras maiusculas,
#com minusculas, 
# quantas letras ao todo sem considerar espaços, 
# quantas letras tem o primeiro nome

nome = input('Escreve o teu nome completo ')
#Letras maiúsculas
maiusculas = nome.upper()
print('O nome em maiusculas é' , maiusculas)

#Letras minusculas
minusculas = nome.lower()
print(' O nome em minusculas é' , minusculas)

#quantas letras sem espaços
semespaco = nome.replace(' ' , '' )
print(' O numero de letras é' , len(semespaco))

semespaco1 = len(nome) - nome.count(" ")
print(semespaco1)

#quantas letras tem o primeiro nome

#separar os nomes
#contar os caracteres do primeiro nome
separar = nome.split()
comprimento = len(separar[0])
print('O comprimento é' , comprimento)