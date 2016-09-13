def alimentar(player):
    confirm = input("Deseja alimentar {}? (s/n)".format(player.nome))

    if confirm[0].lower() == "s":
        player.reduz_fome(30)

        print("{} foi alimentado!".format(player.nome))

    else:
        print("{} Não foi alimentado.".format(player.nome))


def medicar(player):
    confirm = input("Deseja dar remédio a {}? (s/n)".format(player.nome))

    if confirm[0].lower() == "s":
        player.aum_saude(30)

        print("{} melhorou a saúde!".format(player.nome))
    else:
        print("{} não foi medicado.".format(player.nome))


def desenha_tamagotchi():
    print("\n"*30)
    print("     /\___/\  ")
    print("    /       \ ")
    print("   /   ^.^   \ ")
    print("  /    ===    \  ")
    print(" | | |     | | |   ")
    print(" \_|_|-----|_|_/  ")
    print("=================\n")


def jogada(player):
    sair = False
    print("------------------")
    print("(1) Alimentar")
    print("(2) Dar remédio")
    print("(3) Sair")
    print("(Enter) Atualizar Status")
    selec = input("=== ")

    if selec == "1":
        alimentar(player)
    elif selec == "2":
        medicar(player)
    elif selec == "3":
        print("Saindo...")
        sair = True

    return player, sair
