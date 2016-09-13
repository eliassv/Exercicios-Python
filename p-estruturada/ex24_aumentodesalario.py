'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salarioatual = input('Informe o salario atual: R$')
salarioatual = float(salarioatual)
percentual = 0
novosalario = 0

if (salarioatual <= 280):
    novosalario = salarioatual * (20/100 + 1)
    percentual = 20
elif (salarioatual > 280) and (salarioatual <= 700):
    novosalario = salarioatual * (15/100 + 1)
    percentual = 15
elif (salarioatual > 700) and (salarioatual <= 1500):
    novosalario = salarioatual * (10/100 + 1)
    percentual = 10
elif (salarioatual > 1500):
    novosalario = salarioatual * (5/100 + 1)
    percentual = 5
print()
print ('Salario antes do reajuste R$ {:.2f}'.format(salarioatual))
print ('Percentual aplicado: {}%'.format(percentual))
print ('Aumento de R$ {:.2f}'.format(novosalario - salarioatual))
print ('O novo salário e R$ {:.2f}'.format(novosalario))
