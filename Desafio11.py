#Ler a largura e a altura de uma paredes em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m2

largura = float(input('Qual é a largura?'))
altura = float(input('Qual é a altura?'))
area = largura * altura
tinta = area / 2
print('A área da parede é {} e são necessários {} litros de tinta para a pintar'.format( area , tinta))