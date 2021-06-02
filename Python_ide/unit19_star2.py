h = int(input())

size = 2*h - 1

for i in range(h):
    for j in reversed(range(h)):
        if j > i:
            print(' ', end = "")
        else:
            print("*", end = "")
    for j in range(h):
        if j< i:
            print("*", end = "")
    print()
