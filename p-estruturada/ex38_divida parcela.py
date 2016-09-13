'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida:
1       0
3       10
6       15
9       20
12      25'''

while True:
    print()
    try:
        divida = float(input("Informe o valor da divida: R$ "))
        qtdparcela = int(input("Quantas parcelas?: "))

        if qtdparcela == 1 or qtdparcela == 2:
            juros = 0
        elif qtdparcela >= 3 and qtdparcela < 6:
            juros = divida * (10 / 100)
        elif qtdparcela >= 6 and qtdparcela < 9:
            juros = divida * (15 / 100)
        elif qtdparcela >= 9 and qtdparcela < 12:
            juros = divida * (20 / 100)
        elif qtdparcela == 12:
            juros = divida * (25 / 100)
        else:
            print("Numero de parcelas não é valido!")
            continue

        break
    except:
        print("valor inválido tente novamente")
        continue
vparcela = (divida + juros) / qtdparcela

print()
print("Valor da divida R$ {:.2f}".format(divida + juros))
print("Juros R$ {:.2f}".format(juros))
print("Parcelas {}X".format(qtdparcela))
print("Valor da Parcela R$ {:.2f}".format(vparcela))