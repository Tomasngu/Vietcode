import random


def gcd(a, b): #největší společný dělitel
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

def find_d(e,phi_n): # nalezení multiplilkativního inverzního prvku e 
    i = 1
    while True:
        if i*e % phi_n == 1:
            return i
            break
        i += 1

p1 = 103   #vybereme si 2 náhodný prvočísla
p2 = 71
n = p1*p2 #součin prvočísel 
phi_n = (p1-1)*(p2-1) #hodnota eulerovy funkce

e = find_e(phi_n)
print("Kamarádův klíč:",e)

d = find_d(e,phi_n)
print("Náš klíč:",d)

verejny_klic = n
kamaraduv_klic= e
nas_klic = d

desifrovane_pole = []
sifrovane_pole = []
pole = [] #uložení rozdělených písmenek ['a','h','o','j']
pole[:] = input("Zadej slovo do RSA: ")  #rozdělení slova na písmenka do pole např ahoj na ['a','h','o','j']


while True:
    vyber = int(input("Vyberte si: \n1. Zašifrovat zprávu\n2. Dešifrovat zprávu\n3. Konec\nVáš výběr je: "))
    if vyber == 3:
        print("konec")
        exit()
    if vyber == 1:
        print("Šifrovaná zpráva je: ", end = '')
        for i in range(len(pole)):              
            sifrovane_pole.append(ord(pole[i])**kamaraduv_klic % verejny_klic) #zašifruje se to kamarádovým klíčem, ord převadí znaky na čísla
            print(sifrovane_pole[i], end = ' | ') #vypsání zašifrované zprávy
        print("")
    if vyber == 2:
        print(4)
          
