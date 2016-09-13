# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome="pessoa", idade=0, peso=0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def crescer(self, cm):
        self.altura += cm / 100
        print("{} cresceu {} cm, e agora tem {:.3f} m de altura".format(
            self.nome, cm, self.altura))

    def engordar(self, kg):
        self.peso += kg
        print("{} engordou {} kg, e agora pesa {} kg".format(
            self.nome, kg, self.peso))

    def emagrecer(self, kg):
        self.peso -= kg
        print("{} emagreceu {} kg, e agora pesa {} kg".format(
            self.nome, kg, self.peso
        ))

    def envelhecer(self, anos):
        cresc = 0

        if self.idade + anos <= 21:
            cresc = anos * 0.5

        if self.idade < 21:
            if self.idade + anos > 21:
                cresc = ((21 - self.idade) * 0.5)

        self.idade += anos

        print("{} agora tem {} anos de idade.".format(self.nome, self.idade))
        self.crescer(cresc)

def main():
    joao = Pessoa("Joao", 12, 60, 1.68)

    print("Altura do {}: {}m ".format(joao.nome, joao.altura))
    C = int(input("Quanto deseja crescrer? (cm): "))
    joao.crescer(C)

    print()

    print("Peso do {}: {} kg".format(joao.nome, joao.peso))
    E = int(input("Quanto deseja engordar? (kg): "))
    joao.engordar(E)

    print()

    print("Peso do {}: {} kg".format(joao.nome, joao.peso))
    E = int(input("Quanto deseja emagrecer? (kg): "))
    joao.emagrecer(E)

    print()

    print("A idade do {}: {} anos".format(joao.nome, joao.idade))
    E = int(input("Quanto deseja envelhecer? (anos): "))
    joao.envelhecer(E)

main()
