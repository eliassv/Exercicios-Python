'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R
$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math
area = input("Area a ser pintada m² ")
area = float(area)
tinta = area / 6

latas = tinta / 18
latas = math.ceil(latas)
precolata = latas * 80.00

galao = tinta / 3.6
galao = math.ceil(galao)
precogalao = galao * 25.00

qtdlata = 0
qtdgalao = 0
while (tinta != 0):
    if (tinta > 18):
        tinta -= 18
        qtdlata += 1
    elif(tinta > 3.6):
        tinta -= 3.6
        qtdgalao += 1
    elif(tinta < 3.6):
        qtdgalao += 1
        break

print("1. {} latas de R$ 80 - total: R$ {:.2f}".format(latas, precolata))
print("2. {} galoes de R$ 25 - total: R$ {:.2f}".format(galao, precogalao))
print("3. {} latas R$80 e {} galoes R$25 - total R${:.2f}".format(qtdlata, qtdgalao, (qtdlata * 80)+(qtdgalao * 25)))
