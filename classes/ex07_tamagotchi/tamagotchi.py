# Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração,
# o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação
# por que ela pode ser calculada a qualquer momento.

class Tamagotchi:
    def __init__(self, nome="Tamagotchi", fome=0, saude=100, idade=1):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    # Getter and Setter Fome
    @property
    def fome(self):
        return self.__fome

    @fome.setter
    def fome(self, valor):
        if valor < 0:
            self.__fome = 0

        elif valor > 100:
            self.__fome = 100

        else:
            self.__fome = valor

    # Getter and Setter Idade
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):

        if valor > 100:
            print("Maior que 5 segundos")
            self.__idade = valor
        else:
            self.__idade = valor

    # Método Nome
    def altera_nome(self):
        self.nome = input("Qual nome deseja colocar no seu Tamagotchi? ")

    # Métodos Fome
    def reduz_fome(self, valor):
        self.fome -= valor

    def aum_fome(self, valor):
        self.fome += valor

    # Métodos Saúde
    def reduz_saude(self, valor):
        self.saude -= valor

    def aum_saude(self, valor):
        self.saude += valor

    # Metódo altera idade
    def envelhecer(self, segundos):
        # Valor pelo qual segundos são divididos definem duração de um ano de idade
        self.idade += int(segundos / 6)

    def humor(self):
        humor = (50 - (self.fome * .5)) + (self.saude * .5)

        return humor

    def __str__(self):
        return "-----Status----- \nNome:  {}  \nFome:  {} \nSaúde: {} \nIdade: {} \n \nHumor: {}".format(
        self.nome, self.fome, self.saude, self.idade, self.humor())
