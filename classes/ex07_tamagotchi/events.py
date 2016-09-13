def events(player, segundos):
    sair = False

    player.envelhecer(segundos)

    player.aum_fome(int(segundos / 2))

    player.reduz_saude(int(segundos))

    if player.saude < 1:
        print("\nSaúde 0")
        print("Seu tamagotchi morreu! :( \nGAME OVER!")
        sair = True

    if player.idade > 100:
        print("\nSeu tamagotchi morreu de velhice! :( \nGAME OVER!")
        sair = True

    return player, sair
