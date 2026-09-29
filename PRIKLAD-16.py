subor = open("mena_zamestnancov.txt", encoding="utf-8")

riadky = subor.readlines()

polovica = len(riadky)//2

mena = riadky[:polovica]
priezviska = riadky[polovica:]

print("Pocet mien:", len(mena))

naj_meno = 0
naj_priezvisko = 0

for meno in mena:
    meno = meno.strip()

    if len(meno)> naj_meno:
        naj_meno=len(meno)

for priezvisko in priezviska:
    priezvisko = priezvisko.strip()

    if len(priezvisko)>naj_priezvisko:
        naj_priezvisko = len(priezvisko)

print("Naj meno", naj_meno)
print("Naj priezvisko", naj_priezvisko)