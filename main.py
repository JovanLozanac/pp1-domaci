import math
import os
def stepURad (step):
    return (step * 3.14) / 180

def haversine (x1, y1, x2, y2):
    t1 = (math.sin((stepURad(x1) - stepURad(x2)) / 2)) ** 2
    t2 = (math.sin((stepURad(y1) - stepURad(y2)) / 2)) ** 2
    return 2 * 6371.0 * math.asin (math.sqrt(t1 + t2 * math.cos(stepURad(x1)) * math.cos(stepURad(x2))))

def indeksNajmanjeRazdaljine (x1, y1, lista):
    najmanja = haversine (x1, y1, float(lista[0].split("!")[2]), float(lista[0].split("!")[3]))
    broj = 0
    for j in range (1,len(lista)):
        probna = haversine(x1, y1, float(lista[j].split("!")[2]), float(lista[j].split("!")[3]))
        if(probna <= najmanja):
            broj = j
            najmanja = probna
    return broj

def obrada(pocetnaGS, krajnjaGS, pocetnaGD, krajnjaGD, stanica, izlazna):
    if (not os.path.exists(stanica + "_dirA.txt")):
        """radi samo B"""
        ispisSamo(pocetnaGS, krajnjaGS, pocetnaGD, krajnjaGD, stanica, "B", izlazna)

    elif (not os.path.exists(stanica + "_dirB.txt")):
        """radi samo A"""
        ispisSamo(pocetnaGS, krajnjaGS, pocetnaGD, krajnjaGD, stanica, "A", izlazna)
    else:
        """nadji obe, pa koja je bliza, nju ispisi"""
        citanjeA = open(stanica + "_dirA.txt", "r")
        spisakStanicaA = citanjeA.readlines()
        citanjeA.close()

        citanjeB = open(stanica + "_dirB.txt", "r")
        spisakStanicaB = citanjeB.readlines()
        citanjeB.close()

        najblizaKrajnjojA = indeksNajmanjeRazdaljine(krajnjaGS, krajnjaGD, spisakStanicaA)
        najblizaKrajnjojB = indeksNajmanjeRazdaljine(krajnjaGS, krajnjaGD, spisakStanicaB)
        najblizaPocetnojA = indeksNajmanjeRazdaljine(pocetnaGS, pocetnaGD, spisakStanicaA)
        najblizaPocetnojB = indeksNajmanjeRazdaljine(pocetnaGS, pocetnaGD, spisakStanicaB)

        if (najblizaKrajnjojB < najblizaPocetnojB):
            ispis = open(izlazna, "a")
            ispis.write(stanica + "!A" + "\n")

            for i in range(najblizaPocetnojA, najblizaKrajnjojA + 1):
                jednaStanica = spisakStanicaA[i].split("!")
                jednaStanica[2] = str(round(float(jednaStanica[2]), 6))
                jednaStanica[3] = str(round(float(jednaStanica[3]), 6))
                while (len(jednaStanica[2].split(".")[1]) != 6): jednaStanica[2] += '0'
                while (len(jednaStanica[3].split(".")[1]) != 6): jednaStanica[3] += '0'
                ispis.write('!'.join(jednaStanica))
            ispis.close()

        else:
            ispis = open(izlazna, "a")
            ispis.write(stanica + "!B" + "\n")

            for i in range(najblizaPocetnojB, najblizaKrajnjojB + 1):
                jednaStanica = spisakStanicaB[i].split("!")
                jednaStanica[2] = str(round(float(jednaStanica[2]), 6))
                jednaStanica[3] = str(round(float(jednaStanica[3]), 6))
                while (len(jednaStanica[2].split(".")[1]) != 6): jednaStanica[2] += '0'
                while (len(jednaStanica[3].split(".")[1]) != 6): jednaStanica[3] += '0'
                ispis.write('!'.join(jednaStanica))
            ispis.close()
def ispisSamo (pocetnaGS, krajnjaGS, pocetnaGD, krajnjaGD, stanica, smer, izlazna):
    citanje = open(stanica + "_dir" + smer + ".txt", "r")
    spisakStanica = citanje.readlines()
    citanje.close()

    najblizaPocetnoj = indeksNajmanjeRazdaljine(pocetnaGS, pocetnaGD, spisakStanica)
    najblizaKrajnjoj = indeksNajmanjeRazdaljine(krajnjaGS, krajnjaGD, spisakStanica)

    ispis = open(izlazna, "a")
    ispis.write(stanica + "!" + smer + "\n")
    for i in range(najblizaPocetnoj, najblizaKrajnjoj + 1):
        jednaStanica = spisakStanica[i].split("!")
        jednaStanica[2] = str(round(float(jednaStanica[2]), 6))
        jednaStanica[3] = str(round(float(jednaStanica[3]), 6))
        while (len(jednaStanica[2].split(".")[1]) != 6): jednaStanica[2] += '0'
        while (len(jednaStanica[3].split(".")[1]) != 6): jednaStanica[3] += '0'
        ispis.write('!'.join(jednaStanica))

    ispis.close()

try:
    izlazna = input()

    red = input().split()
    pocetnaGS = float(red[0])
    pocetnaGD = float(red[1])
    krajnjaGS = float(red[2])
    krajnjaGD = float(red[3])

    stanice = input().split()
    for stanica in stanice:
        obrada(pocetnaGS, krajnjaGS, pocetnaGD, krajnjaGD, stanica, izlazna)

except FileNotFoundError:
    print ("DAT_GRESKA", end="")
except ValueError:
    print ("PODACI_GRESKA", end="")