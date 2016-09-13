# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário.

tabuada = int(input("Mostrar a tabuada de: "))
inicio = int(input("Inicio em : "))
fim = int(input("Fim em: "))

print()
print("Tabuada do {}, começando em {} e terminando em {}".format(tabuada, inicio, fim))

for i in range(inicio, fim+1):
    print("{} x {} = {}".format(tabuada, i, (tabuada * i)))


