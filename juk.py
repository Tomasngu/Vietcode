T = int(input())                                       #Počet problémů
for i in range(T):                                     #Pro každý problém:
    M, N =  [int (c) for c in input().split()]         #Načti M(počet molekul)
                                                       #a N(délka molekul)
    molecule = []
    for j in range(M):                                 #Pro každou molekulu:
        int_array = [int(c) for c in input().split()]  #Načti její složení
        molecule.append(int_array)                     #Přidej jej k ostatním
    output = []
    for j in range(N):                                 #Pro každou pozici:
        total = sum([molecule[k][j] for k in range(M)])#Sečti hodnoty na
                                                       #daném místě
        output.append(total % 2)                       #Vezmi zbytek součtu po
                                                       #dělení 2 a přidej
                                                       #k předešlým výsledkům
    output_str = [str(output[c]) for c in range(N)]    #Převeď na stringy
    print(' '.join(output_str))                        #Vypiš oddělené mezerami

