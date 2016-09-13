'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''

print("---------- Eleições -----------")
candidato = ["José", "João", "Maria", "Paulo", "Voto nulo", "Voto em branco"]
codigo = [1, 2, 3, 4, 5, 6]
votos = [0, 0, 0, 0, 0, 0]
totvotos = 0

for i in range(len(candidato)):
    print("{} - {}".format(codigo[i], candidato[i]))
print("0 - Encerrar")
print("-------------------------------")

# voto
while True:
    escolha = int(input("Selecione o candidato: "))
    if escolha == 0:
        break
    for i in range(len(codigo)):
        if escolha == codigo[i]:
            votos[i] += 1
    print()

# printa o resultado
print("-------------------------------")
for i in range(len(candidato)):
    print("{} {}".format(candidato[i].ljust(15), votos[i]))
    totvotos += votos[i]
porc_nulos = (votos[4] / totvotos) * 100
porc_branco = (votos[5] / totvotos) * 100

print()
print("Votos nulos     {:.1f}%".format(porc_nulos))
print("Votos brancos   {:.1f}%".format(porc_branco))
