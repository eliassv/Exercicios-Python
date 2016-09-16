from classes import *

def main():
    ret = criar_retangulo()
    executar = True

    while executar:
        print("\n"*50)
        print(ret)

        print("1 - Criar Retângulo")
        print("2 - Ver centro")
        print("3 - Sair")
        op = input("Selcione uma opção = ")
        print()

        if op == "1":
            ret = criar_retangulo()

        elif op == "2":
            ret.centro_retangulo()
            cont = input("Pressione qualquer tecla para continuar...")

        elif op == "3":
            executar = False

def criar_retangulo():
    print("------ Criar Retangulo ------")

    inicio = Ponto(0, 0)
    ret = Retangulo(5, 5, inicio)
    # Define medidas do Retangulo
    largura = float(input("Largura: "))
    altura = float(input("Altura: "))

    ret.largura = largura
    ret.altura = altura

    # Define ponto de inicio
    x = float(input("Eixo X: "))
    y = float(input("Eixo Y: "))

    inicio = Ponto(x, y)
    ret.ponto_inicio = inicio

    return ret

main()
