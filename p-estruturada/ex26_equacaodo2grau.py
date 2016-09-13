'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
nas seguintes situações:
    1. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
        e o programa não deve fazer pedir os demais valores, sendo encerrado;
    2. Se o delta calculado for negativo, a equação não possui raizes reais.
        Informe ao usuário e encerre o programa;
    3. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    4. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

from math import sqrt

print ('    Equação do 2 grau')
print ('    +- ax² +- bx +- c')
print ('---------------------------')
fim = 1

while (fim != 0):
# Solicitar os valores de a, b, c
# Verifica se A é igual a 0
    a = input('Informe o valor de a: ')
    if a == '0':
        print ('Não e uma equacao do 2 grau')
        break
    b = input('Informe o valor de b: ')
    c = input('Informe o valor de c: ')

# Converter os valores para numeros reais
    a = float(a)
    b = float(b)
    c = float(c)

    print ('')
# Calcular o valor de delta (Δ = b² -4 . a . c)
    delta = (b ** 2) - (4 * a * c)
    print ('O valor de delta e ', delta)
    
# Vefiricar se delta for negativo encerra o programa
    if (delta < 0):
        print ('O delta é negativo, a equação não possui raizes reais')
        break

#Calcular o valor de X = (-b +- raiz de delta) / 2 . a
# Verificar se delta for igual a zero, Calcular apenas uma raiz real
    elif (delta == 0):
        x = (-b + sqrt(delta)) / (2 * a)
        print ('O resultado é X= {}'.format(x))
        break

# Verificar se delta for positivo, calcular duas raizes reais
    elif (delta > 0):
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        if (x1 < x2):
            print ('O resultado é X= ({}, {})'.format(x1, x2))
        else:
            print ('O resultado é X= ({}, {})'.format(x2, x1))
        break
