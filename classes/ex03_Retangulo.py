# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

class Retangulo:
    def __init__(self, comprimento="0", largura="0"):
        self.comprimento = comprimento
        self.largura = largura

    @property
    def comprimento(self):
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, valor):

        if valor.isdigit():
            self.__comprimento = valor
        else:
            print("Por favor insira apenas números.")

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, valor):

        if valor.isdigit():
            self.__largura = valor
        else:
            print("Por favor insira apenas números")

    def mudaValor(self):
        c = input("\nComprimento: ")
        self.comprimento = c

        l = input("Largura: ")
        self.largura = l

    def mostraValor(self):
        print("\n--- Retangulo ---")
        print("Comprimento: {} m".format(self.__comprimento))
        print("Largura: {} m".format(self.__largura))
        print("-----------------")

    def calcArea(self):
        print("A área é {} m²".format(
            float(self.__comprimento) * float(self.__largura)))

    def calcPerimetro(self):
        print("O perimetro é {} m".format(
            (float(self.__comprimento) * 2) + (float(self.__largura) * 2)
        ))

def main():
    objeto = Retangulo()
    objeto.mostraValor()

    objeto.mudaValor()
    objeto.mostraValor()

    objeto.calcArea()
    objeto.calcPerimetro()

main()
