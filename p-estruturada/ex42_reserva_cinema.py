def main():
    print("\n===== BEM VINDO AO CINEMA =====")
    for i in cadeirasDisp:
        print("{}".format(i), end=" | ")

    selec = input("\nSelecione a cadeira: ")
    selec = selec.upper()
    print()

    reserva(selec)


def reserva(selec):
    for i in range(10):
        # verifica se seleção é igual a cadeira
        if selec == cadeiras[i]:

            if disponib(cadeiras[i]):  # verifica a disponibilidade da cadeira
                print("Cadeira {} Reservada!".format(cadeiras[i]))
                cadeirasDisp[i] = ".."
                askSair()
            else:
                print("Esta cadeira não está disponível")


def disponib(cadeira):
    # loop pelas cadeiras disponiveis
    for i in cadeirasDisp:
        # verifica se a cadeira selecionada está disponível
        if cadeira == i:
            return True
    return False


def askSair():
    print()
    perg = input("Deseja selecionar outra? [s/n]")
    global continuar
    if perg == "n":
        continuar = False


# INICIO
cadeiras = []
cadeirasDisp = []

# Atribui nome as cadeiras
for i in range(1, 11):
    cadeiras.append("B" + str(i))
    cadeirasDisp.append("B" + str(i))

continuar = True

while continuar:
    main()
