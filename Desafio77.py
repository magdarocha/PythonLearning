#Criar uma tupla com várias palavras e mostrar para cada palavra quais são as vogais

palavras = ('nao', 'sei' , 'programar' , 'tenho' , 'pensamento' , 'de' , 'enfermeira')

for palavra in palavras:
    print(f"A palavra {palavra} tem como vogal: ", end="")
    for i in range(0,len(palavra)):
        if palavra[i] in "aeiou":
            print(f"{palavra[i]} ", end="")
    print()