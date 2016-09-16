# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

# Possua uma classe chamada Ponto, com os atributos x e y.
# Possua uma classe chamada Retangulo, com os atributos largura e altura.
# Possua uma função para imprimir os valores da classe Ponto
# Possua uma função para encontrar o centro de um Retângulo.
# Você deve criar alguns objetos da classe Retangulo.
# Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo,
#   que deve ser um objeto da classe Ponto.
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto
#   que indique os valores de x e y para o centro do objeto.
# O valor do centro do objeto deve ser mostrado na tela
#  Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Ponto na posição X={:.2f} e Y={:.2f}".format(self.x, self.y)


class Retangulo:
    def __init__(self, largura, altura, ponto_inicio):
        self.largura = largura
        self.altura = altura
        self.ponto_inicio = ponto_inicio

    def centro_retangulo(self):
        x = self.ponto_inicio.x + (self.largura / 2)
        y = self.ponto_inicio.y + (self.altura / 2)

        centro = Ponto(x, y)

        print("Centro:", centro)

    def __str__(self):
        return "Retângulo: largura={} altura={} \nInicio em x={} e y={} \n".format(
        self.largura, self.altura, self.ponto_inicio.x, self.ponto_inicio.y)
