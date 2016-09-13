'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço
do litro do álcool é R$ 1,90.'''

# pedir o tipo de combustivel
print ('Qual o combustivel desejado?')
combust = input('A-álcool, G-gasolina: ')

# pedir a quantidade de litros
litros = float(input('Quantos litros: '))

# verificar se for alcool, calcular o preço e desconto até 20 litos, e acima de 20 litros
if (combust == 'A'):
    tipo = 'Alcool'
    preco = litros * 1.90
    if (litros <= 20):
        desconto = preco * (3/100)
    elif (litros > 20):
        desconto = preco * (5/100)
    total = preco - desconto

# verificar se for gasolina, calcular o preço e desconto até 20 litos, e acima de 20 litros
elif (combust == 'G'):
    tipo = 'Gasolina'
    preco = litros * 2.50
    if (litros <= 20):
        desconto = preco * (3/100)
    elif (litros > 20):
        desconto = preco * (5/100)
    total = preco - desconto
else:
    print ('#O tipo de combustivel selecionado não é valido!')

# informar o valor a ser pago
print ('-----------------------------------')
print ('Combustível tipo : {}'.format(tipo))
print ('Preço: {} - {} de Desconto'.format(preco, desconto))
print ('Total a ser pago: {}'.format(total))
