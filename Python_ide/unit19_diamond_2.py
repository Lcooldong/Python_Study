n = int(input())


print(" "*(n-1),"*")

for i in range(1,n+1):
    print(" "*(n-i), end="")  
    print("*", end="")
    print(" "*i, end="")
    print(" "*(i-1) + '*')

    
for i in range(n-1,0,-1):
    print(" "*(n-i), end="")
    print("*", end="")
    print(" "*i, end="")
    print(" "*(i-1) + '*')
    
print(" "*(n-1),"*")
