#Programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.

def area(largura , comprimento):
    """Esta função calcula a área de um terreno"""
    areatotal = largura * comprimento 
    return areatotal


area1 = area(2 , 5)

print(f' O valor da área da sala é {area1}')

