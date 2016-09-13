''' Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas
notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais,
        o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais,
        o programa fornece três notas de 100, uma nota de 50,
        quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

saque = int(input('Qual valor deseja sacar? R$ '))
nota100 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota1 = 0

def QtdNota(nota, QNota, saque):
    resto = saque % nota
    saque = saque - resto
    QNota = saque / nota
    saque = resto
    return (QNota, saque)

if saque >= 100:
    nota100, saque = QtdNota(100, nota100, saque)
if saque >= 50:
    nota50, saque = QtdNota(50, nota50, saque)
if saque >= 10:
    nota10, saque = QtdNota(10, nota10, saque)
if saque >= 5:
    nota5, saque = QtdNota(5, nota5, saque)
if saque >= 1:
    nota1, saque = QtdNota(1, nota1, saque)

print (int(nota100), ' notas de R$100')
print (int(nota50), ' notas de R$50')
print (int(nota10), ' notas de R$10')
print (int(nota5), ' notas de R$5')
print (int(nota1), ' notas de R$1')
