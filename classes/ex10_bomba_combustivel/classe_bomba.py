'''Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel

    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
        quantidade de litros que foi colocada no veículo

        abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível
        e mostra o valor a ser pago pelo cliente.

        alterarValor( ) – altera o valor do litro do combustível.

        alterarCombustivel( ) – altera o tipo do combustível.

        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

        OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
        combustível total na bomba. '''

class bombaCombustivel:
    tanque = {"GASOLINA": 45, "ALCOOL": 125.5, "DIESEL": 205}
    preco = {"GASOLINA": 3.24, "ALCOOL": 2.37, "DIESEL": 2.58}

    def __init__(self, tipo_combustivel="G"):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = 0

    ### Define o tipo e preço do combústivel ###
    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo):
        tipo = tipo[0].upper()

        if tipo == "G":
            print("Tipo GASOLINA Selecionado")
            self.__tipo_combustivel = "GASOLINA"
            self.valor_litro = bombaCombustivel.preco["GASOLINA"]

        elif tipo == "A" or tipo == "Á":
            print("Tipo ALCOOL Selecionado")
            self.__tipo_combustivel = "ALCOOL"
            self.valor_litro = bombaCombustivel.preco["ALCOOL"]

        elif tipo == "D":
            print("Tipo DIESEL Selecionado")
            self.__tipo_combustivel = "DIESEL"
            self.valor_litro = bombaCombustivel.preco["DIESEL"]

        else:
            print("O tipo selecionado não é válido")

    ### Inicio dos métodos ###
    def alterar_combustivel(self):
        print("\nCombustível --------------------------")
        print("G - Gasolina: R$ {}".format(bombaCombustivel.preco["GASOLINA"]))
        print("A - Álcool: R$ {}".format(bombaCombustivel.preco["ALCOOL"]))
        print("D - Diesel: R$ {}".format(bombaCombustivel.preco["DIESEL"]))
        tipo = input("Selecione o tipo desejado: ")
        self.tipo_combustivel = tipo

    def abastercer_valor(self):
        if self.valor_litro == 0:
            print("Selecione um tipo de combustível válido")

        else:
            valor = float(input("\nAbastecer Valor: R$: "))
            litros = valor / self.valor_litro

            if bombaCombustivel.qtd_disponivel(self, litros):
                print("Abastecido {:.2f} litros de {}".format(litros, self.tipo_combustivel))

            else:
                print("Não há combustível dispónivel")

    def abastecer_litros(self):
        if self.valor_litro == 0:
            print("Selecione um tipo de combustível válido")

        else:
            litros = float(input("\nAbastecer Litros: "))

            if bombaCombustivel.qtd_disponivel(self, litros):
                print("{:.2f} litros de {} - Total R$ {:.2f}".format(litros,
                        self.tipo_combustivel, (litros * self.valor_litro)))

                dinheiro = float(input("Dinheiro: R$ "))
                print("Troco: R$ {:.2f} \n".format(dinheiro - (litros * self.valor_litro)))

                print("Abastecido {:.2f} litros de {}".format(litros, self.tipo_combustivel))

            else:
                print("Não há combustível dispónivel")

    def alterar_valor(self):
        print("\n\n---------------------------------------")
        print("Alterar precos combustível")
        print("---------------------------------------")
        self.alterar_combustivel()

        novo_valor = float(input("Novo valor: R$ "))
        bombaCombustivel.preco[self.tipo_combustivel] = novo_valor

        print("{} valor alterado para R$ {}".format(
            self.tipo_combustivel, bombaCombustivel.preco[self.tipo_combustivel]))

    @staticmethod
    def alterar_qtd_combustivel():
        print("\nTanque de combustível -----------------")
        print("Gasolina: {:.2f} litros".format(bombaCombustivel.tanque["GASOLINA"]))
        print("Álcool: {:.2f} litros".format(bombaCombustivel.tanque["ALCOOL"]))
        print("Diesel: {:.2f} litros".format(bombaCombustivel.tanque["DIESEL"]))
        preencher = input("Preencher o Tanque? (s/n)")
        if preencher[0].lower() == "s":
            bombaCombustivel.tanque = {"GASOLINA": 300, "ALCOOL": 300, "DIESEL": 300}

    @staticmethod
    def qtd_disponivel(self, litros):
        # Verifica se possui combústivel do tipo selecionado dispónivel
        if litros <= bombaCombustivel.tanque[self.tipo_combustivel]:
            bombaCombustivel.tanque[self.tipo_combustivel] -= litros
            return True

        else:
            return False
