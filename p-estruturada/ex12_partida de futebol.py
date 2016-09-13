print("       Bangu x Madureira")
print("-------------------------------")
g1 = input("Quantos gols do Bangu? ")
g1 = int(g1)
g2 = input("Quantos gols do Madureira? ")
g2 = int(g2)
print("-------------------------------")

if (g1 > g2):
    dif = g1 - g2
else:
    dif = g2 - g1

print ("DIFERENCA: ", dif)

if (dif == 0):
    print ("Status: EMPATADO")
elif ((dif >= 1) and (dif <= 3)):
    print ("Status: PARTIDA NORMAL")
elif ((dif >= 4) and (dif <= 6)):
    print ("Status: GOLEADA")
else:
    print("Status: SERIO MESMO?")
print ("-------------------------------")
