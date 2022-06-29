def compare(a,b):
    if a>=b:
        return a
    return b
def max(pole):
    for i in range(len(pole)-1):
        if i == 0:
             x = compare(pole[0],pole[1])
        x = compare(x,pole[i+1])
        
    return x

pole = [10,20,5,2,69,1,9,44,144,11]
print(max(pole))

#def max2(pole):
#    pole.remove(max(pole))
#    y = max(pole)
#    return y
#
#z = max2(pole)
#print(z)




    
    
