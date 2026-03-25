# 4n**2 - 4n + 1
s = 0
for i in range(1, 961001):
    if i%2==1:
        s+= i*i
print(s)