# Faça um Programa que leia três números e mostre o maior e o menor deles
n1 = input('digite o 1º numero: ')
n2 = input('digite o 2º numero: ')
n3 = input('digite o 3º numero: ')

if (n1 > n2) and (n1 > n3):
    print ('n1 é o maior')
elif (n2 > n1) and (n2 > n3):
    print ('n2 e o maior')
elif (n3 > n1) and (n3 > n2):
    print ('n3 e o maior')

if (n1 < n2) and (n1 < n3):
    print ('n1 é o menor')
elif (n2 < n1) and (n2 < n3):
    print ('n2 e o menor')
elif (n3 < n1) and (n3 < n2):
    print ('n3 e o menor')
