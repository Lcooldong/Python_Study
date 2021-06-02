num = int(input())
print("--------------------")
size = 2*num +1


for i in range(size):
    for j in reversed(range(size)):
        if i == j:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(size+1):
        if i == j+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(size-1):
    for j in range(size):
        if j == i+1:
            print("*", end="")
        else:
            print(" ", end="")
    for j in reversed(range(size-1)):
        if j == i+1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

