n = 30

for i in range(n):
    for j in range(n):
        if i%2 == 0 and j%2 == 0:    
            print("@",end="")
        if i%2 == 0 and j%2 != 0:
            print(" ",end="")
        if i%2 != 0 and j%2 != 0:
            print("@",end="")
        if i%2 != 0 and j%2 == 0:
            print(" ",end="")       
    print()


print("--------------------")


for i in range(n):
    for j in range(n):
        if i%2 == 0:
            if j%2 == 0:    
                print("@",end="")
            else:
                print(" ",end="")  
        else:
            if j%2 != 0:
                print("@",end="")
            else:
                print(" ",end="")
                
    print()
