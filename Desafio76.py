#Ter uma tupla com nomes de produtos e respetivos preços na sequência
#No fim mostrar uma lista de preços organizada de forma tabular

produtos = ('Pão', 1 , 'Massa', 1.50 , 'Arroz', 1.20 , 'Comida de gato', 5)

print ('Tabela de preços')

for i in range(0, len(produtos), 2):
    print(f"{produtos[i]} ----------------------------------- {produtos[i+1]}")
