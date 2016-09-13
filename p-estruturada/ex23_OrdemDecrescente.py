#Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = input('digite o 1º numero: ')
n2 = input('digite o 2º numero: ')
n3 = input('digite o 3º numero: ')
aux = "0"

if (n1 < n2):
    aux = n1
    n1 = n2
    n2 = aux
if (n1 < n3):
    aux = n1
    n1 = n3
    n3 = aux
if (n2 < n3):
    aux = n2
    n2 = n3
    n3 = aux

print ('{}..{}..{}..'.format(n1, n2, n3))
