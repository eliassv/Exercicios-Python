'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''

quest01 = input('Telefonou para a vitima? [s/n] ')
quest02 = input('Esteve no local do crime? [s/n] ')
quest03 = input('Mora perto da vítima? [s/n] ')
quest04 = input('Devia para a vítima? [s/n] ')
quest05 = input('Já trabalhou com a vítima? [s/n] ')
totquest = 0

if quest01 == 's':
    totquest += 1
if quest02 == 's':
    totquest += 1
if quest03 == 's':
    totquest += 1
if quest04 == 's':
    totquest += 1
if quest05 == 's':
    totquest += 1

print ('--------------------------------')

if totquest == 2:
    print ('Suspeito')
elif (totquest >= 3) and (totquest <= 4):
    print ('Cúmplice')
elif (totquest == 5):
    print ('Assassino')
else:
    print ('Inocente')
