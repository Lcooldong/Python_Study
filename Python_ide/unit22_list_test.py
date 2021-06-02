a, b = map(int, input().split())

num = 1
for i in range(1, a+1):
        num = num*2


c = []

for j in range(a, b+1):
    
    c.append(num)
    num *= 2
    

del c[1]
del c[-2]    
print(c)



