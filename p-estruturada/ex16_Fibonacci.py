# Programa para mostrar sequencia de fibonacci de 1 a 10
# Iniciando com 0 e 1, acrescenta o próximo número sendo a soma dos anteriores

n1 = 0
n2 = 1
c = 0

for i in range(10):
    c = n1 + n2
    n1 = n2
    n2 = c
    print ("{}...".format(c))
