x = list(input())

for j in range(0,len(x)):
    print(" "*j, end = '')
    for i in x[:len(x)-j]:
        print(i, end = '')
    for i in reversed(x[:-j-1]):
        print(i, end = '')
    print("")


