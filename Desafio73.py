#Criar tupla com os 10 primeiros colocados da tabela do campeonato de futebol na ordem de colocação
# Mostrar: apenas os 5 primeiros colocados
#Os ultimos 4 colocados da tabela
#Uma lista com as equipas em ordem alfabetica
#Em que posição da tabela está a equipa do Porto

colocados = ('Benfica', 'Sporting', 'Porto', 'VitoriaSC', 'Braga', 'Boavista', 'Moreirense', 'Famalicão', 'Estrela', 'Portimonense')

print(f'Os 5 primeiros colocados são {colocados[0:5]}')

print(f' Os 4 últimos colocados são {colocados[-4:]}')

print(f'Equipas por ordem alfabética: {sorted(colocados)}')

print(f'A equipa do Porto está na {colocados.index('Porto')+1} posição')

