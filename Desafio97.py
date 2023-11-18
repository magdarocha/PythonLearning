#Ter uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
# Exemplo "Olá, Mundo" e saída : Olá, Mundo!

def escreva(mensagem):
    """Esta função imprime um texto com linhas na parte superior e inferior"""
    print('-' * len(mensagem))
    print(mensagem)
    print('-' * len(mensagem))

escreva('Olá, Mundo')