# Ler dois valores e mostrar um menu no ecrã
# 1 para somar, 2 para multiplicar, 3 para maior , 4 para novos numeros e 5 para sair do programa
# O programa deve realizar a operação solicitada em cada caso

valor1 = int(input(' Escreve um número: '))
valor2 = int(input(' Escreve outro número: '))

opcao = 0

while opcao != 5:
    print(' Escolha 1 para somar')
    print(' Escolha 2 para multiplicar')
    print(' Escolha 3 para saber qual o número maior')
    print(' Escolha 4 para escrever novos números')
    print(' Escolha 5 para sair')
    opcao = int(input(' Qual é a opção? '))

    if opcao == 1:
        print(valor1 + valor2)
    elif opcao == 2:
        print(valor1 * valor2)
    elif opcao == 3:
        if valor1 > valor2:
            print(' O valor {} é maior. '.format(valor1))
        else:
            print('O valor {} é maior'.format(valor2))
    elif opcao == 4:
        valor1 = int(input(' Escreve um número: '))
        valor2 = int(input(' Escreve outro número: '))

print (' Saiu! ')
