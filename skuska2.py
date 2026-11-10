subor = open("hlasovanie_1.txt", "r")
hlasy = subor.readlines()
subor.close()

print("Pocet sms: ", len(hlasy))

minimum = 100000
for i in range(5220,5230):
    pocet = hlasy.count(str(i) + "\n")
    print(i, ":",pocet)

    if pocet < minimum:
        minimum = pocet
        najmenej = i

