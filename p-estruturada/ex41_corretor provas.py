def cls(x):
    print("\n" * x)

def menu():
    cls(5)
    print("----------Corretor de provas----------")
    print("1 - Cadastro de Gabarito")
    print("2 - Cadastro de Respostas")
    print("3 - Exibir Respostas dadas")
    print("4 - Exibir Notas")
    print("0 - SAIR")
    op = input("Selecione a opção: ")
    print("--------------------------------------")

    if op == "1":
        cls(50)
        cadastGabar()
    elif op == "2":
        cls(50)
        cadastResp()
    elif op == "3":
        cls(50)
        respDadas()
    elif op == "4":
        cls(50)
        alunosNotas()
    elif op == "0":
        global sair
        sair = True
    else:
        print("Digite uma opção válida!")
        print()

def cadastGabar():
    print("--- Cadastrar Gabarito ---")
    for i in range(1, 11):  # Loop solicitando resposta das questões
        resp = input("Gabarito da Questão {}: ".format(i))
        gabarito.append(resp)  # adiciona resposta na lista gabarito

def cadastResp():
    print("--- Cadrastrar reposta ---")
    nome = input("NOME: ")
    nota = 0
    respostas = []  # cria lista
    for i in range(1, 11):  # Solicita respostas e acrescenta na lista
        resp = input("Resposta Questão {}: ".format(i))
        respostas.append(resp)

    for i in range(len(gabarito)):  # Soma a nota comparando com o gabarito
        if respostas[i] == gabarito[i]:
            nota += 10

    # atribui o nome, nota, e respostas dadas para as listas principais
    alunos.append({"nome": nome, "nota": nota})
    alunosresp.append(respostas)

def respDadas():
    for i in range(len(alunos)):  # loop pelos alunos cadastrados
        # exibe o dicinário de nome e nota
        print("ALUNO: {} - NOTA: {}".format(alunos[i]["nome"].ljust(15), alunos[i]["nota"]))

        # loop pelas respostas do aluno i
        print("Respostas : ", end="")
        for r in alunosresp[i]:
            print(r.upper(), end=" - ")
        print()

        # loop exibindo o gabarito
        print("Gabarito  : ", end="")
        for r in gabarito:
            print(r.upper(), end=" - ")
        print()

        print("Acertos   : ", end="")
        for r in range(len(gabarito)):  # loop pelas questões
            # verifica respostas do aluno i com gabarito, exibe as corretas
            if alunosresp[i][r] == gabarito[r]:
                print(r + 1, end=" - ")
            else:
                print(" ", end=" - ")
        print()
        print()

def alunosNotas():
    # exibe o dicinário de nome e nota
    for i in range(len(alunos)):
        print("ALUNO: {} - NOTA: {}".format(alunos[i]["nome"].ljust(15), alunos[i]["nota"]))

gabarito = []
alunos = []
alunosresp = []

while True:
    sair = False
    menu()

    if sair:
        break

print("====== PROGRAMA ENCERRADO =======")