def je_sude(pole):
    suda_cisla = []
    for prvek in pole:
        if prvek % 2 == 0:
            suda_cisla.append(prvek)
    return suda_cisla


pole = [1,1,5,3,8,12]
print(je_sude(pole))
            
