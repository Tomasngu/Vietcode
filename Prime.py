def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


 # @timeit
def prime_factors(n):
    prime_factor_list = []
    while not n % 2:
        prime_factor_list.append(2)
        n //= 2
    while not n % 3:
        prime_factor_list.append(3)
        n //= 3
    i = 5
    while n != 1:
        if is_prime(i):
            while not n % i:
                prime_factor_list.append(i)
                n //= i
        i += 2

    return prime_factor_list
def b(n):
    list_b = []
    for num in (prime_factors(n)):
        if num not in list_b:
            list_b.append(num)
    pro = 1        
    for nums in list_b:
        pro *= nums
    return pro
a = 2
for i in range(150):
    print("a_" + str(i+1) +"=" + str(a) + ",b_" +str(i+1) + "=" + str(b(a)) + ",poměr = " + str(a/b(a)))
    a = a + b(a)
    