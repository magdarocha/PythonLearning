#Ler a idade e sexo de várias pessoas. A cada pessoa inscrita o programa deve perguntar se o utilizador quer ou não continuar.
#No final mostrar: quantas pessoas têm mais de 18 anos, quantos homens estão inscritos e quantas mulheres têm menos de 20 anos

contagem_18anos = 0

contagem_homens = 0

contagem_mulheres_menos20anos = 0


while True:
    idade = int(input(' Que idade tens? '))
    sexo = str(input(' Qual é o teu sexo? ')).upper()

    continuar = input((' Quer continuar? [S,N] ')).upper()
    
    
    if idade > 18:
        contagem_18anos += 1 

    if sexo == 'M':
        contagem_homens += 1

    if sexo == 'F':
        if idade < 20:
            contagem_mulheres_menos20anos += 1


    if continuar == 'N':
        break

print( f'{contagem_18anos} têm mais que 18 anos! Estão inscritos {contagem_homens} homens! {contagem_mulheres_menos20anos} são mulheres e têm menos de 20 anos! ')


