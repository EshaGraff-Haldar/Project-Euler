for j in range(999,100, -1):
    for x in range(999, 100, -1):
        prod = j*x
        product = str(prod)
        palindrome = True
        for i in range(len(product)//2):
            if product[i] != product[-i-1]:
                palindrome=False
                break
        if palindrome==True:
            lowest_ans = prod
            print(lowest_ans)
            break
    if palindrome==True: break

m = lowest_ans
for j in range(999,100, -1):
    for x in range(999, 100, -1):
        prod = j*x
        if prod <= m:
            break
        product = str(prod)
        palindrome = True
        for i in range(len(product)//2):
            if product[i] != product[-i-1]:
                palindrome=False
                break
        if palindrome==True:
            if prod > m: m = prod
print(m)