import math
refPi = math.pi
Pi = 0
i = 0
while True:
    Pi += 1/(4*i+1)
    Pi -= 1/(4*i+3)
    i += 1
    print(4*Pi)
    if (refPi - 4*Pi) < 0.00001:
        break