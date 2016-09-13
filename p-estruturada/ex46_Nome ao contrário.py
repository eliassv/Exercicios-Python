# Nome ao contrário em maiúsculas.
# Faça um programa que permita ao usuário digitar o seu nome e
# em seguida mostre o nome do usuário de trás para frente utilizando
# somente letras maiúsculas.

nome = input("Insira o nome: ")
nome = nome.upper()
char = len(nome)

while char > 0:
    print(nome[char-1], end=" ")
    char -= 1