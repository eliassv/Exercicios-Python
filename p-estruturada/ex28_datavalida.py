'''Faça um Programa que peça uma data no formato dd/mm/aaaa
e determine se a mesma é uma data válida.'''
data = 'inválida'

while (data != '000'):
    print ('A data é ', data.upper())
#pede a data
    print ('----------------------------------------')
    dia, mes, ano = input('Insira a data: (dd/mm/aaaa) ').split('/')
#converter para inteiros
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

# verifica se e ano bissexto
    if ano % 400 == 0:
        bissexto = 'S'
    elif ano % 4 == 0:
        if ano % 100 != 0:
            bissexto = 'S'
        else:
            bissexto = 'N'
    else:
        bissexto = 'N'

# verifica se o ano está entre 1900 e 2050
    if (ano >= 1900) and (ano <= 2050):
        data = 'válida'
    else:
        data = 'inválida'
        continue

# verifica se o mes está entre 1 e 12
    if (mes < 1) or (mes > 12):
        data = 'inválida'
        continue

# verifica se o mês tem 31 dias (meses 1, 3, 5, 7, 8, 10 e 12)
    if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
        if (dia >= 1) and (dia <= 31):
            data = 'válida'
            break
        else:
            data = 'inválida'
            continue
# verifica se o mês é fevereiro, se for ano bissexto 29 dias senão 28.
    elif (mes == 2):
        if (bissexto == 'S'):
            if (dia >= 1) and (dia <= 29):
                data = 'válida'
                break
            else:
                data = 'inválida'
                continue
        if (bissexto == 'N'):
            if (dia >= 1) and (dia <= 28):
                data = 'válida'
                break
            else:
                data = 'inválida'
                continue
# se for outros meses entre 1 e 30 dias
    else:
        if (dia >= 1) and (dia <= 30):
            data = 'válida'
            break
        else:
            data = 'inválida'
            continue
print ('A data é ', data.upper())
