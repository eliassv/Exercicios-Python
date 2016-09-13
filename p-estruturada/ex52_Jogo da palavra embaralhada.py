import random

listaPalavras = []

with open("listaPalavras.txt", encoding="utf-8") as listaFile:
    while True:
        line = listaFile.readline()
        line = line.upper()

        if not line:
            break

        listaPalavras.append(line)

palavra = listaPalavras[random.randrange(len(listaPalavras))]
palavra = list(palavra)
palavra.pop(len(palavra)-1)

palavraOriginal = ""
for char in palavra:
    palavraOriginal += char

def embaralha(palavra):
    i = 0

    while i+1 < len(palavra):

        if i+1 > len(palavra):
            break

        temp = palavra[i]
        palavra[i] = palavra[i+1]
        palavra[i+1] = temp

        i += 1

    return palavra

def exibePalavra():
    print("Adivinhe a Palavra...")
    for char in palavra:
        print(char, end="")
    print()

def verifGame(jogada):
    jogada = jogada.upper()

    if jogada == palavraOriginal:
        print("Parabéns você Ganhou")
        return True

    elif tentativa > 2:
        print("Você perdeu a palavra correta é")
        print(palavraOriginal)
        return True
    else:
        print("Você errou a {}ª tentativa\n".format(tentativa))

gameOver = False
tentativa = 1

while not gameOver:
    palavra = embaralha(palavra)

    exibePalavra()
    jogada = input("\nA palavra original é: ")

    gameOver = verifGame(jogada)
    tentativa += 1
