'''Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

l1 = input('Digite o primeiro lado: ')
l1 = float(l1)
l2 = input('Digite o segundo lado: ')
l2 = float(l2)
l3 = input('Digite o terceiro lado: ')
l3 = float(l3)

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    if (l1 == l2) and (l2 == l3):
        print ('triangulo equilatero')
    elif (l1 != l2) and (l2 != l3) and (l1 != l3):
        print ('triangulo escaleno')
    else:
        print ('tiangulo Isósceles')
else:
    print ('nao pode formar um triangulo!')
