# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Square:
    def __init__(self, lado="0"):
        self.lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, valor):

        if valor.isdigit():
            self.__lado = valor
        else:
            print("O valor do lado deve ser apenas em numeros")

    def valorLado(self):
        print("\nO valor do lado é {} cm".format(self.__lado))

    def mudarLado(self):
        novoLado = input("\nMudar lado de {} cm para: ".format(self.__lado))
        self.lado = novoLado

    def calcArea(self):
        print("\nA área do quadrado é {:.2f} cm²".format(
            float(self.__lado) * float(self.__lado)))

    def __str__(self):
        return "O quadrado possui {} cm de lado e {:.2f} cm² de area".format(
            self.__lado, float(self.__lado) * float(self.__lado))


def main():
    quadradoA = Square()
    lado = input("Insira o valor do lado: ")
    quadradoA.lado = lado

    print(quadradoA)

    quadradoA.mudarLado()
    quadradoA.valorLado()
    quadradoA.calcArea()


main()
