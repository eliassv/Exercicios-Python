# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

interv = int(input("Digite o intervalo de números primos: "))

for a in range(interv):
    num = float(a)
    divis = 0

    for i in range(int(num)):
        if (num % float(i+1)) == 0:
            divis += 1

    if divis == 2:
        print("{}.. ".format(int(num)))