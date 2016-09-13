print("------------------------------")
print("    Escola Javali Cansado")
print("------------------------------")
nota1 = input("Digite a primeira nota: ")
nota1 = int(nota1)
nota2 = input("Digite a segunda nota: ")
nota2 = int(nota2)
nota3 = input("Digite a terceira nota: ")
nota3 = int(nota3)
nota4 = input("Digite a quarta nota: ")
nota4 = int(nota4)
print("------------------------------")

media = (nota1 + nota2 + nota3 + nota4) / 4
print ("A media e: {}".format(media))

if ((media >= 90) and (media <= 100)):
    print ("Aproveitamento A")
elif ((media >= 80) and (media < 90)):
    print("Aproveitamento B")
elif ((media >= 60) and (media < 80)):
    print ("Aproveitamento C")
elif ((media >= 49) and (media < 60)):
    print ("Aproveitamento D")
elif ((media >= 40) and (media < 49)):
    print ("Aproveitamento E")
else:
    print ("Aproveitamento F")

if (media >= 60):
    print ('Aluno APROVADO')
else:
    print ('Aluno REPROVADO')

print("------------------------------")
