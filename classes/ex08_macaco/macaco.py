# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
# (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos,
# alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do
# estomago a cada refeição. Experimente fazer com que um macaco coma o outro.
# É possível criar um macaco canibal?

class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, objeto):
        self.bucho.append(objeto)

    def verBucho(self):
        print("Coisas no Bucho: ")
        for i in self.bucho:
            print(i)
        print("...")

    def digerir(self):
        print("Digerindo...")
        self.verBucho()
        self.bucho = []
