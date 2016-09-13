# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = float(input("Digite um número: "))
c = int(num)
divis = 0

for i in range(c):
    if (num % float(i+1)) == 0:
        divis += 1

if divis == 2:
    print("O numero {} É primo.".format(num))
else:
    print("O numero {} NÃO é primo.".format(num))