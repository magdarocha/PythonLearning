#Ler duas notas de um aluno e calcular a média
# Mostrar uma mensagem no final de acordo com a média atingida:
#Média abaixo de 5.0 Reprovado
#Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

nota = float(input( ' Qual foi a tua nota? '))
nota1 = float(input( ' Qual foi a tua segunda nota? '))
media = float(nota+nota1) / 2

if media <= 5.0:
    print (' Reprovado ')
elif 5.0 < media <= 6.9:
    print (' Recuperação ')
elif media >= 7.0:
    print (' Aprovado ')
