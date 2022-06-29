trida_a = []
trida_b = []
trida = ["Kevin", "Honza", "Radek", "Tue", "Adéla", "Vojta"]
for x in range(len(trida)):
    zak = trida[x]
    
    if x % 2 == 0: 
        trida_a.append(zak)
    else:
        trida_b.append(zak)
    
print(", ".join(trida_a))
print("-".join(trida_b))

    