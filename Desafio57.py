# Ler o sexo de uma pessoa mas só aceitar valores M e F
# Caso esteja errado pedir para escrever de novo até ter um valor correto

sexo = str(input(' Qual é o teu sexo?')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = input(' Escreva novamente o sexo ').upper()

