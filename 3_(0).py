import math
original = 600851475143
num = original

prime_factors = []

i = 2
while i <= num:
    if num%i==0 and i!=1:
        prime_factors.append(i)
        num = num/i
    else:
        if i<=2: i+=1
        else: i+=2

print(prime_factors)
print(max(prime_factors))