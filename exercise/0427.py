def twist(x, y):
    n = x
    x = y
    y = n
    return x, y

result = twist(1, 2)

print(result)   #튜플로 받아짐