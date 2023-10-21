#Ler o ano de nascimento de um jovem e informar de acordo com a idade:
#Se ele ainda se vai alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistar
#Também deve mostrar o tempo que falta ou que passou do prazo

ano = int(input(' Qual o teu ano de nascimento? '))
idade = 2023 - ano 

if 18 <= idade < 21:
    print (' Ainda te podes alistar ')
    prazo = 21 - idade
    print (' Ainda tens {} anos '.format (prazo))
elif idade == 21:
    print ( ' Está na hora de te alistares')
elif idade > 21:
    print (' Já não te podes alistar ')
    prazo1 = idade - 21
    print(' Passaram {} anos depois do prazo. '.format( prazo1))
else:
    print (' És menor de idade. Não te podes alistar')

