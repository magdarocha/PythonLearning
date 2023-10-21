#Ler o ano de nascimento de um atleta e mostrar a categoria de acordo com a idade
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sénior
# Acima: Master

ano = int(input(' Qual o teu ano de nascimento? '))
idade = 2023 - ano 

if idade <= 9:
    print ( ' Mirim ')
elif 9 < idade <= 14:
    print (' Infantil ')
elif 14 < idade <= 19:
    print (' Junior')
elif 19 < idade <= 20:
    print (' Sénior')
elif idade > 20:
    print (' Master')

