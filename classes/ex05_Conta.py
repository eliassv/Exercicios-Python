# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
import random
import time

class bankAccount:
    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, numero):
        valido = False

        if numero[0:4].isdigit():
            if numero[4:5] == "-":
                if numero[5:6].isdigit():
                    valido = True
                    self.__conta = numero

        if valido == False:
            print("O numero da conta deve ser no formato [ XXXX-X ]")

    def alterarNome(self):
        verif = input("Nome atual {} \nDeseja mudar o nome? [S/N]"
                      .format(self.nome))
        verif = verif[0].upper()

        if verif == "S":
            novo_nome = input("Por favor insira o novo nome: ")
            self.nome = novo_nome
            print("Nome ALTERADO!")

        else:
            print("Alteração de nome CANCELADA.")

    def deposito(self):
        while True:
            try:
                print()
                print("Depósito na conta {}".format(self.conta))
                valor = float(input("Qual o valor do depósito: R$ "))

                if valor > 3000:
                    print("Não é possível realizar o depósito! "
                          "\nO valor máximo permitido é R$ 3000")
                    continue

                self.saldo += valor
                print("R$ {:.2f} depositado. \nNovo Saldo R$ {:.2f}".format(
                    valor, self.saldo))
                break

            except:
                print("Por favor insira um valor valido!")

    def saque(self):
        print()
        print("Conta {} \nSaldo disponível R$ {:.2f}".format(
            self.conta, self.saldo))
        while True:
            try:
                valor = float(input("Qual valor deseja sacar: R$ "))

                if valor > self.saldo:
                    print("Você não possui saldo disponível\n")
                    continue

                self.saldo -= valor
                print("\nSaque de R$ {:.2f} realizado! \nNovo Saldo R$ {:.2f}".format(
                    valor, self.saldo))

                break

            except:
                print("Por favor insira um valor valido!\n")

    def __str__(self):
        return "\n===== CONTA BANCÁRIA =====\
        \nCONTA: {} \nNOME: {} \nSALDO: R${:.2f}\
        \n==========================".format(self.conta, self.nome, self.saldo)


def menu():
    print("======== BEM VINDO AO BANCO ========")
    print("1 - Acessar conta")
    print("2 - Criar conta")
    print("3 - Sair")
    print("====================================")
    opc = input("Selecione uma opção: ")

    return opc

def menuConta(contas):
    print("Acessar conta ================")
    numero = input("Número da conta [ XXXX-X ]: ")

    acesso = False

    for n in contas:
        if numero == n.conta:
            acesso = True
            while True:
                print(n)
                print("1 - Saque")
                print("2 - Depósito")
                print("3 - Alterar Nome")
                print("4 - Sair")
                opc = input("Selecione a opção: ")

                if opc == "1":
                    cls(50)
                    n.saque()
                elif opc == "2":
                    cls(50)
                    n.deposito()
                elif opc == "3":
                    cls(50)
                    n.alterarNome()
                elif opc == "4":
                    print("Encerrando acesso...\n")
                    time.sleep(3)
                    cls(50)
                    break
                else:
                    print("\nSelecione uma opção válida!\n")

    if acesso == False:
        print("\nConta Inválida!\n")

    return contas

def criarConta(contas):
    print("======== Criar Conta ========")
    nome = input("NOME: ")
    numero = str(random.randrange(1000, 9999)) + "-" +\
        str(random.randrange(1, 9))
    print("Criando conta...\n")
    time.sleep(3)
    print("CONTA CRIADA!")

    Nconta = bankAccount(numero, nome)
    contas.append(Nconta)

    print(Nconta)
    sair = input("Pressione qualquer tecla para voltar ao menu principal.")
    cls(50)

    return contas


def cls(x):
    print("\n" * x)

def main():
    conta01 = bankAccount("1234-5", "Joao da Silva", 1250)
    contas = [conta01]

    cls(50)

    while True:
        print()
        opc = menu()

        if opc == "1":
            cls(50)
            contas = menuConta(contas)
        elif opc == "2":
            cls(50)
            contas = criarConta(contas)
        elif opc == "3":
            cls(50)
            print("Obrigado por utilizar \nEncerrando...")
            break
        else:
            print("\nSelecione uma opção válida!\n")


    for i in contas:
        print(i)

main()
