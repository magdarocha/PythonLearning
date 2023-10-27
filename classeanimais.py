class Animais:

    def __init__(self, nome, especie, cor, altura, peso, idade):

        self.nome = nome

        self.especie = especie

        self.altura = altura

        self.peso = peso

        self.idade = idade

        self.cor = cor

    def comer(self, comida):

        self.peso += comida

        return print(f' O animal de nome {self.nome}, da espécie {self.especie}, com a cor {self.cor}, com a altura {self.altura}, comeu e ficou com o peso de {self.peso} kg. Tem a idade de {self.idade} anos.')


def soma(n1, n2):
    s = n1 + n2
    print(s)
    return s

gato = Animais('Snow', 'europeu comum','branco', '50 cm', 5, 7 )

gato.comer(1)

 
len([1, 2])

resultado = soma(1, 2)

resultado = resultado +2