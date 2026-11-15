def brojIgraca(listaKarata):
    return len(listaKarata)

def brojPreostalihKarata(listaKarata):
    zbir = 0
    for red in listaKarata:
        zbir = zbir + len(red)
    return zbir

listaKarata = []
# unos podataka
while (True):
    unosReda = input()
    if (unosReda == ""): break
    deljenje = unosReda.split(" ")
    for i in range(4): deljenje[i] = int(deljenje[i])
    listaKarata.append (deljenje)

# obrada podataka
"""
Igra se izvodi tako što svaki igrač izbacuje po jednu kartu iz svoje ruke i to redom kojim su igrači navedeni.
Igrač izabira da baci kartu istu kao onu koja je prva dodata na talon, ukoliko je ima u ruci. Ukoliko je nema u ruci, a ima kartu 7, onda nju baca na talon.
Ukoliko ni to nije slučaj, baca kartu sa najmanjom vrednošću na talon, što čini i prvi igrač koji započinje partiju (kada je talon prazan).
"""
talon = []
talonNemaKarti = True
while(brojPreostalihKarata(listaKarata) > 0):
    for i in range (brojIgraca(listaKarata)): # umesto da navodimo len fakticki matrice --> sprecavanje moguce konfuzije
        if(talonNemaKarti):
            prvaNaTalonu = min(listaKarata[i])
            talonNemaKarti = False
            talon.append(prvaNaTalonu)
            listaKarata[i].remove(prvaNaTalonu)

        elif(listaKarata[i].count(talon[0]) > 0):
            talon.append(talon[0])
            listaKarata[i].remove(talon[0])

        else:
            pomocniBroj = min(listaKarata[i])
            talon.append(pomocniBroj)
            listaKarata[i].remove(pomocniBroj)

# ispis (print(talon) daje i uglaste zagrade)
for i in range (len(talon)):
    if(i == len(talon) - 1): print(talon[i], end = "")
    else: print(talon[i], end = " ")