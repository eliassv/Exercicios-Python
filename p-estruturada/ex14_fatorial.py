# Perguntar o numero do fatorial
# Atribuir 1 para o fatorial
# Repetir ate o numero ser menor que 1
# multiplicar o fatorial * numero
# reduzir um do numero

numero = input("Digite um numero: ")
N = numero
numero = int(numero)
fatorial = 1

print (numero, end='')
while (numero > 1):
    fatorial = fatorial * numero
    numero = numero - 1
    print ("x{}".format(numero), end='')

print()
print ("O valor do fatorial de {} e igual a {}".format(N, fatorial))
