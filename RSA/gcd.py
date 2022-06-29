import random


def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)


def find_e(phi_n):
    while True:
        e = (2*random.randint(0,(phi_n/2))+1)
        if e < phi_n:
            break
    while True:
        if gcd(e, phi_n) == 1:
            return e  
        else:
            e += 2

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def find_d(e, phi_n):
    g, x, y = egcd(e, phi_n)
#    if g != 1:
#        raise Exception('modular inverse does not exist')
#    else:
    return x % phi_n


p1 = 103
p2 = 71
n = p1*p2
phi_n = (p1-1)*(p2-1)

e = find_e(phi_n)
print(e)

d = find_d(e,phi_n)
print(d)

verejny_klic = [n,e]
soukromy_klic = [n,d]

desifrovane_pole = []
sifrovane_pole = []
pole = []
pole[:] = input("Zadej slovo do RSA: ")

while True:
    vyber = int(input("Vyberte si: \n1. Zašifrovat zprávu\n2. Dešifrovat zprávu\n3. Konec\nVáš výběr je: "))
    if vyber == 3:
        print("konec")
        exit()
    if vyber == 1:
        print("Šifrovaná zpráva je: ", end = '')
        for i in range(len(pole)):
            sifrovane_pole.append(ord(pole[i])**verejny_klic[1] % verejny_klic[0])
            print(sifrovane_pole[i], end = ' | ')
        print("")
    if vyber == 2:
        print("Dešifrovaná zpráva je: ", end = '')
        for i in range(len(pole)):
            desifrovane_pole.append(sifrovane_pole[i]**soukromy_klic[1] % soukromy_klic[0])
            print(chr(desifrovane_pole[i]), end = '')
        print("")




#exponent = int(input("Zadej dešifrovací klíč: "))
#    if exponent != d:
#        print("Špatný klíč")
#        

        
    
