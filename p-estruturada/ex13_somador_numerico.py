valor = input("Digite o valor: ")
valor = int(valor)
menor = valor
soma = 0
soma = soma + valor
cont = "s"

while (cont != "n"):
    valor = input("Digite o valor: ")
    valor = int(valor)
    if (valor < menor):
        menor = valor
    soma = soma + valor

    cont = input("outro? [s/n]")

print ("A soma de todos os valores foi {}".format(soma))
print ("O menor valor digitado foi {}".format(menor))
