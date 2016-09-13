'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area = input("Informe a área a ser pintada m²: ")
area = float(area)

tinta = area / 3
latas = tinta / 18
latas = round(latas)
custo = float(latas) * 80.00
custo = float(custo)

print("")
print("Serão necessários {} latas de tinta de R$ 80,00".format(latas))
print("Preço total R$ {:.2f}".format(custo))
