last = 1
new = 2
count = 2
s = 0
while new < 4000000:
    if (count+1)%3==0: s += new 
    count+=1
    new, last = new + last, new
print(s)