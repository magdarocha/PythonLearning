#Criar um programa onde se escreve uma expressão qualquer que use parenteses
#O programa deve analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta

expressao = str(input(' Escreve uma frase com parenteses: '))

parenteses = 0

for i in expressao:
    if i == '(':
        parenteses += 1
    if i == ')':
        parenteses -= 1
    if parenteses < 0:
        print (' Alguem fechou parênteses sem abrir, vou terminar')
        break
if parenteses == 0:
    print ('Está tudo correto ')
else:
    print ('Algo está mal ')