prime_factors_list = []
for num in range(1, 21):
    prime_factors =[]
    i = 2
    while i <= num:
        if num%i==0 and i!=1:
            prime_factors.append(i)
            num = num/i
        else:
            if i<=2: i+=1
            else: i+=2
    for x in prime_factors:
        diff = prime_factors.count(x) - prime_factors_list.count(x)
        if diff>0:
            for d in range(diff): prime_factors_list.append(x)

print(prime_factors_list)
s = 1
for j in prime_factors_list: s*=j
print(s)
