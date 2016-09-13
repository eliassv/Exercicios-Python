# Nome na vertical.
# Faça um programa que solicite o nome do usuário
# e imprima-o na vertical.

nome = input("Insira o nome: ")

for char in range(len(nome)):
    print(nome[char])