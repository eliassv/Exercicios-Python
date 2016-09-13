'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes)
e verifique se há excesso. Se houver, gravar na variável excesso e na variável
multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
variáveis com o conteúdo ZERO.
'''
peso = input('Digite o peso dos peixes: ')
peso = float(peso)
multa = 0
excesso = 0

if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4

print ('Valor da multa R${:.2f}'.format(multa))
