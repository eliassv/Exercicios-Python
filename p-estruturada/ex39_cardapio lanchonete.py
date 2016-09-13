# O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

# Define o cardápio

print("------------- Lanchonete --------------")
print("Especificação     Código    Preço")
print("---------------------------------------")

item = ["Cachorro Quente", "Bauru Simples", "Bauru com ovo", "Hambúrguer", "Cheeseburguer", "Refrigerante", "FINALIZAR PEDIDO"]
codigo = [100, 101, 102, 103, 104, 105, 0]
preco = [6.30, 4.60, 5.75, 9.25, 9.80, 3.75, 0]

# loop pelos itens, e da print na tela
for i in range(len(item)):
    print("{}   {}       R$ {:.2f}".format(item[i].ljust(15), codigo[i], preco[i]))
print("---------------------------------------")

pedido = []
qtdpedido = []
totalitem = []

# Pede os itens e quantidades e incrementa na lista de pedido
while True:
    selec = int(input("Informe o código do item desejado: "))
    if selec == 0: # Se selecionado 0 finaliza o pedido.
        print("- - - - - - - - - - - - - - - - - - ")
        print()
        break
    selecqtd = int(input("Quantidade: "))

    for i in range(len(item)): #loop pelos itens do cardapio
        if selec == codigo[i]: #se o codigo escolhido existir incrementa o pedido
            pedido.append(item[i])
            qtdpedido.append(selecqtd)
            totalitem.append(selecqtd * preco[i])
    print("- - - - - - - - - - - - - - - - - - ")

# Mostra a nota fiscal
print("------------ NOTA FISCAL --------------")
print("Especificação     Qtde    Preço")
print("---------------------------------------")
for i in range(len(pedido)): #loop pelo pedido, printando na tela o nome, qtde, e total
    print("{}   {}       R$ {:.2f}".format(pedido[i].ljust(15), qtdpedido[i], totalitem[i]))

#Soma o total, e informa o troco
totalapagar = 0
for i in range(len(pedido)):
    totalapagar += totalitem[i]

print()
print("TOTAL ------------------- R$ {:.2f}".format(totalapagar))
dinheiro = float(input("Dinheiro: R$ "))
print("TROCO: R$ {:.2f}".format(dinheiro - totalapagar))
