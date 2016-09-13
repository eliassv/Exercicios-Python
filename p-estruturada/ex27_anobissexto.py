'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida
informe se este ano é ou não bissexto.

1. Os anos bissextos são múltiplos de 4
2. Não múltiplos de 100 (1900 não é bissexto)
3. Múltiplos de 400 (2000 é bissexto)..'''

ano = int(input('Digite o ano: '))

if ano % 400 == 0:
    print ('Ano bissexto!')
elif ano % 4 == 0:
    if ano % 100 != 0:
        print ('Ano bissexto!')
    else:
        print ('Não é ano bissexto')
else:
    print ('Não é ano bissexto')
