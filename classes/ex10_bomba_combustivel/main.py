from classe_bomba import *
import time

def main():
    bomba1 = bombaCombustivel()
    executar = True

    while executar:
        cls(50)
        executar = menu(bomba1)
        time.sleep(3)


def cls(x):
    print("\n" * x)


def menu(bomba):
    print("--------------------------------------")
    print("           POSTO IPIRANGA")
    print("--------------------------------------")
    print("1 - Escolher tipo combustível")
    print("2 - Abastecer por valor")
    print("3 - Abastecer por litros")
    print("4 - Alterar preços")
    print("5 - Preencher tanque das bombas")
    print("6 - Sair")
    print("-------------------------------------")
    print("Combustível Selecionado: {} \n".format(bomba.tipo_combustivel))
    op = input("Selecionar opção: ")

    if op == "1":
        bomba.alterar_combustivel()

    elif op == "2":
        bomba.abastercer_valor()

    elif op == "3":
        bomba.abastecer_litros()

    elif op == "4":
        bomba.alterar_valor()

    elif op == "5":
        bombaCombustivel.alterar_qtd_combustivel()

    elif op == "6":
        print("Saindo...")
        return False

    else:
        print("Selecione uma opção válida.")

    return True

main()
