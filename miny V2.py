import random
x = int(input("Zadej x: "))
y = int(input("Zadej y: "))
if x < 1 or y < 1:
    print("Nelze ")
    sys.exit()
for i in range(y):
    for j in range(x):
        print(("X"), end = " ")
    print("")

               