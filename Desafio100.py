#Lista chamada números e duas funções sorteia() e somaPar()
#A primeira funçao vai sortear 5 numeros e colocá-los dentro da lista
#A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

import random

def sorteia(numeros):
    """Esta função sorteia 5 números de uma lista e retorna uma lista com esses números"""
    lista = random.choices(numeros, k=5)
    return lista

def somapar(lista):
    """Esta função soma os valores pares que vieram da lista"""
    soma = 0
    for i in lista:
        if i%2 == 0:
            soma = soma + i
    return soma


valores_sorteados= sorteia([3,4,5,6,7,8,9,4,3,5,6,7,8,2,3])

print(f'Os valores sorteados são: {valores_sorteados}')

somapares = somapar(valores_sorteados)

print(f'A soma dos valores pares é {somapares}')

