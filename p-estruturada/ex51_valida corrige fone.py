# Valida e corrige número de telefone. Faça um programa que leia um número de telefone,
# e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
# O usuário pode informar o número com ou sem o traço separador.

def verificaFone():
    num = 0

    for char in fone:
        if char.isdigit():
            num += 1

    if num == 8:
        print("O telefone está correto!")
        return True

    elif num == 7:
        corrigeFone()
        return True

    else:
        print("O telefone digitado não é valido!")
    print()

def corrigeFone():
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")

    global foneCorrigido

    for char in fone:
        if char.isdigit():
            foneCorrigido.append(char)

    print("Telefone corrigido sem formatação: ", end="")
    for char in foneCorrigido:
        print(char, end="")
    print()

    foneCorrigido.insert(4, ("-"))
    print("Telefone corrigido com formatação: ", end="")
    for char in foneCorrigido:
        print(char, end="")
    print()

foneCorreto = False

while not foneCorreto:
    fone = input("Valida e corrige número de telefone \nTelefone: ")
    fone = list(fone)
    foneCorrigido = [3]

    foneCorreto = verificaFone()