tabuleiro = [[1]*3 for i in range(3)]
num = 1

for l in range(3):
    for c in range(3):
        tabuleiro[l][c] = num
        num += 1

def exibeTabuleiro():
    print("\n-------------")
    for l in range(3):
        print("| ", end="")
        for c in range(3):
            print(tabuleiro[l][c], end=" | ")

        print("\n-------------")

def jogada():
    jogadaValida = False

    while not jogadaValida:
        posicao = input("Deseja jogar {} em que posição? ".format(player))

        if not posicao.isdigit():
            print("Escolha um número!")
            continue

        for l in range(3):
            for c in range(3):

                if tabuleiro[l][c] == int(posicao):
                    tabuleiro[l][c] = player
                    jogadaValida = True

        if jogadaValida == False:
            print("\nEsta jogada NÃO é valida!")

def trocaPlayer():
    global player

    if player == "X":
        player = "O"
    else:
        player = "X"

def verificaJogo():
    # Verifica diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        trocaPlayer()
        print("Fim de JOGO\n O Jogador {} Ganhou!!!".format(player))
        return True

    if tabuleiro[2][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[0][2]:
        trocaPlayer()
        print("Fim de JOGO\n O Jogador {} Ganhou!!!".format(player))
        return True

    # Verifica linhas
    for l in range(3):
        if tabuleiro[l][0] == tabuleiro[l][1] and tabuleiro[l][1] == tabuleiro[l][2]:
            trocaPlayer()
            print("Fim de JOGO\n O Jogador {} Ganhou!!!".format(player))
            return True

    # Verifica colunas
    for c in range(3):
        if tabuleiro[0][c] == tabuleiro[1][c] and tabuleiro[1][c] == tabuleiro[2][c]:
            trocaPlayer()
            print("Fim de JOGO\n O Jogador {} Ganhou!!!".format(player))
            return True

    # Jogo em velha
    ocorr = 0
    for l in range(3):
        for c in range(3):
            if tabuleiro[l][c] != "X" and tabuleiro[l][c] != "O":
                ocorr += 1
    if ocorr == 0:
        print("Fim de Jogo\n Deu Velha")
        return True

def cls():
    print("\n"*30)


player = "X"
gameOver = False

while not gameOver:
    cls()
    exibeTabuleiro()
    jogada()
    trocaPlayer()
    print()
    gameOver = verificaJogo()
exibeTabuleiro()
