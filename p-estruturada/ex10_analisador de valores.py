soma = 0
spares = 0
div5 = 0
nulo = 0

for i in range(1,6):
    v = input("Digite o {}º valor: ".format(str(i)))
    v = int(v)
    soma = soma + v

    if ((v % 5) == 0):
        div5 += 1
    if (v == 0):
        nulo += 1
    if ((v % 2) == 0):
        spares = spares + v

media = soma / 5
print()
print("A soma entre os valore e ", soma)
print("A media entre os valores e ", media)
print("Valores divisiveis por 5 ", div5)
print("Valores nulos ", nulo)
print("A soma dos valores pares e ", spares)
