print('--------1번---------')


def calc(num1, op, num2):
    if op == '+':
        result = num1 + num2
        return print(f'{num1:.2f}+{num2:.2f}={result:.2f}')
    elif op == '-':
        result = num1 - num2
        return print(f'{num1:.2f}-{num2:.2f}={result:.2f}')
    elif op == '*':
        result = num1 * num2
        return print(f'{num1:.2f}x{num2:.2f}={result:.2f}')
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
            return print(f'{num1:.2f}÷{num2:.2f}={result:.2f}')
        else:
            return print('불능')
        
calc(10,'+',2)
calc(10.5,'-',2.1)
calc(3,'*', 2.5)
calc(10,'/',2)
calc(4,'/',0)

print('--------2번---------')


def DoubleNum(x, y):
    if x != 0 and y != 0:
        if x % y == 0:
            return print("{}는 {}의 배수입니다.".format(x, y))
        else:
            return print("{}는 {}의 배수가 아닙니다.".format(x, y))
    elif x == 0 and y != 0:
        return print('0은 모든 수의 배수입니다.')
    else:
        return print('0은 0의 배수가 아닙니다.')

DoubleNum(16, 4)
DoubleNum(16, 5)
DoubleNum(16, 0)
DoubleNum(0, 15)
DoubleNum(0, 0)

print('--------3번---------')


def sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum +=i
    return sum

print("{}".format(sum(1, 10)))
print("{}".format(sum(1, 3) + sum(5, 7)))



print('--------4번---------')


def Factorial(n):
    if n == 1:
        return 1
    return n * Factorial(n-1)
    
    
print("{}".format(Factorial(5)))



print('--------5번---------')


def Fibo(n):
    if n <= 1:
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)

print("{}번째입니다.".format(Fibo(3)))


print('--------6번---------')
import numpy as np

def ShowBit(n):
    a = []
    while n >= 1:
        if n % 2 == 0:
            a.append(0)
        else:
            a.append(1)
        n //= 2

    for i in range(1, len(a)):
        if len(a) <= i * 4:
            length = i * 4
            break

    # b = np.zeros((length)) 0.0으로 채워짐
    b = np.full(length, 0)
    start = len(b) - len(a)
    index = int(length / 4)
    b[start:] = list(reversed(a))
    four2 = b.reshape(index, 4)
    # four = [ list(b[4*i:4*i+4]) for i in range(index)] 1차원배열이 나와서 고민좀해야

    for i in range(index):
        for j in range(4):
            print(four2[i, j], end="")
        if i != index - 1:
            print(" ", end="")

ShowBit(16)

print()

print('--------7번---------')

def Check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

    
# a = int(input("정수를 입력하시오. : "))
a = 5
while a < 2:
    print("2이상인 숫자를 입력하세요.\n")
    a = int(input("정수를 입력하시오. :"))

if Check(a):
    print(f"{a}은(는) 소수입니다.")
else:
    print(f"{a}은(는) 소수가 아닙니다.")


