pole = []
pole[:] = input("Zadej něco: ")
print(pole)

for x in range(len(pole)):
    pole[x] = ord(pole[x]) #z písma na číslo

print(pole)
    
for x in range(len(pole)):
    pole[x] = chr(pole[x]) #z čísla na písmo
    
print(pole)


print("Ahoj", end = '') #end nedela novy radek
print("XX")
