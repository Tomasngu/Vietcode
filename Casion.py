import random
max_limit = 200
balance = 100
dacos = 0
me = 0
pocet_hodu = 0

while True:
    for i in range(3):
        c_dacos = random.randint(1,6)
        c_me = random.randint(1,6)
        dacos += c_dacos
        me += c_me
        
    if dacos > me:
        balance += -10
    elif dacos<me:
        balance += 10
    print(balance)
    pocet_hodu += 1
    if balance <= 0:
        print("Dacos ripped you off")
        break
    if balance >= max_limit:
        print("Congratulations")
        break
print(pocet_hodu * 2)
    