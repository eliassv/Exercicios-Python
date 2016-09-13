nome = input("Insira o nome: ")
char = len(nome)

while char > 0:
    print(nome[0:char])
    char -= 1