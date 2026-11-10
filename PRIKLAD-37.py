subor = open("hlasovanie_1.txt")
riadky = subor.readlines()
subor.close()

print("Celkový počet zaslaných SMS:", len(riadky))

for cislo in range(5220, 5230):
    vystup = open(str(cislo) + ".txt", "w")
    poradie = 1
    for riadok in riadky:
        if riadok.strip() == str(cislo):
            vystup.write(str(poradie) + "\n")
        poradie += 1
    vystup.close()