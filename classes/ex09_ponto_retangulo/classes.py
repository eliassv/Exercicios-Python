class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Ponto na posição X: {:.2f} e Y: {:.2f} \n".format(self.x, self.y)


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
        return "Retângulo: largura: {} altura: {} \nInicio em x: {} e y: {} \n".format(
        self.largura, self.altura, self.ponto_inicio.x, self.ponto_inicio.y)
