#Faça um programa que tenha uma função chamada maior(), que receba os parametros com valores inteiros
#O programa tem que analisar todos os valores e dizer qual é o maior


def maior(numeros):
    """Esta função recebe parâmetros comvalores inteiros e diz qual o valor maior"""
    o_maior = 0

    for i in numeros:
        if i > o_maior:
            o_maior = i
    return o_maior

o_maior = maior([3,6,4,8,6])

print(f'O número maior é {o_maior}')