# Desenvolva um jogo da forca.
# O programa terá uma lista de palavras lidas de um arquivo texto
# e escolherá uma aleatoriamente.
#  O jogador poderá errar 6 vezes antes de ser enforcado.
import json
import random

palavras = []

with open("forcaPalavras.txt", encoding="utf-8") as dataFile:
    palavras = json.load(dataFile)

forca = palavras[random.randrange(len(palavras))]
forca = list(forca)
forcaOculta = []

for i in forca:
    forcaOculta += "_"

def exibeForca():
    print("A palavra é: ", end="")

    for i in forcaOculta:
        print(i, end=" ")
    print()

def jogada():
    letra = input("\nDigite uma letra: ")
    letra = letra[0].upper()

    acerto = False
    for i in range(len(forca)):
        if forca[i] == letra:
            forcaOculta[i] = forca[i]
            acerto = True

    if acerto == False:
        global tentativa
        print("Você errou na {}ª vez. Tente de novo!\n".format(tentativa))
        tentativa += 1

def verifGame():
    if tentativa == 6:
        print("Fim do jogo! Você PERDEU! \nA Palavra era: ", end="")
        for i in forca:
            print(i, end="")
        print()
        return True

    letrasIguais = 0
    for i in range(len(forca)):
        if forca[i] == forcaOculta[i]:
            letrasIguais += 1

    if letrasIguais == len(forca):
        print("Fim do jogo! Você GANHOU! \nA Palavra era: ", end="")
        for i in forca:
            print(i, end="")
        print()
        return True


gameOver = False
tentativa = 1

while not gameOver:
    exibeForca()
    jogada()

    gameOver = verifGame()