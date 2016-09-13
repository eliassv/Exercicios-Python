'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

num = input('Digite um numero menor que 1000: ')
qtnum = len(num)

if (qtnum == 3):
    centena = num[0:1]
    dezena = num[1:2]
    unidade = num[2:3]
    print ('{} = {} centenas, {} dezenas e {} unidades'.format(num, centena, dezena, unidade))

if (qtnum == 2):
    dezena = num[0:1]
    unidade = num [1:2]
    print ('{} = {} dezenas e {} unidades'.format(num, dezena, unidade))

if (qtnum == 1):
    unidade = num[0:1]
    print ('{} = {} unidades'.format(num, unidade))
