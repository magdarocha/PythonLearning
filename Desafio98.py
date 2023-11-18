#Função chamada contador que receba 3 parâmetros: inicio, fim e passo e realize a contagem
#O programa tem que realizar três contagens através da função criada
# de 1 até 10, de 1 em 1
# de 10 até 0, de 2 em 2
# uma contagem personalizada

def contador(inicio,fim,passo):
    """Esta função recebe três parâmetros e realiza contagens, de um em um e de dois em dois"""
    if inicio > fim:
        c = fim
        paragem = inicio
    else:
        c = inicio
        paragem = fim

    while c <= paragem:
        print(c)
        c += passo

contador(1,10,1)
print('-'*10)
contador(10,0,2)
