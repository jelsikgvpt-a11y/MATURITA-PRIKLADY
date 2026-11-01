subor = open("hlasovanie_1.txt", "r")
hlasy = subor.readlines()
subor.close()

vypadnuti = open("hlasovanie_vypadnuty.txt", "r")
vypadnuti = vypadnuti.readlines()

print("Pocet SMS:", len(hlasy))

for i in range(5220, 5230):
    print(i, ":", hlasy.count(str(i) + "\n"))

minimum = 100000
for i in range(5220, 5230):
    pocet = hlasy.count(str(i) + "\n")

    if pocet < minimum:
        minimum = pocet
        najmenej = i

print("Najmenej hlasov:", najmenej)

minimum = 100000
for i in range(5220, 5230):
    if str(i) + "\n" not in vypadnuti:
        pocet = hlasy.count(str(i) + "\n")

        if pocet < minimum:
            minimum = pocet
            najmenej = i

print("Najmenej hlasov bez vypadnutych:", najmenej)