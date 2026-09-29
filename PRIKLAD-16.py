subor = open("mena_zamestnancov.txt", encoding="utf-8")

riadky = subor.readlines()

polovica = len(riadky) // 2

mena = riadky[:polovica]
priezviska = riadky[polovica:]

print("Počet mien:", len(mena))

najdlhsie_meno = 0
najdlhsie_priezvisko = 0

for meno in mena:
    meno = meno.strip()

    if len(meno) > najdlhsie_meno:
        najdlhsie_meno = len(meno)

for priezvisko in priezviska:
    priezvisko = priezvisko.strip()

    if len(priezvisko) > najdlhsie_priezvisko:
        najdlhsie_priezvisko = len(priezvisko)

print("Dĺžka najdlhšieho mena:", najdlhsie_meno)
print("Dĺžka najdlhšieho priezviska:", najdlhsie_priezvisko)

subor.close()