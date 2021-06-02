def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)





print(fib(10))

print("----------------일반함수-----------------")
def fib(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1

    for i in range(1, n):
        a, b = b, a + b

    return a
print(fib(10))

print("----------------람다1-------------------")
fib = lambda n: 1 if n<=2 else fib(n-1) + fib(n-2)
print(fib(10))

print("----------------람다2-------------------")
fib = lambda n, a=0, b=1 : a if n<=0 else fib(n-1,b, a+b)
print(fib(10))

print("----------------메모이제이션---------------------")

def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append(fibList[i-1] + fibList[i-2])
    return fibList
print(fib(10))

print("-------------------제너레이터------------------")
def fibs():
    a,b = 0,1
    while True:
        a,b = b, a+b
        yield a

f = fibs()
print(next(f))
