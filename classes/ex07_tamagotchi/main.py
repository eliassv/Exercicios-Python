import time
from tamagotchi import Tamagotchi
from gameplay import *
from events import *

def main():
    print("--------------------------")
    print("        TAMAGOTCHI")
    print("--------------------------")
    player = Tamagotchi("Tamagotchi", 90, 30)
    player.altera_nome()

    sair = False

    while not sair:
        tempo_inicio = time.time()

        desenha_tamagotchi()
        print(player)

        player, sair = jogada(player)

        tempo_fim = time.time()
        player, sair = events(player, (tempo_fim - tempo_inicio) )

main()
