def prumer(pole):
    soucet = 0
    for prvek in pole:
        soucet += prvek
    prumer_pole = soucet/len(pole)
    return prumer_pole

vysky = [1.65,1.6,1.7,1.7]
prumer_vysky = prumer(vysky)
print("Průměr výšky je " + str(prumer_vysky))




vahy = [40,50,60,80]

