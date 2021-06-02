
# [1,1,2,3,5,8,13,21 ]
a = 1
b = 1
d = 2


for i in range(10):
    print(f"{a} {b}", end = " ")
    c = a + b
    d = c + b
    a, b = c, d
    
print("-------------------------")

a = 1
b = 1
sumP = 2
print("1 1 ", end = "")
for i in range(10):
    c = a + b
    sumP += c #전체 합계
    a,b = b, c
    print(f"{c}", end = " ")
print()
print(f"합계 {sumP}")
   

print("세 수를 입력하세요 : ", end = "")
a,b,c = map(int, input().split())

max = a
min = a

if b>= max:
    max = b
else:
    min = b

if c >= max:
    max = c
else:
    min = c
    
print(f'max = {max}, min = {min}')

print("-------------------------")

print("두 수를 입력하세요 : ", end = "")
a, b = map(int, input().split())

if a > b:
    c = a-b
    b = 0
elif b > a:
    c = b-a
    a =0
else:
    c = a-b
    a = 0
    b = 0

print(f"a ={a}, b ={b}, c={c}")

print("-------------------------")

a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] % 2 == 0:
        print("even")
    else:
        print("odd")



