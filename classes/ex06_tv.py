# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
import time

class televisor:
    def __init__(self, canal="1", volume="50"):
        self.canal = canal
        self.volume = volume

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num > 0 and num <= 150:
                self.__canal = num
            else:
                print("Canal Inválido")

        else:
            print("O canal deve ser apenas números!")

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 0 and num <= 100:
                self.__volume = num
            else:
                print("O volume deve ser entre 0 e 100")

        else:
            print("O volume deve ser apenas números!")


    def mudaCanal(self):
        num = input("Mudar para CANAL: ")
        self.canal = num

    def mudaVolume(self):
        num = input("Mudar para VOLUME: ")
        self.volume = num

    def __str__(self):
        return "CANAL: {} \nvolume: {}\n ".format(self.canal, self.volume)

def main():
    tv01 = televisor()

    while True:
        print("\n"*40)
        print(tv01)

        print("opções ---------")
        print("1 - mudar canal")
        print("2 - mudar volume")
        print("3 - desligar\n ---------------")
        selec = input("Selecionar:")

        if selec == "1":
            tv01.mudaCanal()

        elif selec == "2":
            tv01.mudaVolume()

        elif selec == "3":
            print("Desligando ...")
            break

        else:
            print("Selecione uma opção válida!")

        time.sleep(2)

main()
