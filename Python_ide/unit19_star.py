h = int(input())

size = 2*h - 1

for i in range(h):
    for j in range(size):
        if ((h+i) <=j) or ((i+j)<=(h-2)):           
            print(" ", end = "")
        else:
            print("*", end = "")
        
    print()
