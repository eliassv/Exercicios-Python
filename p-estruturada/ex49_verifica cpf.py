# erificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

def verificaCPF(numCPF):
    if numCPF[0:3].isdigit() and numCPF[4:7].isdigit() and \
            numCPF[8:11].isdigit() and numCPF[12:14].isdigit():
        if numCPF[3] == "." and numCPF[7] == "." and numCPF[11] == "-":
            print("O numero de CPF é VALIDO!")
            return True
        else:
            print("O numero de CPF não é válido!\n")
    else:
        print("O numero de CPF não é válido!\n")

valido = False

while not valido:
    CPF = input("Digite o numero de CPF \nno formato [xxx.xxx.xxx-xx]\n= ")

    valido = verificaCPF(CPF)