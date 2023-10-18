#Ler três numeros e dizer qual é o maior e o menor

numero1 = input(' Diga-me um número ')
numero2 = input(' Diga-me outro número ')
numero3 = input(' Diga-me um ultimo número ')

if numero1 > numero2:
    if numero3 < numero1:
        print(' O {} é o maior'.format( numero1 ))
    else:
        print(' O {} é o maior'.format( numero3 ))
    

else:
    if numero2 > numero3:
        print( ' O {} é o maior'.format( numero2))
    else:
        print(' O {} é o maior'.format( numero3 ))

if numero1 < numero2:
    if numero3 > numero1:
        print(' O {} é o menor'.format( numero1 ))
    else:
        print(' O {} é o menor'.format( numero3 ))
    

else:
    if numero2 < numero3:
        print( ' O {} é o menor'.format( numero2))
    else:
        print(' O {} é o menor'.format( numero3 ))