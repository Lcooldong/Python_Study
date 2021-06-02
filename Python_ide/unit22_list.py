#from collections import deque
#a = deque([10,20,30])
a = [10, 20, 30]
print(a)

a.append(40)
print(a)

#a.popleft()
#print(a)

#a.appendleft(10)
#print(a)

a.pop()
print(a)

print(a.index(30))

a.extend([40,40,40])
print(a)
print(a.count(40))

a.reverse()
print(a)

del a[1]
print(a)

a.remove(40)
print(a)

a.sort()
print(a)

a.pop(2)
print(a)

a.clear()
print(a)

a.extend([10,20,30])
del a[:]
print(a)

a.extend([40,50,60])
a[len(a):] = [80,90]
print(a)

if not len(a):
    print("비어있음")
else:
    print("채워져 있음")

if a:
    print("채워져 있다고")


b = [0, 0, 0, 0]
c =b.copy()
d = b

print(b)
print(c)

print(b is c)
print(b == c)
print(b is d)

for i in [38, 21, 53, 62, 19]:
    print(i)

for index, value in enumerate(a):
    print(index+1, value)

for index, value in enumerate(a, start = 1):
    print(index, value)

e = [11, 23, 45, 16]
for i in range(len(e)):
    print(e[i])

k = 0
while k < len(e):
    print(e[k])
    k +=1

f = [11, 12 , 13, 5, 17]
smallest = a[0]
largest = a[1]
for i in f:
    if i < smallest:
        smallest = i
    
for j in f:
    if j > largest:
        largest  = j

print(largest)
print(smallest)

f.sort()
print(f, end =" ")
print(f[0])



f.sort(reverse = True)
print(f, end =" ")
print(f[0])

x = 0
for i in f:
    x +=i

print(x)

print(sum(f))
print(max(f))
print(min(f))

g = [i for i in range(10) if i % 2 == 0]
print(g)
h = list((i+2)*3 for i in range(10))
print(h)

o = [i*j for i in range(1, 10)
         for j in range(2, 10)]
print(o)

p = [1.2, 2.5, 3.6, 4.1]
for i in range(len(p)):
    p[i] = int(p[i])

print(p)

r = [1.4, 12.1, 11.5]
r = list(map(int, r))
print(r)

s = map(str, range(5))
print(s)

t = list(map(str, range(5)))
print(t)

a, b = [10, 20]
print(a)
print(b)

#x = input().split()
#m = map(int,x)
#a,b = m  # 맵 객체는 변수 여러개에 저장가능
#print(a,b)

a = [10,20,30]
a[-1:]=[40]
print(a)

for i in a:
    print(i)

i = 0
while i<len(a):
    print(a[i])
    i +=1

print(len(a))

#for i in a:
#    print(a[i])

b = (10, 20)
print(b[:])

a = ["alpha", "bravo", "charile", "delta", "echo","foxtrot", "golf", "hotel", "india" ]
b = [i for i in a if len(i) == 5]
print(b)


