from pprint import pprint

a =[[10, 20],
    [30, 40],
    [50, 60] ]

pprint(a, indent = 2, width = 20)

print(a)

print(a[1][0])

print("------------------------")

b = []
b.append([])
b[0].append(10)
b[0].append(20)
b.append([])
b[1].append(30)

print(b)

print("------------------------")

for x, y in a:
    print(x, y)

print("------------------------")

for x in a:
    for y in x:
        print(y, end = " ")
    print()

print("------------------------")

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = " ")
    print()

print("------------------------")

i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1

print("------------------------")


i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end = " ")
        j += 1
    print()
    i += 1

print("------------------------")


a = []

for i in range(10):
        a.append(0)
        
print(a)

print("------------------------")


a = []

for i in range(3):
    line  =[]
    for j in range(2):
        line.append(0)
    a.append(line)

print(a)


print("------------------------")


a = [[0 for j in range(3)] for i in range(4)]
pprint(a, indent = 2, width = 20)


print("------------------------")

a = [[0]*3 for i in range(3)]
pprint(a, indent = 2, width = 20)


print("------------------------")

a = [3, 1, 3, 2, 5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
pprint(b, indent = 2, width = 20)


print("------------------------")

a = [ [0]* i for i in [1, 2, 3, 4 ,5]]
pprint(a, indent = 2, width = 20)


print("------------------------")

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
    
]
#이름순
print(sorted(students, key = lambda student:student[0]))
#알파벳순
print(sorted(students, key = lambda student:student[1]))
#숫자순
print(sorted(students, key = lambda student:student[2]))

print("------------------------")

#2차원 리스트에서는 copy 말고 deepcopy로 해야 다름
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 200
print(a)
print(b)

a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a)

b[0][0] = 100
print(a)
print(b)

print("------------------------")

for i in a:
    for j in i:
        print(j)


print([[0, 0, 0] for i in range(3)])

print("------------------------")


a =[[[0 for i in range(3)] for j in range(4)] for k in range(2)]
print(a)
