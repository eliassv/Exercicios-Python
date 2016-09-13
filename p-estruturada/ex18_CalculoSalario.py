'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
'''

valorHr = input("Qual o valor da hora: R$")
valorHr = float(valorHr)
horastrab = input("Quantas horas trabalhadas: ")
horastrab = float(horastrab)

salbruto = valorHr * horastrab
impRenda = (11 / 100) * salbruto
inss = (8/100) * salbruto
sindicato = (5/100) * salbruto
salliquido = salbruto - impRenda - inss - sindicato

print("")
print ("+ Salario bruto R${:.2f}".format(salbruto))
print ("- Imposto de renda R${:.2f}".format(impRenda))
print ("- Inss R${:.2f}".format(inss))
print ("- Sindicato R${:.2f}".format(sindicato))
print ("Salario liquido R${:.2f}".format(salliquido))
