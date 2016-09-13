import random

def menu():
    print("MENU DE OPÇÕES")
    print("=====================")
    print("[1] Mostrar a Matriz")
    print("[2] Diagonal Principal")
    print("[3] Triangulo Superior")
    print("[4] Triangulo Inferior")
    print("[5] Sair")
    global opc
    opc = input("======== OPÇÃO: ")

def cls(x):
    print("\n" * x)

def mostraMatriz():
    for l in range(4):
        print("| ", end="")
        for c in range(4):
            print(matriz[l][c], end=" | ")
        print()

def diagPrincipal():
    for l in range(4):
        print("| ", end="")
        for c in range(4):
            if l == c:
                print(matriz[l][c], end=" | ")
            else:
                print("  ", end=" | ")
        print()

def trianguloSup():
    for l in range(4):
        print("| ", end="")
        for c in range(4):
            if l < c:
                print(matriz[l][c], end=" | ")
            else:
                print("  ", end=" | ")
        print()

def trianguloInf():
    for l in range(4):
        print("| ", end="")
        for c in range(4):
            if l > c:
                print(matriz[l][c], end=" | ")
            else:
                print("  ", end=" | ")
        print()


matriz = [[0]*4 for i in range(4)]
for l in range(4):
    for c in range(4):
        matriz[l][c] = random.randrange(11, 99)

cls(50)
while True:
    cls(3)
    opc = ""
    menu()

    if opc == "1":
        cls(30)
        mostraMatriz()
    elif opc == "2":
        cls(30)
        diagPrincipal()
    elif opc == "3":
        cls(30)
        trianguloSup()
    elif opc == "4":
        cls(30)
        trianguloInf()
    elif opc == "5":
        print("\nPROGRAMA FINALIZADO ==============================")
        break
    else:
        cls(30)
        print("\n Selecione uma opção válida!")
