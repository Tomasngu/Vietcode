import statistics

soucet = 0
znamky = []
while True:
    znamka = input("Zadejte známku: ")
    if znamka == "stop":
        break
    soucet += int(znamka)
    if int(znamka) > 5 or int(znamka) < 0:
        print("Neplatná známka")
        continue
    znamky.append(int(znamka))
print("Průměr: " +  str(statistics.mean(znamky)))
        