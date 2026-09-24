import random

# wuefel = random.randint(1,6)
# print (wuefel)

while True:
    liste = []
    wurf = int(input("Wie oft soll geworfen werden?"))
    for x in range(wurf):
        wuefel = random.randint(1, 6)
        liste.append(wuefel)
    print(liste)
# print("Sie haben liste[x] geworfen")
