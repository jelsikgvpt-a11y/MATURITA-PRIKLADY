veta = input("Zadaj mi vetu:")

pocet = [0]*10

for znak in veta:
    if znak == " ":
        cislo = 0 
        opakovanie = 1
        vysledok = "0"
    else:
        cislo = (ord(znak)-ord("A")) //3 +1
        opakovanie = (ord(znak)-ord("A")) %3 +1
        vysledok = str(cislo)*opakovanie

    print(vysledok, end = " ")
    pocet[cislo] = opakovanie
najviac = max(pocet)

print()
print("Najcastejsie policko:", end =" ")

for i in range (10):
    if pocet(i) == najviac:
        print(i,)
